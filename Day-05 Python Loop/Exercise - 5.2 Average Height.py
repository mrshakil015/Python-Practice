#----- using the normal way calculate the total and average------

total_height =0
no_students =0
students_heights = input("Input a list of student height ").split()
for n in range(0, len(students_heights)):
    students_heights[n] = int(students_heights[n])
    
for height in students_heights:
    total_height += height
    no_students += 1

print("All student heights: ", students_heights)
print("Summation of student height: ",total_height)
print("Average of student height: ",total_height/no_students)

#-----------Using function--------------
print("Student height using Sum function: ", sum(students_heights))
print("No of Student using len function: ", len(students_heights))
print("Average Height using function: ", sum(students_heights)/len(students_heights))


