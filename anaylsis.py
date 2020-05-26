# -*- coding: utf-8 -*-
"""
Created on Mon May 25 18:02:34 2020

@author: Luming
"""

import pandas as pd
import time
import os
import numpy as np

#read the file name to list
cle_datime=[]
data_time=[]
file_list=[]
x=[]
y=[]
z=[]
time=[]
count=[]
for dirPath, dirNames, fileNames in os.walk("./test_data"):
    print (dirPath)
    for f in fileNames:
        cle_datime.append(f)
        with open('./test_data/'+f,'r') as k:
            aa=k.readlines()
            for i in range(len(aa)):
                file_list.append(aa[i].strip('[]').split(','))
    