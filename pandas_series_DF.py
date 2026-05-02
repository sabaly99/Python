from statistics import stdev
import pandas as pd


#series
Data = [1,23,4,65,3,456,2]
series = pd.Series(Data , index= ['a','b','c','d','e','f','g'] )
print(series)


print('\n '* 2)
#DataFrames
data33 = {
    'Name':['Nana','mmmaman','adbasase','kafgf'],
    'Age': [23,43,12,23],
    'job': ["miner",'doctor','developer','doctor']
}
df = pd.DataFrame(data33)
print(f"orinal frame : \n {df}")
print('\n '* 2)

#modifying by replacing some values in the dictionary
df_filled = df.fillna({'Age':df['Age'].mean()})

print(f"Modified version :\n {df_filled}")
print('\n '* 2)

#modifying by removing duplicate values
rm_duplicates = df.drop_duplicates()
print(f"duplicated removed version: /n {rm_duplicates}")
print('\n '* 2)

#Merging of data
student1 = pd.DataFrame({
    'ID':[1,2,3,4,5],
    'Name':['Nana','Mana','Sana','Vana','Gana'],
    'Score':[93,73,76,85,96,]
})

student2 = pd.DataFrame({
    'ID':[1,2,3,4,5],
    'city':['Accra','NYC','London','Chicago','Atlanta'],
    'Age':[23,21,26,22,23]
})

merged_studs = pd.merge(student1,student2, on = 'ID')
print(merged_studs)
print('\n '* 2)

#sorting of data
sorted_data = merged_studs.sort_values(by='Score')
print(sorted_data)