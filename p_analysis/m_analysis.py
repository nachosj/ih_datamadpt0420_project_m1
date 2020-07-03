import pandas as pd


def challenge1(mergedtable):
    challenge1_df = mergedtable.groupby(['Country', 'Job Title', 'Age Group']).agg({'uuid': 'count'})
    challenge1_df.columns = ['Quantity']
    challenge1_df = challenge1_df.reset_index()
    challenge1_df['Percentage'] = (challenge1_df['Quantity'] / challenge1_df['Quantity'].sum()*100).round(2).astype(str) + '%'
    challenge1_df.sort_values(by='Quantity', ascending=False, inplace=True)
    return challenge1_df


