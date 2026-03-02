class Student :
    def __init__(self, name):
        self.name = name
        self.subjects = {}

    def add_subject(self, subject, score):
        self.subjects[subject] = score
