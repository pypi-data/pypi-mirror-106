import pandas as pd 

def activeUnit(unit, master, trademark):
    unit_set = pd.merge(unit, master[['Operator Name', 'SerialNumber', trademark]], on='SerialNumber', how='left')
    unit_set = unit_set.loc[unit_set[trademark]=='Yes']
    unit_set = unit_set.rename(columns={trademark: 'Active'})
    unit_set['Trademark'] = trademark
    unit_set = unit_set.reset_index()
    
    return unit_set
