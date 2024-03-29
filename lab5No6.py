assignment = float(input("Assignment and Seatwork: "))/100 * 100

quiz = float(input("Quiz: ")) 

if quiz > 30:
    print("score must not exceed 30")
else:
    quiz = quiz / 30 * 100


    labExercise = float(input("Laboratory Exercises: ")) /100 * 100

    exam = float(input("Exam: "))

    if exam > 50:
        print("score must not exceed 50")
    else:
        exam = exam / 50 * 100



        grade = (assignment + quiz + labExercise + exam) /400 * 100
        print("\nAssignment: ",assignment)
        print("quiz: ",quiz)
        print("Laboratory Exercises: ",labExercise)
        print("Exams: ",exam)

        print("\nYour grade is: ",grade)

        if grade >= 75:
            print("\nPassed")
        elif grade > 100:
            print("grade must not be more than 100")
        else:
            print("\nFailed")
    

    