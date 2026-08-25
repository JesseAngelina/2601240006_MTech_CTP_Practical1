# Student Attendance System

## 1. Objective

To develop a Python-based attendance analysis system that calculates the attendance percentage of multiple students and generates an attendance report.

## 2. Input

The program accepts:

* Number of students
* Student name
* Number of classes attended
* Total number of classes conducted

## 3. Output

The program displays:

* Attendance percentage of each student
* Attendance status

  * Below 75%
  * Eligible
* Student with the highest attendance
* Class average attendance
* List of students whose attendance is below 75%

## 4. Algorithm

1. Start.
2. Create an empty list to store student details.
3. Read the number of students.
4. For each student:

   * Read the student's name.
   * Read the number of classes attended.
   * Read the total number of classes conducted.
   * Calculate the attendance percentage using:
     **Attendance Percentage = (Classes Attended / Total Classes Conducted) × 100**
   * Store the student details and calculated percentage in the list.
5. Display the attendance percentage and status of each student.
6. Find the student with the highest attendance by comparing the attendance percentages.
7. Calculate the class average attendance by adding all attendance percentages and dividing by the number of students.
8. Display the highest attendance and class average.
9. Check each student's attendance percentage.
10. Display the students whose attendance is below 75%.
11. If no student has attendance below 75%, display an appropriate message.
12. Stop.

## 5. Time Complexity

**O(n)**

Where `n` is the number of students.

The program performs several separate loops over the list of students. Since these loops run sequentially, the overall time complexity remains **O(n)**.
