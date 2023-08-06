import pandas as pd 

def activeImp(imp, master, trademark):
    imp_set = pd.merge(imp, master[['Operator Name', 'SerialNumber', trademark]], on='SerialNumber', how='left')
    imp_set = imp_set.loc[imp_set[trademark]=='Yes']
    imp_set = imp_set.rename(columns={trademark:'Active'})
    imp_set['Trademark'] = trademark
    imp_set = imp_set.reset_index()
    
    return imp_set