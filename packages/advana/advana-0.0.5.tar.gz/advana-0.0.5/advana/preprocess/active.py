import pandas as pd 

def active_unit(unit, master, trademark):
    unit_set = pd.merge(unit, master[['Operator Name', 'SerialNumber', trademark]], on='SerialNumber', how='left')
    unit_set = unit_set.loc[unit_set[trademark]=='Yes']
    unit_set = unit_set.rename(columns={trademark: 'Active'})
    unit_set['Trademark'] = trademark
    unit_set = unit_set.reset_index()
    
    return unit_set

def active_imp(imp, master, trademark):
    imp_set = pd.merge(imp, master[['Operator Name', 'SerialNumber', trademark]], on='SerialNumber', how='left')
    imp_set = imp_set.loc[imp_set[trademark]=='Yes']
    imp_set = imp_set.rename(columns={trademark:'Active'})
    imp_set['Trademark'] = trademark
    imp_set = imp_set.reset_index()
    
    return imp_set

def active_day(day, master, trademark):
    day_set = pd.merge(day, master[['Operator Name', 'SerialNumber', trademark]], on='SerialNumber', how='left')
    day_set = day_set.loc[day_set[trademark]=='Yes']
    day_set = day_set.rename(columns={trademark: 'Active'})
    day_set['Trademark'] = trademark
    day_set = day_set.reset_index()
    
    return day_set