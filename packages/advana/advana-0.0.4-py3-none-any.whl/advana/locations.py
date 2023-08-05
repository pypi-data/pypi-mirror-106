def locations(roll, trademark, start, end):
    
    roll = roll.loc[roll['Trademark']==trademark]
    roll_loc = roll.sort_values(by=['WeekNo']).drop_duplicates(subset='SerialNumber', keep='first')
    roll_loc.loc[(roll_loc['WeekNo'] > start-1) & (roll_loc['WeekNo'] < end+1), 'Status'] = 'New'
    roll_loc['Status'] = roll_loc['Status'].fillna('Existing')
    roll_loc = roll_loc.reset_index(drop=True)
    
    return roll_loc
