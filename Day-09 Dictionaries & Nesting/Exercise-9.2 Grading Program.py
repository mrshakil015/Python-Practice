student_socres = {
    "Hannan": 81,
    "Roni": 78,
    "Shamim": 99,
    "Jahid":74,
    "Rohim":70
}
student_grades={}

for key in student_socres:
    score = student_socres[key]
    if score >=91 and score <=100:
        student_grades[key] = "Outstanding"
    elif score >=81 and score <=90:
        student_grades[key] = "Exceeds Expectations"    
    elif score >=71 and score <=80:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

print("Student Grade is:\n",student_grades)