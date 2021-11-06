class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def lec_rate(self, courses_name):
        self.finished_courses.append(courses_name)

    def lecturer_rate(self, lecturer, course, l_grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [l_grade]
            else:
                lecturer.grades[course] = [l_grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'''
        Имя: {self.name} 
        Фамилия: {self.surname} 
        Средняя оценка за домашние задания: {self.rating()} 
        Курсы в процессе изучения: {",".join(self.courses_in_progress)} 
        Завершенные курсы: Введение в програмирование'''

    def rating(self):
        rat_list = list(self.grades.items())
        for skore in rat_list:
            grade = 0
            for key, value in rat_list:
                grade += sum(value) / len(value)
                grade = round(grade / len(rat_list), 1)
                return grade

    def __gt__(self, other):
        if not isinstance(other, Student):
            return f'''{self.name}{self.surname} 
         Средний балл выше, чем у {other.name}{other.surname}'''
        else:
            return f'''{self.name}{self.surname} Средний балл ниже, чем у {other.name}{other.surname}'''


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rating(self):
        rat_list = list(self.grades.items())
        for skore in rat_list:
            grade = 0
            for key, value in rat_list:
                grade += sum(value) / len(value)
                grade = round(grade / len(rat_list), 1)
            return grade


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def __str__(self):
        return f'''
             Имя: {self.name}  
             Фамилия: {self.surname} 
             Средняя оценка лекции: {self.rating()}'''

    def __gt__(self, other):
        if not isinstance(other, Student):
            return f'{self.name}{self.surname} Средний балл выше , чем у {other.name}{other.surname}'
        else:
            return f'{self.name}{self.surname} Средний балл ниже , чем у {other.name}{other.surname}'


class Reviewer(Lecturer):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def __str__(self):
        return f'''
         Имя: {self.name} 
         Фамилия: {self.surname}'''


student1 = Student('Boni', ' Grenn', 'girl')
student2 = Student('Roy', ' Grey', 'boy')
student1.courses_in_progress += ['Python', 'Git']
student2.courses_in_progress += ['Python']
cool_mentor = Mentor('Bill', ' Joseph')
cool_mentor.courses_attached += ['Python']
cool_reviewer = Reviewer('Some', ' Buddy')
cool_reviewer1 = Reviewer('Molli', ' Robin')
cool_reviewer.courses_attached += ['Python']
cool_lecturer = Lecturer('Deni', ' Salli')
cool_lecturer.courses_attached += ['Python', 'Git']
cool_lecturer1 = Lecturer('Jeni', ' Brith')
cool_lecturer1.courses_attached += ['Python']
student1.lecturer_rate(cool_lecturer, 'Python', 10)
student2.lecturer_rate(cool_lecturer, 'Python', 9)
student1.lecturer_rate(cool_lecturer, 'Python', 10)
student1.lecturer_rate(cool_lecturer1, 'Python', 10)
student2.lecturer_rate(cool_lecturer1, 'Python', 8)
student2.lecturer_rate(cool_lecturer1, 'Python', 9)
cool_reviewer1.rate_hw(student1, 'Python', 8)
cool_reviewer1.rate_hw(student1, 'Python', 8)
cool_reviewer1.rate_hw(student1, 'Python', 10)
cool_reviewer1.rate_hw(student2, 'Python', 6)
cool_reviewer1.rate_hw(student2, 'Python', 8)
cool_reviewer.rate_hw(student2, 'Python', 10)

print(student1)
print(cool_lecturer)
print()
print(cool_lecturer1)
print()
print(student1)
print()
print(student2)
print()
print(student2 > student1)
print()
print(cool_lecturer > cool_lecturer1)
print()
print(cool_lecturer1 > cool_reviewer)
print()
print(cool_lecturer.courses_attached)
print()

list_student = [student1, student2]
list_lecturer = [cool_lecturer, cool_lecturer1]


def avg_grades(student, subj):
    count = 0
    number = 0
    for i in student:
        for k, v in i.grades.items():
            count += sum(v)
            number += len(v)
    all = count / number
    return f"{all:.1f}"


print(avg_grades(list_student, 'Python'))


def avg_grades_lec(lecturer, subj):
    count = 0
    number = 0
    for i in lecturer:
        for k, v in i.grades.items():
            count += sum(v)
            number += len(v)
    all = count / number
    return f"{all:.1f}"


print(avg_grades_lec(list_lecturer, 'Git'))


