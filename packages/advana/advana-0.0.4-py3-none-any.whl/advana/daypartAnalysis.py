import pandas as pd 

def daypartAnalysis(day, ref, trademark):
    
    daypart = day.loc[day['Trademark']==trademark]
    ref = ref.loc[ref['Trademark']==trademark]
    
    daypart = pd.merge(daypart, ref[['SerialNumber','Status']], on='SerialNumber', how='left')
    daypart = daypart.groupby(['Operator Name', 'Hour', 'Status'])['TransID'].nunique()
    daypart = daypart.to_frame().reset_index()
    average = daypart['TransID'].mean()
    daypart['Transactions'] = (daypart['TransID']/average)*100
    daypart['Trademark'] = trademark
    
    return daypart 
