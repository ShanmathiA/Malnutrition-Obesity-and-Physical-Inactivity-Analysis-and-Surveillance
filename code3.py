# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 03:54:21 2017

@author: kousy
"""

import matplotlib.pyplot as plt
import pandas as pd
from pylab import *

vis=pd.read_csv('post_refinement.csv',delimiter='|')
vis=pd.DataFrame(vis)

vis1=vis[['Topic']]

new = vis1['Topic'].value_counts()

cnt = new.iloc[0:].tolist()

figure(1, figsize=(3,3))
#Implemenation of LIST
labels = ['Obesity / Weight Status','Fruits and Vegetables - Behavior','Physical Activity - Behavior','Television Viewing - Behavior','Sugar Drinks - Behavior']

#Implementation of TUPLES
explode=(0.2, 0, 0, 0,0) 
pie(cnt, labels=labels,explode=explode,
                autopct='%1.1f%%', shadow=True, startangle=90)

plt.show()