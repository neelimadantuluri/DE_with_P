def get_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

print("Welcome to the Simple Grading System!")

num_students = int(input("How many students are there? "))

for i in range(num_students):
    print("\nStudent", i + 1)
    name = input("Enter the student's name: ")
    score = float(input("Enter the student's score (0 - 100): "))
    grade = get_grade(score)

    print("Name:", name)
    print("Score:", score)
    print("Grade:", grade)
    print("----------------------")


