def sort_students(names, marks):
    for i in range(len(marks)):
        for j in range(i + 1, len(marks)):
            if marks[i] < marks[j]:
                # Swap marks
                marks[i], marks[j] = marks[j], marks[i]

                # Swap names
                names[i], names[j] = names[j], names[i]


# Input
names = ["Anitha", "Vivek", "Lakshmi", "Ramesh", "Kumar"]
marks = [95, 83, 67, 97, 85]

# Sort students
sort_students(names, marks)

# Output
print("Students in descending order:")

for i in range(len(names)):
    print(names[i], "-", marks[i])

print("\nStudents eligible for scholarship:")

for i in range(len(names)):
    if marks[i] >= 90:
        print(names[i], "-", marks[i])