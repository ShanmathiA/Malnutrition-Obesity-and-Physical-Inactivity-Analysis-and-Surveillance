# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 00:18:48 2017

@author: kousy
"""


import matplotlib.pyplot as plt
import pandas as pd
vis=pd.read_csv('post_refinement.csv',delimiter='|')
vis=pd.DataFrame(vis)
vs = vis[['Data_Value','YearStart']]
vs1 = vs.groupby('YearStart')['Data_Value'].mean()
print(vs1)
ax=vs1.plot(kind='line', title="Diagnostic Rate over the years", figsize=(15,15), legend=True, fontsize=15, color='green')
ax.set_xlabel("Year", fontsize=15)
ax.set_ylabel("Diagnostic Rate", fontsize=15)
plt.show()