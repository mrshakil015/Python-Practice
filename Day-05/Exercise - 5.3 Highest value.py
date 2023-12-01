#---- Using normal approch find out the maximum value-------

student_scores = input("Input a list of student scores: ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print("Student scores: ", student_scores)

initial_score = 0
for score in student_scores:
    if score > initial_score:
        initial_score = score
print("Highest Score: ", initial_score)


#---- Using function find out the maximum value-------

print("Highest Score using max: ", max(student_scores))