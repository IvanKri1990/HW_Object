class Student:
    def __init__(self, name, surname, grades):
        self.name = name
        self.surname = surname
        self.courses_in_progress = []
        self.courses_finished = []
        self.grades = grades

    def __str__(self):
        return f'''Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашнее задание: {self.grades}
Курсы в процессе изучение: {self.courses_in_progress} \nЗавершенный курсы: {self.courses_finished}'''

    def __eq__(self, grade):
        return self.grades == grade.grades


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname}"


class Lecturer(Mentor):
    def __init__(self, name, surname, grades):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = grades

    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.grades}"


some_reviewer = Reviewer("Some", "Buddy")
print(some_reviewer)

some_lecturer = Lecturer("Some", "Buddy", 9.9)
print(some_lecturer)

some_student = Student("Ruoy", "Eman", 9.9)
some_student.courses_in_progress += ["Python", "Git"]
some_student.courses_finished += ["Введение в программирование"]
print(some_student)

student = Student("Ruoy", "Eman", 9.9)
lector = Lecturer("Some", "Buddy", 9.9)
if student == lector:
    print("Средняя оценка одинаковая")
else:
    print("Оценки не равны")