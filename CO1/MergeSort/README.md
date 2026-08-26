# Student Sorting and Scholarship Eligibility

## 1. Objective

To sort students in descending order based on their marks and identify students who are eligible for a scholarship with marks greater than or equal to 90.

## 2. Input

The program uses two lists:

* **Names:** `Anitha, Vivek, Lakshmi, Ramesh, Kumar`
* **Marks:** `95, 83, 67, 97, 85`

Each student's name corresponds to their marks at the same index.

## 3. Output

The program displays:

* Students arranged in descending order of marks.
* Students eligible for the scholarship.
* A student is eligible for the scholarship if their marks are **90 or above**.

### Sample Output

```text
Students in descending order:
Ramesh - 97
Anitha - 95
Kumar - 85
Vivek - 83
Lakshmi - 67

Students eligible for scholarship:
Ramesh - 97
Anitha - 95
```

## 4. Algorithm

1. Start.
2. Create a list containing student names.
3. Create a corresponding list containing student marks.
4. Compare each student's marks with the marks of the students that follow.
5. If the current student's marks are less than the next student's marks:

   * Swap the two marks.
   * Swap the corresponding student names so that the names remain associated with their marks.
6. Repeat the comparison and swapping process until all students are arranged in descending order of marks.
7. Display the sorted list of students and their marks.
8. Traverse the sorted marks.
9. Check whether each student's marks are greater than or equal to 90.
10. If the marks are 90 or above, display the student as eligible for the scholarship.
11. Stop.

## 5. Time Complexity

**O(n²)**

The sorting algorithm uses two nested loops to compare the marks of students.

* Outer loop: **O(n)**
* Inner loop: **O(n)**
* Overall sorting complexity: **O(n²)**

The scholarship eligibility check takes **O(n)**.

Therefore, the overall time complexity is:

**O(n²)**

## 6. Space Complexity

**O(1)**

The sorting is performed in-place by swapping elements in the existing `names` and `marks` lists. No additional data structure proportional to the input size is created.
