import os
import sys
from multiprocessing import Queue, Process, cpu_count
import gzip
import filetype
import pandas as pd
# import shutil
# import tarfile

__author__ = "Anupam_Gautam"


class CombinerClass:

    def __init__(self,TakeFileDirectory,TakeCounter,TakeOrganismNameToSend,TakeOutPutFileName,TakeThread):

        self.TakeFileDirectory=TakeFileDirectory
        self.TakeCounter=TakeCounter
        self.TakeOrganismNameToSend=TakeOrganismNameToSend
        self.TakeOutPutFileName=TakeOutPutFileName
        self.TakeThread=TakeThread
    
    def getFileList(self,DataFrame):
        '''
        Returns the list of files in specified folder.
        '''
        filelist = []
        counter=self.TakeCounter
        for value in DataFrame.iloc[:,0].to_list():
            counter=counter+1
            filepath=os.path.abspath(os.path.join(self.TakeFileDirectory,value))
            filepath=str(counter)+"&"+filepath
            filelist.append(filepath)
        
        return filelist

    def Parallelizer(self,ListOffiles):
        q = Queue()
        procs = []
        for i in range(0,int(self.TakeThread)):
        # Split the source filelist into several sublists.
            lst = [ListOffiles[j] for j in range(0, len(ListOffiles)) if j % int(self.TakeThread) == i]
            if len(lst)>0:
                #p = Process(target=FastaDetailProcessor, args=([lst, q,RecieveFilepath]))
                p = Process(target=self.FastaFileProcessor , args=([lst,self.TakeOrganismNameToSend,self.TakeOutPutFileName,q]))
                p.start()
                procs += [p]
        # Collect the results:
        all_results = []
        for i in range(0, len(procs)):
        # Save all results from the queue.
            all_results += q.get()

        return(len(ListOffiles))

    @staticmethod
    def FastaFileProcessor(TakeFileNameString,TakeOrganismNameToUse,TakeOutputFileName,q):
        try:
            result=[]
        #workQueue='done'
            for NameOfFile in TakeFileNameString:
                fileName=NameOfFile.split("&")
                orgNumber=fileName[0]
                HeaderFileName=TakeOutputFileName+".Header"
                OrgListFileName=TakeOutputFileName+".Orglist"
                fw=open(TakeOutputFileName+"_InputAll.faa", "a")
                fwHeader=open(HeaderFileName, "a")
                fwOrg=open(OrgListFileName, "a")
                fwOrg.write(str(TakeOrganismNameToUse)+str(orgNumber)+"\t"+str(fileName[1])+"\n")
                kind = filetype.guess(fileName[1])
                #print(kind)
                if kind is not None:
                    if kind.extension in ["gz","bz2"]:
                        f  = gzip.open(fileName[1], "rt")
                    #print(fileName)
                    #ProcessGzFile(NameOfFile,TakeOrganismNameToUse,TakeOutputFileName)
                elif kind is None:
                    # print("hello")
                    f  = open(fileName[1], "r")
                    #ProcessNormalFile(NameOfFile,TakeOrganismNameToUse,TakeOutputFileName)
                firstLine = f.readline()
                Header=firstLine.strip("\n")
                counter=0
                sequence=''
                for line in f:
                    line=line.strip("\n")
                    if '>' in line:
                        counter=counter+1
                        fw.write('>'+str(TakeOrganismNameToUse)+str(orgNumber)+"|"+str(TakeOrganismNameToUse)+str(orgNumber)+"_"+str('gene')+str(counter)+"\n"+str(sequence)+"\n")
                        fwHeader.write('>'+str(TakeOrganismNameToUse)+str(orgNumber)+"|"+str(TakeOrganismNameToUse)+str(orgNumber)+"_"+str('gene')+str(counter)+"\t"+str(fileName[1])+"\t"+str(Header)+"\n")
                        Header=line
                        sequence=''
                    else:
                        sequence=sequence+line
                fw.write('>'+str(TakeOrganismNameToUse)+str(orgNumber)+"|"+str(TakeOrganismNameToUse)+str(orgNumber)+"_"+str('gene')+str(counter)+"\n"+str(sequence)+"\n")
                fwHeader.write('>'+str(TakeOrganismNameToUse)+str(orgNumber)+"|"+str(TakeOrganismNameToUse)+str(orgNumber)+"_"+str('gene')+str(counter)+"\t"+str(fileName[1])+"\t"+str(Header)+"\n")
                sequence=''
                f.close()
                fw.close()
                fwOrg.close()
                fwHeader.close()
            result.append("Done")
        except:
            q.put([])
            raise
        q.put(result)

def CombinerEntry(ReceiveFastaFileDirectory: str="", ReceiveOutputDirectory: str="",ReceiveMetadatfile: str="",ReceiveColumnName: str="", ReceivePrefixForFilename: str="", ReceiveThread: int="") -> None:

    ReceiveOutPutFileName=os.path.abspath(os.path.join(str(ReceiveOutputDirectory),str(ReceivePrefixForFilename)))

    metadatafileInitial=pd.read_csv(ReceiveMetadatfile,sep="\t")
    metadata=metadatafileInitial[['#SampleID',ReceiveColumnName]]
    name=metadata[ReceiveColumnName].unique()
    grouped = [x for _, x in metadata.groupby(ReceiveColumnName)]
    iteratorCount=0
    for numberofGroup in range(0,len(grouped)):

        iteratorCount=iteratorCount+1

        if iteratorCount==1:
            counter=0
        else:
            counter=NumberOfFile

        CombinerClassHandler=CombinerClass(TakeFileDirectory=ReceiveFastaFileDirectory,TakeCounter=counter, TakeOrganismNameToSend=str(name[numberofGroup]+"_Org"), TakeOutPutFileName=ReceiveOutPutFileName, TakeThread=ReceiveThread)
        getFileListReturn=CombinerClassHandler.getFileList(grouped[numberofGroup])
        NumberOfFile=CombinerClassHandler.Parallelizer(getFileListReturn)

    return(ReceiveOutPutFileName+"_InputAll.faa")
    # InitialProcessHandler=InitialProcess(ReceiveFastaFileDirectory,ReceiveOutPutFileName,ReceiveMetadatfile,ReceiveThread)
    # files = InitialProcessHandler.getFileList()

    # #print(files)
    # logging.info('Total Number of Files '+ str(len(files)))
    # NumberOfFile=InitialProcessHandler.Parallelizer(files)

    # tarDir(PathOfDir).tarIt()

