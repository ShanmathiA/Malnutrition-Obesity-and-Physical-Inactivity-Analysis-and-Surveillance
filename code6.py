# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 17:19:20 2017

@author: Shanmathi
"""

import matplotlib.pyplot as plt
import plotly as plot
import pandas as pd
import plotly.offline as offline
import plotly.graph_objs as go

#Implementation of FUNCTION
def stateanalysis(statevalue):
    ss_name = vs['Sample_Size'][(vs['LocationDesc'] == statevalue)]
    dv_name = vs['Data_Value'][(vs['LocationDesc'] == statevalue)]
    trace = go.Scatter(
                x = ss_name,
                y = dv_name,
                mode = 'markers',
                marker=dict(size='16',color='crimson',colorscale='Viridis')
            )
    return(trace)
    
vis=pd.read_csv('post_refinement.csv',delimiter='|')
vis=pd.DataFrame(vis)
vs = vis[['LocationDesc','Data_Value','Sample_Size']]
statename = input("Enter the name of the state to analyze:")
trace = stateanalysis(statename)
data = [trace]

#Implementation of DICTIONARY
layout = dict(title = 'Data Value and Sample Size comparison')
fig = dict(data=data,layout=layout)

offline.plot(fig)

