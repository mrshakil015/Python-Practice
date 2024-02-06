import numpy as np
import pandas as pd

student_dict = {
    "Name":['Shakil','Ridoy','Shaiful','Banna'],
    "ID":[15,11,14,13],
    "Address":['Hemayetpur','Kollanpur','Savar','Mirpur'],
    "Age":[23,24,26,25]
}
students_tab = pd.DataFrame(student_dict)
print("Students List:\n",students_tab)
students_tab.to_csv('list.csv')
students_tab.to_csv('list_without_index.csv', index=False)
print("Show the first 2 rows:\n",students_tab.head(2))
print("Show the last 2 rows:\n",students_tab.tail(2))
print("\nDescribe the data frame:\n",students_tab.describe())
studentList2 = pd.read_csv('StudentList.csv')
print("\nStudents List 2:\n",studentList2)
print("Print the student list 2 Marks:\n",studentList2['Roll NO'])
print("Print 1 index student roll:",studentList2['Roll NO'][1]) 

newdf1 = pd.DataFrame(np.random.rand(300,4), index=np.arange(300))
print("Random Data Set generate:\n", newdf1)
print(newdf1.dtypes)
print(newdf1.head())
print(newdf1.tail())
print(newdf1.describe())

newdf1[0][0] = 'Shakil'
print(newdf1.head())
print(newdf1.dtypes)
print(newdf1.columns)
print(newdf1.sort_index(axis=0, ascending=False))
print(newdf1.sort_index(axis=0))
newdf1.columns = list("ABCD")
newdf1.loc[0,'B'] = 64661
print(newdf1.head())
print(newdf1.drop('D', axis=1))
print("\nShow the specific row and  columns:\n",newdf1.loc[[1,2,3,7],['C','A']])
print("\nshow the specific row and  all columns:\n",newdf1.loc[[1,25,31,75],:])
print("\nSpecific Value wise filter the dataframe:\n",newdf1.loc[(newdf1['A']=="Shakil")])
print(newdf1.iloc[0,1])
newdf1.drop([1,4,7,9], axis=0,inplace=True)
print(newdf1.head(5))

print(newdf1.reset_index(drop=True))
print(newdf1['B'].isnull())

newdf2 = pd.read_csv('dataframe.csv')
print(newdf2)
print("Drop the null value:\n",newdf2.dropna())
print("Drop the duplicates value & keep single one:\n",newdf2.drop_duplicates(subset=['Roll NO']))
print("Drop the duplicates value & keep first duplicates value:\n",newdf2.drop_duplicates(subset=['Roll NO'],keep='first'))
print("Drop the duplicates value & keep last duplicates value:\n",newdf2.drop_duplicates(subset=['Roll NO'],keep='last'))
print("Drop the duplicates all values:\n",newdf2.drop_duplicates(subset=['Roll NO'],keep=False))
print(newdf1.shape)
print(newdf2)
print("Data Frame Info:\n",newdf2.info())
print(newdf2.notnull())
newdf3 = pd.read_excel('instututesdf.xlsx')
print("Institute data frame:\n", newdf3)
print(pd.read_excel('institutesdf.xlsx', sheet_name='teclist'))
dataf =pd.read_excel('institutesdf.xlsx', sheet_name='teclist')
dataf.iloc[0,0] = 50
print(dataf)
