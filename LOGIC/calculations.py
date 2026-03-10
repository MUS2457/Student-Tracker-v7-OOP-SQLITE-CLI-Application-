from DATA.class_methods import Student

def class_averages(students):
    averages = Student.students_averages(students)
    if not averages :
        return None
    class_average = round(sum(averages.values()) / len(averages), 2)
    number_of_students = len(students)
    return class_average ,number_of_students

def pass_fail_students (students):
    averages = Student.students_averages(students)
    fail_students = {}
    success_students = {}

    if not averages:
        return fail_students , success_students
    for name , average in averages.items():
        if average < 50 :
            fail_students[name] = average
        else:
            success_students[name] = average
    number_fail_students = len(fail_students)
    number_success_students = len(success_students)

    return (fail_students, success_students,
         number_fail_students, number_success_students)

def below_above_class_average(students):
    averages = Student.students_averages(students)
    below = {}
    above = {}

    if not averages:
        return below, above, None, None

    result = class_averages(students)
    if not result:
        return below, above, None, None

    class_average, number_student = result

    for name, average in averages.items():
        if average < class_average:
            below[name] = average
        else:
            above[name] = average

    number_student_below = len(below)
    number_student_above = len(above)

    return below, above, number_student_below, number_student_above

def top_low_students (students):
    averages = Student.students_averages(students)
    if not averages :
        return None, None,None,None
    top = max(averages, key=averages.get)
    low = min(averages, key=averages.get)

    return top, low, averages[top], averages[low]

def subjects_per_student (students):
    subject_count = {}
    if not students :
        return {}
    for name, obj in students.items():
        subject_count[name] = len(obj.subjects)
    return subject_count

def valid_invalid_subjects(students):
    validated_subjects = {}
    invalidated_subjects = {}

    for name, obj in students.items():
        for subject, score in obj.subjects.items():
            # We first check if the student key exists in the dictionary.
            # If it doesn't exist, we create an empty dictionary for that student.
            # This prevents KeyError and allows us to store multiple subjects
            # per student without overwriting previous ones.

            if score > 50:
                if name not in validated_subjects:
                    validated_subjects[name] = {}
                validated_subjects[name][subject] = score

            else:
                if name not in invalidated_subjects:
                    invalidated_subjects[name] = {}
                invalidated_subjects[name][subject] = score

    return validated_subjects, invalidated_subjects

def students_grade (students):
    grades = {}
    averages = Student.students_averages(students)
    if not averages :
        return grades
    for name, average in averages.items():
        if 90 <= average <= 100:
            grade = "A"
        elif 80 <= average < 90:
            grade = "B"
        elif 70 <= average < 80:
            grade = "C"
        elif 50 <= average < 70:
            grade = "D"
        else:
            grade = "F"
        grades[name] = grade

    return grades

def class_grade(students):
    result = class_averages(students)

    if not result:
        return None

    class_average, number_of_students = result

    if 80 <= class_average < 90:
        grade = "A"
    elif 70 <= class_average < 80:
        grade = "B"
    elif 60 <= class_average < 70:
        grade = "C"
    elif 50 <= class_average < 60:
        grade = "D"
    else:
        grade = "F"

    return grade
