#2) Студент (свойства: имя-фамилия, специальность, год начала обучения, список оценок – при создании объекта, по умолчанию, пустой список).
#Методы:
#3.	Добавить новую оценку в свойство списка оценок
#4.	Посчитать средний балл,
#5.	Посчитать сколько лет учится уже студент.
import datetime


class Student:
    """Student description..."""

    def __init__(self, name_surname, speciality, year, marks=None):
        if marks is None:
            marks = []
        self.name_surname = name_surname
        self.speciality = speciality
        self.year = year
        self.marks = marks

    def add_mark(self, new_mark):
        """Method add mark for student"""
        self.marks.append(new_mark)

    def average_score(self):
        """Method returns how many years the student has been studying"""
        return sum(self.marks) / len(self.marks)

    def study_experience(self):
        """Method return average score ball for student"""
        return datetime.datetime.now().year - self.year

    def __str__(self):
        return f"Student object "


s = Student(name_surname="tester", speciality="qa", year=2013)
#print(s)
s.add_mark(5)
s.add_mark(7)
print(s.marks)
print(s.average_score())
print(s.study_experience())

