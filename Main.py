from Classes import Person, Student, Classroom
classroom = Classroom()
while True:
    try:
        obj = int(input("What would you like to do?\n"
                    "1)Add a student\n"
                    "2)Remove a student\n"
                    "3)Search a student\n"
                    "4)Add a score to a student\n"
                    "5)Show top student\n"
                    "6)List all students\n"
                    "7)Exit\n"
                    ": "))
    except ValueError:
        print("Please enter a valid number")
        continue
    if obj == 1:
        try:
            student = Student(input("Enter student name: "), int(input("Enter student age: ")), input("Enter student grade: "))
        except ValueError:
            print("It's not that hard twin.")
            continue
        classroom.add_student(student)
        print(f"{student.name} has been added to the classroom")
        continue
    elif obj == 2:
        del_student = input("Enter student name: ")
        student_to_remove = classroom.search_student(del_student)
        if student_to_remove:
            classroom.remove_student(student_to_remove)
            print(f"{student_to_remove.name} has been removed from the classroom")
            continue
        else:
            print("Bruh who is this?")
            continue
    elif obj == 3:
        name = input("Student name: ")
        classroom.search_student(name)
        continue
    elif obj == 4:
        name = input("Student to be given score: ")
        subject = input("Enter subject name: ")
        try:
            score = int(input("Enter student score: "))
        except ValueError:
            print("You dumb?")
            continue
        student_to_be_scored = classroom.search_student(name)
        if student_to_be_scored:
            student_to_be_scored.add_score(subject, score)
            continue
        else:
            print("Bruh who is this?")
            continue
    elif obj == 5:
        classroom.top_student()
        continue
    elif obj== 6:
        classroom.list_students()
        continue
    elif obj == 7:

        with open("Student_management.txt" , "a") as f:
            for student in classroom.students:
                score_str = (f"{subject}: {score}" for subject, score in student.scores.items())
                f.write(f"{student.name} who is {student.age} years old in {student.grade}\n"
                    f"{', '.join(score_str)}\n"
                    f"with average score of {student.average_score():.2f}\n")
        print("Students info saved in file!")

        break









