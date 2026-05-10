class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade
        self.scores = {}
    def add_score(self, subject, score):
        self.scores[subject] = score
        print(f"{self.name}'s new score is {self.scores}")
        return self.scores
    def average_score(self):
        if len(self.scores) == 0:
            return 0
        average = sum(list(self.scores.values())) / len(self.scores)
        return average
    def info(self):
        for subject, score in self.scores.items():
            print(f"{subject} : {score}")
        print(f"{self.name} is {self.age} years old in {self.grade} and has an average score of {self.average_score():.2f}")
class Classroom:
    def __init__(self):
        self.students = []
    def add_student(self, student):
        self.students.append(student)
    def remove_student(self, student):
        self.students.remove(student)
    def list_students(self):
        for i, student in enumerate(self.students, start=1):
            print(f"{i} - {student.name} is {student.age} years old in {student.grade}")
    def search_student(self, name):
        for student in self.students:
            if name.lower() == student.name.lower():
                print(f"{student.name} is {student.age} years old in {student.grade} grade")
                return student
    def top_student(self):
        if not self.students:
            print("No student found")
            return None
        top_student = max(self.students, key = lambda s: s.average_score())
        print(f"{top_student.name} is the top student with average score of {top_student.average_score():.2f}")
        return top_student



