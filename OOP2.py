class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.course_grades:
                lecturer.course_grades[course] += [grade]
            else:
                lecturer.course_grades[course] = [grade]
        else:
            return 'Ошибка'

    def __counting_grades(self):
        mid_grades_py = sum(self.grades['Python']) / len(self.grades['Python'])
        mid_grades_git = sum(self.grades['Git']) / len(self.grades['Git'])
        grades_py_git = (mid_grades_py + mid_grades_git) / len(self.grades)
        return round(grades_py_git, 1)


    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student')
            return
        return student1.__counting_grades() > student2.__counting_grades()

    def __str__(self):
        some_student = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание: ' \
                       f'{self.__counting_grades()}\n' \
                       f'Курсы в процессе изучения: {",".join(self.courses_in_progress)}\nЗавершенные курсы: ' \
                       f'{" ".join(self.finished_courses)}'
        return some_student


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.course_grades = {}

    def __calculation_grades(self):
        middle_grades_py = sum(self.course_grades['Python']) / len(self.course_grades['Python'])
        middle_grades_git = sum(self.course_grades['Git']) / len(self.course_grades['Git'])
        middle_grades_py_git = (middle_grades_py + middle_grades_git) / len(self.course_grades)
        return round(middle_grades_py_git, 1)

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer')
            return
        return lecturer1.__calculation_grades() < lecturer2.__calculation_grades()

    def __str__(self):
        self.some_lecturer = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: ' \
                             f'{self.__calculation_grades()}'
        return self.some_lecturer


class Reviewer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        self.some_reviewer = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        return self.some_reviewer

student1 = Student('Анна', 'Ветрова')
student1.courses_in_progress += ['Python', 'Git']
student1.finished_courses += ['Files']

student2 = Student('Виталий', 'Иванов')
student2.courses_in_progress += ['Python', 'Git']
student2.finished_courses += ['Files']

lecturer1 = Lecturer('Алексей', 'Петров')
lecturer1.courses_attached += ['Python', 'Git']

lecturer2 = Lecturer('Ирина', 'Швецова')
lecturer2.courses_attached += ['Python', 'Git']

student1.rate_lecturer(lecturer1, 'Python', 10)
student1.rate_lecturer(lecturer1, 'Python', 8)
student1.rate_lecturer(lecturer1, 'Python', 9)
student1.rate_lecturer(lecturer1, 'Git', 8)
student1.rate_lecturer(lecturer1, 'Git', 7)
student1.rate_lecturer(lecturer1, 'Git', 9)

student2.rate_lecturer(lecturer2, 'Python', 8)
student2.rate_lecturer(lecturer2, 'Python', 7)
student2.rate_lecturer(lecturer2, 'Python', 5)
student2.rate_lecturer(lecturer2, 'Git', 9)
student2.rate_lecturer(lecturer2, 'Git', 7)
student2.rate_lecturer(lecturer2, 'Git', 7)

some_reviewer = Reviewer('Вадим', 'Свечкин')
some_reviewer.courses_attached += ['Python', 'Git']

reviewer2 = Reviewer('Сергей', 'Иващенко')
reviewer2.courses_attached += ['Python', 'Git']

some_reviewer.rate_hw(student1, 'Python', 7)
some_reviewer.rate_hw(student1, 'Python', 9)
some_reviewer.rate_hw(student1, 'Python', 10)
some_reviewer.rate_hw(student1, 'Git', 10)
some_reviewer.rate_hw(student1, 'Git', 7)
some_reviewer.rate_hw(student1, 'Git', 10)

some_reviewer.rate_hw(student2, 'Python', 5)
some_reviewer.rate_hw(student2, 'Python', 9)
some_reviewer.rate_hw(student2, 'Python', 10)
some_reviewer.rate_hw(student2, 'Git', 9)
some_reviewer.rate_hw(student2, 'Git', 9)
some_reviewer.rate_hw(student2, 'Git', 9)

all_student = [student1, student2]
all_lecturer = [lecturer1, lecturer2]

def counter_average_grades(student, course):
        grade_lst = []
        for student in all_student:
            if course in student.grades:
                grade_lst += student.grades[course]
            else:
                return 'Ошибка'
            result_grades = sum(grade_lst) / len(grade_lst)
        return round(result_grades, 1)

def calculation_average(lecturer, course):
        lst_grade = []
        for lecturer in all_lecturer:
            if course in lecturer.course_grades:
                lst_grade += lecturer.course_grades[course]
            else:
                return 'Commit mistake'
            result = sum(lst_grade) / len(lst_grade)
        return round(result, 1)

print('Student:')
print(student1.__str__())
print(student2.__str__())
print('Lecturer:')
print(lecturer1.__str__())
print(lecturer2.__str__())
print('Reviewer:')
print(some_reviewer.__str__())
print(reviewer2.__str__())
print(f'Средняя оценка   Анна Ветрова больше чем у  Виталий Иванов ?: {student1.__lt__(student2)}')
print(f'Средняя оценка у лектора Алексей Петров меньше чем у Ирина Швецова ?: {lecturer1.__lt__(lecturer2)}')
print(f"Средний бал среди студентов по курсу Python: {counter_average_grades(all_student, 'Python')}")
print(f"Средний бал среди студентов по курсу Git: {counter_average_grades(all_student, 'Git')}")
print(f"Средний бал среди лекторов за лекцию  Python: {calculation_average(all_lecturer, 'Python')}")
print(f"Средний бал среди лекторов за лекцию  Git: {calculation_average(all_lecturer, 'Git')}")