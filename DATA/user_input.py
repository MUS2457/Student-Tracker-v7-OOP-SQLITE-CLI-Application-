from DATA.class_methods import Student

def get_name():
    while True:
        name = input("Enter your name, 'done' to finish 'exit' to quit : ").strip()

        if name.lower() in ('done', 'exit'):
            return name.lower()
        elif any(char.isdigit() for char in name) or name == "":
            print("Enter a valid student name.")
            continue
        else:
            return name.capitalize()

def get_subject(name):
    while True:
        subject = input(f"Enter the subject name for {name} or 'done' to stop : ").strip()

        if any(char.isdigit() for char in subject) or subject == "":
            print("Enter a valid subject name.")
            continue
        elif subject.lower() == "done":
            return 'done'
        else:
            return subject.upper()

def get_score(name, subject):
    while True:
        try :
            score = int(input(f"Enter the score of the subject {subject} for student {name}: "))
            if score < 0 or score > 100:
                print("Enter a valid score between 0 and 100.")
                continue
            return score

        except ValueError:
            print("Enter a valid score between 0 and 100.")
            continue

def get_student():
    students = {}
    while True:
        name = get_name()
        if name == 'exit' :
            print("Quitting ,Return to main menu.")
            break
        elif name == 'done':
            break

        student = Student(name)

        while True:
            subject = get_subject(name)
            if subject == 'done' :
                break
            score = get_score(name, subject)
            student.add_subject(subject, score)

        students[name] = student

    return students

