import pandas as pd 

def rollingSales(unit, ref, trademark):
    
    roll = unit.loc[unit['Trademark']==trademark]
    ref = ref.loc[ref['Trademark']==trademark]
    
    roll_sales = pd.merge(roll, ref[['SerialNumber', 'Status']], on='SerialNumber', how='left')
    roll_sales = roll_sales.reset_index(drop=True)
    
    roll_sales = roll_sales.groupby(['Operator Name', 'WeekNo', 'Status'])['SalesCount'].sum()
    
    def to_frame(sets):
        sets = sets.to_frame().reset_index()
        return sets 
    
    roll_sales = to_frame(roll_sales)
    roll_sales['Trademark'] = trademark 
    
    return roll_sales