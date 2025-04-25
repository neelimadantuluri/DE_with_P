# def get_grade(score):
#     if score >= 90:
#         return 'A'
#     elif score >= 80:
#         return 'B'
#     elif score >= 70:
#         return 'C'
#     elif score >= 60:
#         return 'D'
#     else:
#         return 'F'
#
# print("Welcome to the Simple Grading System!")
#
# num_students = int(input("How many students are there? "))
#
# for i in range(num_students):
#     print("\nStudent", i + 1)
#     name = input("Enter the student's name: ")
#     score = float(input("Enter the student's score (0 - 100): "))
#     grade = get_grade(score)
#
#     print("Name:", name)
#     print("Score:", score)
#     print("Grade:", grade)
#     print("----------------------")


# print("Welcome to the Simple Grading System!")
#
# num_students = int(input("How many students are there? "))
#
# student_list = []
#
# for i in range(num_students):
#     print("\nStudent", i + 1)
#
#     name = input("Enter the student's name: ")
#     score = float(input("Enter the student's score (0 - 100): "))
#
#     if score >= 90:
#         grade = 'A'
#     elif score >= 80:
#         grade = 'B'
#     elif score >= 70:
#         grade = 'C'
#     elif score >= 60:
#         grade = 'D'
#     else:
#         grade = 'F'
#
#     student_info = {
#         "name": name,
#         "score": score,
#         "grade": grade
#     }
#
#     student_list.append(student_info)
#
# print("\n--- Class Results ---")
# for student in student_list:
#     print("Name:", student["name"])
#     print("Score:", student["score"])
#     print("Grade:", student["grade"])
#     print("----------------------")

#OR

# print("Welcome to the Simple Grading System!")
#
# num_students = int(input("How many students are there? "))
#
# for i in range(num_students):
#     print("\nStudent", i + 1)
#     name = input("Enter the student's name: ")
#     score = float(input("Enter the student's score (0 - 100): "))
#
#     if score >= 90:
#         grade = 'A'
#     elif score >= 80:
#         grade = 'B'
#     elif score >= 70:
#         grade = 'C'
#     elif score >= 60:
#         grade = 'D'
#     else:
#         grade = 'F'
#
#     print("Name:", name)
#     print("Score:", score)
#     print("Grade:", grade)
#     print("----------------------")


