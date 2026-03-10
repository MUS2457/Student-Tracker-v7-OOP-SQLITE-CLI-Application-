
class Student :
    def __init__(self, name):
        self.name = name
        self.subjects = {}

    def add_subject(self, subject, score):
        self.subjects[subject] = score

    @classmethod
    def students_averages(cls, students):
        averages = {}
        if not students:
            return averages
        for name, obj in students.items():
            averages[name] = round(sum(obj.subjects.values()) / len(obj.subjects), 2) if obj.subjects else 0
        return averages

    @classmethod
    def from_dict(cls, data):   # for practice not used

        students = {}

        for date,names in data.items():
            for name, subjects in names.items():
                student = cls(name)
                for subject, score in subjects.items():
                    student.add_subject(subject, score)

                students[name] = student

        return students
