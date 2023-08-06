import pandas as pd 

def activeDay(day, master, trademark):
    day_set = pd.merge(day, master[['Operator Name', 'SerialNumber', trademark]], on='SerialNumber', how='left')
    day_set = day_set.loc[day_set[trademark]=='Yes']
    day_set = day_set.rename(columns={trademark: 'Active'})
    day_set['Trademark'] = trademark
    day_set = day_set.reset_index()
    
    return day_set