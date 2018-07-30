# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 01:47:39 2017

@author: kousy
"""

import matplotlib.pyplot as plt
import plotly as plot
import pandas as pd
import plotly.offline as offline

vis=pd.read_csv('post_refinement.csv',delimiter='|')
vis=pd.DataFrame(vis)
vs = vis[['Gender','Topic','Sample_Size']]
vs3 = pd.DataFrame(vs.groupby(['Gender','Topic'])['Sample_Size'].sum())

#Implementation of FILE concept
vs3.to_csv('question3.csv',sep='|',encoding='utf-8')
vs3 = pd.read_csv('question3.csv',delimiter='|')

ssdnd = vs3['Sample_Size'][(vs3['Gender'] == "Do not wish to Disclose")]
ssfem = vs3['Sample_Size'][(vs3['Gender'] == "Female")]
ssmal = vs3['Sample_Size'][(vs3['Gender'] == "Male")]

#Implementation of DICTIONARY
data1 = [{"x": vs3['Topic'] , "y": ssfem, 'name':"Female", 'type':'bar'},
              {"x": vs3['Topic'] , "y": ssmal, 'name':"Male", 'type':'bar' }]
layout1 = dict(title = 'Classification of Classes based on Gender')

fig = dict(data=data1, layout=layout1)
offline.plot(fig)