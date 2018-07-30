import pandas as pd

"""Importing the Dataset to Python"""
datafile=pd.read_csv('python_project.csv',delimiter='|')
datafile=pd.DataFrame(datafile)

"""Deleting Irrelevant Columns"""
#Implementation of LIST, DATAFRAME
refine=datafile.drop(['YearEnd','Datasource','Data_Value_Unit','Data_Value_Type','Data_Value_Alt','Data_Value_Footnote_Symbol','Data_Value_Footnote','Total','TopicID','DataValueTypeID','QuestionID','LocationID'],axis=1)
refine=pd.DataFrame(refine)
print(refine)

"""
Data Cleaning 1
Removal of Null values in the columns
"""
#Implementation of DATAFRAME
refine1=refine.dropna(subset=['Data_Value','Low_Confidence_Limit'])
refine1=pd.DataFrame(refine1)
print(refine1)

"""
Data Cleaning 2
Providing relevant values to the misfed Values
"""
refine1[['Gender']]=refine1['Gender'].fillna('Do not wish to Disclose')
refine1[['Grade']]=refine1['Grade'].fillna('Does not apply')
print(refine1)

"""
Data Cleaning 3
Spliting GeoLocation value into two columns
"""
refine1['GeoLocation']=refine1['GeoLocation'].str.strip('()')
refine1[['Latitude','Longitude']]=refine1['GeoLocation'].str.split(',',expand=True)
print(refine1)

"""
Saving the DataFrame to a new CSV file
"""
#Implementation of FILE concept
refine1.to_csv('post_refinement.csv',sep='|',encoding='utf-8')
