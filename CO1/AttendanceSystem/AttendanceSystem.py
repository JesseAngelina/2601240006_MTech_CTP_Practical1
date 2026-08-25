students = []

n = int(input("Enter number of students: "))

for i in range(n):

    name = input("\nEnter student name: ")
    attended = int(input("Enter classes attended: "))
    conducted = int(input("Enter total classes conducted: "))

    percentage = (attended / conducted) * 100

    students.append([name, attended, conducted, percentage])


print("\n--- ATTENDANCE REPORT ---")

# Display attendance of all students
for student in students:

    print("Name:", student[0])
    print("Attendance:", student[3], "%")

    if student[3] < 75:
        print("Status: Below 75%")
    else:
        print("Status: Eligible")

    print()


# Find highest attendance
highest = students[0]

for student in students:

    if student[3] > highest[3]:
        highest = student


# Calculate class average
total_percentage = 0

for student in students:
    total_percentage = total_percentage + student[3]

average = total_percentage / n


print("--- SUMMARY ---")
print("Highest Attendance:", highest[0], "-", highest[3], "%")
print("Class Average Attendance:", average, "%")


print("\nStudents below 75%:")

found = False

for student in students:

    if student[3] < 75:
        print(student[0], "-", student[3], "%")
        found = True

if found == False:
    print("No student is below 75%.")