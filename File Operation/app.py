#Open and Read File
f = open("File Operation/demo.txt","r")
data = f.read()
print(data)
f.close()

print("\n")
#---Open and Read Line by line
file = open("File Operation/demo.txt","r")
line = file.readline()
print(line)
file.close()

print("\n")
#---Read all lines into a list
file2 = open("File Operation/demo.txt","r")
allline = file2.readlines()
print(allline)
file2.close()

print("\n")
#-------Write File---
# Open a file for writing
fileW = open("File Operation/demo.txt", "w")
fileW.write("To write data to a file, we need to open it in write mode ('w').")
# Close the file
fileW.close()

#-------Write and Read File---
# Open a file for writing
fileWR = open("File Operation/demo.txt", "w+")
fileWR.write("To write data to a file, we need to open it in write mode ('w').")
print(fileWR.read())
# Close the file
fileW.close()



#---Append data into the file
fileA = open("File Operation/demo.txt", "a")
fileA.write("This is a new line.")
fileA.close()

#---Read and Append
fileAR = open('File Operation/demo.txt', 'a+')

# Reading existing content
print("Read and Append existing content:")
fileAR.seek(0)  # Move the pointer to the beginning of the file
print(fileAR.read())

# Appending data
fileAR.write("Appending some more data.\n")

fileAR.close()
