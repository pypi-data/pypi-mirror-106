import pandas as pd 
import numpy as np
import os
from metapan.modules.utility import OutputDirectoryGenerator,tarDir,gb_to_mb
from metapan.modules.combiner import CombinerEntry

class pann:

    def __init__(self,inputfiledirectory, outputPath, metadatfile, columnname, tool, toolpath, sequenceidentity, wordlength, alignmentcoverage, prefix, threads,ram):

        self.inputfiledirectory = inputfiledirectory
        self.outputPath = outputPath
        self.metadatfile = metadatfile
        self.columnname = columnname
        self.tool = tool
        self.toolpath = toolpath
        self.sequenceidentity = sequenceidentity
        self.wordlength = wordlength
        self.alignmentcoverage = alignmentcoverage
        self.prefix= prefix
        self.threads= threads
        self.ram= ram

    def fileProcessing(self):
        combinedFastaFile=CombinerEntry(ReceiveFastaFileDirectory=self.inputfiledirectory, ReceiveOutputDirectory=self.outputPath, ReceiveMetadatfile=self.metadatfile,ReceiveColumnName=self.columnname,ReceivePrefixForFilename =self.prefix, ReceiveThread=self.threads)
        return(combinedFastaFile)

    def ForCluster(self,TakeFastaFile):

        ram=gb_to_mb(self.ram)
        if self.toolpath:
            if self.tool=='cdhit':
                tool=os.path.abspath(self.toolpath)
            elif self.tool=='usearch':
                tool='usearch'
        else:
            if self.tool=='cdhit':
                tool='cdhit'
            elif self.tool=='usearch':
                tool='usearch'
    # got a non-empty string

        if self.tool =='cdhit':
            stringCdHit=tool+' -i '+TakeFastaFile.strip("\n")+' -o '+TakeFastaFile.replace("_InputAll.faa","")+'   -c '+str(self.sequenceidentity)+' -T '+str(self.threads)+' -n '+str(self.wordlength)+' -d 300 -aL '+str(self.alignmentcoverage)+' -sc 1  -sf 1 -bak 1 -M '+str(ram)#cdhit command
            #print(stringCdHit)
            os.system(stringCdHit)

def panningEntry(inputfiledirectory: str ="", output: str = "metapan", metadatfile: str="",columnname: str="", tool: str ="", toolpath: str="", sequenceidentity: float=0.9, wordlength: int=5, alignmentcoverage: float=0.9, prefix: str="",threads: int="",ram: str = "") -> None:

    DirectoryCaller=OutputDirectoryGenerator(os.path.abspath(output),'metapan')
    PathOfDir=DirectoryCaller.DicGenAndCheck()
    # print(inputfiledirectory, PathOfDir, os.path.abspath(metadatfile), columnname,sequenceidentity, wordlength, alignmentcoverage, prefix,threads,ram)
    pannHandler=pann(inputfiledirectory, PathOfDir, os.path.abspath(metadatfile), columnname, tool, toolpath, sequenceidentity, wordlength, alignmentcoverage, prefix,threads,ram)
    combinedFastaFile=pannHandler.fileProcessing()
    pannHandler.ForCluster(combinedFastaFile)


