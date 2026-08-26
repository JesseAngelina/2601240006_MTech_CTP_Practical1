# Binary Search – Book Search

## 1. Objective

To implement the Binary Search algorithm to efficiently search for a particular book in a sorted list of books.

The program checks whether the target book exists and displays its index and position if it is found.

## 2. Input

The program uses:

* A sorted list of book numbers from `1` to `1,000,000`
* Target book number: `75000`

## 3. Output

If the target book is found, the program displays:

* `Book exists`
* Index of the book
* Position of the book

If the book is not found, the program displays:

* `Book does not exist`

### Sample Output

```text
Book exists
Index = 74999
Position = 75000
```

## 4. Algorithm

1. Start.
2. Create a sorted list of book numbers.
3. Set `low` to the first index of the list.
4. Set `high` to the last index of the list.
5. Repeat while `low` is less than or equal to `high`:

   * Calculate the middle index using:
     `mid = (low + high) // 2`
   * Compare the middle element with the target value.
   * If the middle element is equal to the target, return its index.
   * If the middle element is smaller than the target, search the right half by setting:
     `low = mid + 1`
   * Otherwise, search the left half by setting:
     `high = mid - 1`
6. If the target is not found, return `-1`.
7. Check the returned index.
8. If the index is not `-1`, display that the book exists along with its index and position.
9. Otherwise, display that the book does not exist.
10. Stop.

## 5. Time Complexity

**Best Case: O(1)**

The target element is found at the middle of the list during the first comparison.

**Average Case: O(log n)**

The search space is divided into half after every comparison.

**Worst Case: O(log n)**

The algorithm continues dividing the search space until the element is found or the search space becomes empty.

For `n = 1,000,000`, Binary Search requires only approximately `log₂(1,000,000)` comparisons, which is about **20 comparisons** in the worst case.

## 6. Space Complexity

**O(1)**

The iterative implementation uses only a fixed number of variables such as `low`, `high`, `mid`, and `target`.
