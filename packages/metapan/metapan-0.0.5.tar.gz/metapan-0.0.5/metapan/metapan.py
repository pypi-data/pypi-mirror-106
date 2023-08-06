from optparse import OptionParser, OptionGroup
import sys
import os
from multiprocessing import Queue, Process, cpu_count
from metapan.modules.panning import panningEntry


__author__ = "Anupam_Gautam"

# def mainFunction(args):
#     print(hello)
def main():
    parser = OptionParser("%prog [options] infile",
                          description="Run pangenome and does comparison at Functional level",
                          epilog=__author__)


    parser.add_option("-i", "--inputfiledirectory", default="", action="store", dest="inputfiledirectory",
                       help="Input file directory",metavar="inputfiledirectory")
    parser.add_option("-o", "--output",default="metapan", action="store", dest="output",
                      help="output folder path [Default: metapan]", metavar="output" )
    parser.add_option("-m", "--metadatafile", action="store",dest="metadatafile",
                       help="Enter name for input File",metavar="metadatafile")
    parser.add_option("-g", "--columnname", action="store",dest="columnname",
                       help="Enter columnname name for grouping",metavar="columnname")
    cluster = OptionGroup(parser,"Clustering Parameter")
    # cluster.add_argument('-m',  metavar='MatrixFile',dest='MatrixFile', required=True,
    #                    help='Enter name for matrix file')
    cluster.add_option("-s", "--tool", default='cdhit', action="store",dest="tool", 
                       help="Enter tool to use for clustering cdhit, usearch etc [Default: cdhit]",metavar="tool")
    cluster.add_option("--toolpath", default='', action="store",dest="toolpath", 
                       help="Enter path to tool to use for clustering cdhit, usearch etc",metavar="toolpath")
    cluster.add_option("-c", "--sequenceidentity", default=0.9, action="store",dest="sequenceidentity", 
                       help="Enter sequence identity threshold, [Default: 0.9]",metavar="sequenceidentity")
    cluster.add_option("-w", "--wordlength", default=5 , action="store",dest="wordlength",  
                       help="Enter word_length, see CD-HIT  user guide for choosing it [Default: 5]", metavar="wordlength")
    cluster.add_option("-a","--alignmentcoverage", dest="alignmentcoverage", action="store", default=0.9,
                       help='Enter alignment coverage for the longer sequence, if set to 0.9 the alignment must covers 90%% of the sequence [Default: 0.9]',metavar='alignmentcoverage')
    parser.add_option_group(cluster)


    GeneralParameter = OptionGroup(parser, "General Parameter")
    GeneralParameter.add_option('-p',"--prefix",action="store",dest='prefix', default="prefix",
                       help='Enter prefix', metavar='prefix')
    GeneralParameter.add_option('-t',"--threads",action="store",dest='threads', default=cpu_count(),
                       help='Enter number of threads', metavar='threads')
    GeneralParameter.add_option('-r',"--ram",action="store",dest='ram', default="4gb",
                       help='Enter ram in gb you want to use [Default: 2gb]',metavar='ram')
    # parser.add_option(GeneralParameter)

    parser.add_option_group(GeneralParameter)
    (options, args) = parser.parse_args()

    # if len(args) == 1:
    #     infile = args[0]
    # elif len(args) == 0:
    #     raise IOError("Must specify input file (use - for stdin)")
    # else:
    #     raise IOError("Too many arguments", args)


    panningEntry(inputfiledirectory=options.inputfiledirectory, output=options.output, metadatfile=options.metadatafile, columnname=options.columnname, tool=options.tool, toolpath=options.toolpath, sequenceidentity=options.sequenceidentity, wordlength=options.wordlength, alignmentcoverage=options.alignmentcoverage, prefix=options.prefix,threads=options.threads, ram=options.ram)

if __name__ == '__main__':
	main()
