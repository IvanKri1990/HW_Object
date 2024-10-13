class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def getGrade(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in self.courses_attached:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, stud, course, grade):
        if isinstance(stud, Student) and course in self.courses_attached and course in stud.courses_in_progress:
            if course in stud.grades:
                stud.grades[course] += [grade]
            else:
                stud.grades[course] = [grade]
        else:
            return 'Ошибка'


best_student = Student('Roy', 'Eman', 'man')
best_student.courses_in_progress += ['Python']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

print(best_student.grades)

best_student = Student('Ish', 'Va', 'men')
best_student.courses_in_progress += ['Git']

best_lector = Lecturer('Ivan', 'Ivanov')
best_lector.courses_attached += ['Git', 'Python']

best_lector.getGrade(best_lector, 'Git', 9)
best_lector.getGrade(best_lector, 'Git', 7)
best_lector.getGrade(best_lector, 'Git', 10)

print(best_lector.grades)