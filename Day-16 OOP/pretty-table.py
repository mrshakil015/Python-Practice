# Pretty tables are the visual representation of the data in tabular forms. These are ASCII tables and easy to use. The prettytable library consists of the PrettyTable class, which is used to create relational tables. To work with this library, we need to install it using the below command.

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name",["PIkachu", "Squirtle", "Charmander"])
table.add_column("Type",["Electric", "Water", "Fire"])
table.align = "l"
print(table)

#--------------Row wise Table-----------
rowTable = PrettyTable(["Student Name", "Class", "Subject", "Makrs"])  
  
name = "rohim"
read = "X"
subject = "cse"
marks = 85

# Add rows  
rowTable.add_row([name, read, subject, marks])
rowTable.add_row(["Camron", "X", "English", "91"])  
rowTable.add_row(["Haris", "X", "Math", "63"])  
rowTable.add_row(["Jenny", "X", "Science", "90"])  
rowTable.add_row(["Bernald", "X", "Art", "92"])  
rowTable.add_row(["Jackson", "X", "Science", "98"])  
rowTable.add_row(["Samual", "X", "English", "88"])  
rowTable.add_row(["Stark", "X", "English", "95"])  

  
print(f"Row wise Pretty Table:\n {rowTable}")  

#----------Column Wise table---------------
columns = ["Student Name", "Class", "Subject", "Makrs"]
columnTable = PrettyTable()  
columnTable.add_column(columns[0],['Rohim', 'Korim'])
columnTable.add_column(columns[1],['X', 'IX'])
columnTable.add_column(columns[2],['Python', 'English'])
columnTable.add_column(columns[3],[85, 84])

print(f"Column wise Pretty Table:\n {columnTable}")  
