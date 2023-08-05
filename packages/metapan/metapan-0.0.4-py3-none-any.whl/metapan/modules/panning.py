import pandas as pd 
from multiprocessing import  Pool
import numpy as np
import os
import gzip
class pann:

    def __init__(self,InputFileDir,metadata,groupingColumn,OutDirPath,PrefixForFilename,Thread):
        self.InputFileDir = InputFileDir
        self.metadata = metadata
        self.groupingColumn = groupingColumn
        self.OutDirPath = OutDirPath
        self.PrefixForFilename = PrefixForFilename
        self.Thread= Thread

    def fileProcessing(self):
        # for 

def panningEntry():



