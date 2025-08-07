import pandas as pd

data  = {
    'Name' : ['Ali','Saleem','Usman'],
    'Age' : [23,24,56],
    'Grade' : ['A','B','A']
}

df = pd.DataFrame(data)
print(df)

#df2= pd.read_csv('students_data.csv')
#print(df.head())

print(df[df['Grade'] == 'A'])
print(df[df['Age'] > 22])

df_sorted = df.sort_values(by='Age',ascending=False)
print(df_sorted)

grouped = df.groupby('Grade').size()
print(grouped)

df_sorted.to_csv('output.csv',index=False)
df.to_excel('output.xlsx',index=False)