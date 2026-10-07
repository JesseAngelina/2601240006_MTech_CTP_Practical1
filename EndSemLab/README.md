

```markdown
# Merge Sort – Railway Passenger Age Analysis

## Experiment 4

### Problem Statement

An Indian railway reservation system stores the ages of passengers who booked tickets for a particular train. The system needs to arrange the ages in ascending order for statistical analysis.

The task is to implement **Merge Sort using the Divide-and-Conquer technique** and compare the number of comparisons for:

- Already Sorted Input
- Reverse Sorted Input
- Random Input

---

## AIM

To implement Merge Sort using the Divide-and-Conquer technique to sort passenger ages in ascending order and compare the number of comparisons for sorted, reverse-sorted, and random inputs.

---

## ALGORITHM

1. Start.
2. Define the `merge_sort()` function.
3. If the array contains zero or one element, return it as it is already sorted.
4. Find the middle index of the array.
5. Divide the array into two halves.
6. Recursively apply Merge Sort to both halves.
7. Compare elements from the left and right sorted halves.
8. Add the smaller element to the result array.
9. Count every element comparison.
10. Add the remaining elements after one half is completely processed.
11. Repeat the process for:
    - Already sorted input
    - Reverse sorted input
    - Random input
12. Display the sorted arrays and comparison counts.
13. Analyze the time complexity.
14. Stop.

---

## SOURCE CODE

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2

    left, c1 = merge_sort(arr[:mid])
    right, c2 = merge_sort(arr[mid:])

    result = []
    i = j = 0
    comparisons = c1 + c2

    while i < len(left) and j < len(right):
        comparisons += 1

        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result, comparisons


# Test cases
sorted_input = [10, 15, 20, 25, 30, 35, 40]
reverse_input = [40, 35, 30, 25, 20, 15, 10]
random_input = [25, 10, 40, 15, 30, 20, 35]

for name, arr in [
    ("Already Sorted", sorted_input),
    ("Reverse Sorted", reverse_input),
    ("Random", random_input)
]:
    result, comparisons = merge_sort(arr)

    print("\n", name)
    print("Input:", arr)
    print("Sorted:", result)
    print("Comparisons:", comparisons)
```

---

## INPUT

### Already Sorted

```text
[10, 15, 20, 25, 30, 35, 40]
```

### Reverse Sorted

```text
[40, 35, 30, 25, 20, 15, 10]
```

### Random

```text
[25, 10, 40, 15, 30, 20, 35]
```

---

## EXPECTED OUTPUT

```text
Already Sorted
Input: [10, 15, 20, 25, 30, 35, 40]
Sorted: [10, 15, 20, 25, 30, 35, 40]
Comparisons: 9

Reverse Sorted
Input: [40, 35, 30, 25, 20, 15, 10]
Sorted: [10, 15, 20, 25, 30, 35, 40]
Comparisons: 11

Random
Input: [25, 10, 40, 15, 30, 20, 35]
Sorted: [10, 15, 20, 25, 30, 35, 40]
Comparisons: 14
```

> Note: The exact number of comparisons depends on the input values and the implementation.

---

## COMPARISON OF INPUT CASES

| Input Type | Comparisons | Time Complexity |
|------------|-------------|-----------------|
| Already Sorted | 9 | O(n log n) |
| Reverse Sorted | 11 | O(n log n) |
| Random | 14 | O(n log n) |

The number of comparisons changes depending on the arrangement of elements, but the asymptotic time complexity remains **O(n log n)** for all cases.

---

## TIME COMPLEXITY

### Best Case

```text
O(n log n)
```

### Average Case

```text
O(n log n)
```

### Worst Case

```text
O(n log n)
```

### Space Complexity

```text
O(n)
```

---

## KEY CONCEPTS

### Divide-and-Conquer

Merge Sort follows three main steps:

```text
Divide → Conquer → Combine
```

- **Divide:** Split the array into two halves.
- **Conquer:** Recursively sort both halves.
- **Combine:** Merge the sorted halves.

### Recursion

The `merge_sort()` function calls itself to sort smaller subarrays.

### Comparison Counting

The statement:

```python
comparisons += 1
```

counts each comparison between elements of the left and right sorted arrays.

---

# VIVA QUESTIONS AND ANSWERS

### 1. What is Merge Sort?

**Answer:**  
Merge Sort is a Divide-and-Conquer sorting algorithm that divides an array into smaller parts, recursively sorts them, and merges the sorted parts.

---

### 2. Why is Merge Sort called a Divide-and-Conquer algorithm?

**Answer:**  
It divides the array into two halves, recursively sorts each half, and combines them by merging the sorted halves.

---

### 3. What is the time complexity of Merge Sort?

**Answer:**  

```text
Best Case    → O(n log n)
Average Case → O(n log n)
Worst Case   → O(n log n)
```

---

### 4. Why are the comparison counts different for sorted, reverse, and random inputs?

**Answer:**  
The number of comparisons depends on the arrangement of elements during the merging process. However, the overall time complexity remains O(n log n).

---

### 5. What is the base case in Merge Sort?

**Answer:**  
The base case is when the array contains zero or one element because it is already sorted.

---

## CONCLUSION

Merge Sort was successfully implemented using the Divide-and-Conquer technique. The passenger ages were sorted in ascending order for sorted, reverse-sorted, and random inputs. The comparison counts varied depending on the input arrangement, while the time complexity remained **O(n log n)**.
```

### 📁 GitHub file structure

Keep it simple:

```text
Merge-Sort/
│
├── Mergesort.py
└── README.md
```

Then upload both files to your GitHub repository.
