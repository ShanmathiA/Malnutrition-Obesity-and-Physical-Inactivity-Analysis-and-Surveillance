# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 02:28:13 2017

@author: kousy
"""
import pandas as pd

datafile1=pd.read_csv('post_refinement.csv',delimiter='|')
datafile1=pd.DataFrame(datafile1)
"""
Standard Deviation
"""
sd=datafile1[['Data_Value']].std()
print("Standard Deviation:",sd)

"""
Mean/Average
"""
avg=datafile1[['Sample_Size']].mean()
print("Mean/Average:",avg)
"""
Median
"""
med=datafile1[['Data_Value']].median()
print("Median:",med)
"""
Maximum
"""
maxi=datafile1[['Sample_Size']].max()
print("Maximum:",maxi)

