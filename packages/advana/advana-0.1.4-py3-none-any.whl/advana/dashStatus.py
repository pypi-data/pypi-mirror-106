import pandas as pd

def dashStatus(dash, ref, trademark):
    
    dash1 = dash.loc[dash['Trademark']==trademark]
    ref = ref.loc[ref['Trademark']==trademark]
    
    dashboard = pd.merge(dash1, ref[['SerialNumber', 'Status']], on='SerialNumber', how='left')
    dashboard = dashboard.reset_index(drop=True)
    
    metrics = dashboard.groupby(['Trademark', 'Operator Name', 'Status'])[['SalesCount', 'NetSalesRevenue', 'Transactions']].sum()
    metrics = metrics.reset_index()
    metrics['Avg Price'] = (metrics['NetSalesRevenue'] / metrics['SalesCount'])
 
    return metrics

