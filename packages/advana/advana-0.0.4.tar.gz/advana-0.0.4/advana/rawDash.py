import pandas as pd 

def rawDash(roll, imp, trademark, start, end):
    
    unit_set = roll.loc[roll['Trademark']==trademark]
    unit_set = unit_set.loc[(unit_set['WeekNo']>start-1)&(unit_set['WeekNo'] < end+1)]
    
    imp_set = imp.loc[imp['Trademark']==trademark]
    imp_set = imp_set.loc[(imp_set['WeekNo'] > start-1) & (imp_set['WeekNo'] < end+1)]
    
    op_unit = unit_set.groupby(['Operator Name', 'SerialNumber'])['SalesCount'].sum()
    op_sales = unit_set.groupby(['Operator Name', 'SerialNumber'])['NetSalesRevenue'].sum()
    op_imp = imp_set.groupby(['Operator Name', 'SerialNumber'])['Transactions'].sum()
    
    def to_frame(sets):
        sets = sets.to_frame()
        sets = sets.reset_index()
        return sets 
    
    op_metrics = pd.merge(to_frame(op_unit), to_frame(op_sales)[['NetSalesRevenue', 'SerialNumber']], on='SerialNumber', how='left')
    op_metrics = pd.merge(op_metrics, to_frame(op_imp)[['Transactions', 'SerialNumber']], on='SerialNumber', how='left')
    op_metrics['Trademark'] = trademark
    op_metrics = op_metrics.reset_index(drop=True)
    
    return op_metrics

