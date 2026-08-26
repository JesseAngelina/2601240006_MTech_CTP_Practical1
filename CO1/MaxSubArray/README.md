# README – Maximum Profit Streak

## 1. Project Title

**Maximum Profit Streak using Kadane's Algorithm**

## 2. Description

This Python program finds the **continuous period of days with the maximum total profit** from a series of daily profit or loss changes.

Each day can have:

* A positive value → profit
* A negative value → loss

The program identifies the best continuous period and displays the maximum profit obtained during that period.

## 3. Objective

The main objectives are:

* Accept the number of days.
* Store daily profit/loss changes.
* Find the continuous period with the highest total profit.
* Display the starting and ending days.
* Display the maximum profit.
* Display the daily changes in the best period.

## 4. Algorithm Used

**Kadane's Algorithm**

The algorithm works by maintaining:

* `current_sum` → maximum sum ending at the current position.
* `best_sum` → maximum sum found so far.

For every value, the program decides whether to:

1. Start a new subarray from the current day, or
2. Continue the existing subarray.

The program also keeps track of the starting and ending days of the maximum-profit period.

## 5. Example

Suppose the daily changes are:

```text
-2  3  -1  5  -6  4
```

The maximum-profit continuous period is:

```text
3  -1  5
```

Therefore:

```text
Maximum profit = 7
```

## 6. Input

The program takes:

* Number of days
* Profit/loss for each day

Example:

```text
Enter number of days: 6

Enter profit/loss for day 1: -2
Enter profit/loss for day 2: 3
Enter profit/loss for day 3: -1
Enter profit/loss for day 4: 5
Enter profit/loss for day 5: -6
Enter profit/loss for day 6: 4
```

## 7. Output

```text
--- RESULT ---
Best period: Day 2 to Day 4
Maximum profit: Rs.7.00

Daily changes in best period:
3 -1 5
```

## 8. Main Functions

### `maximum_subarray()`

```python
def maximum_subarray(changes):
```

Finds the continuous sequence with the maximum sum using Kadane's Algorithm.

It returns:

* Maximum profit
* Starting index
* Ending index

### `main()`

```python
def main():
```

Handles:

* User input
* Storing daily changes
* Calling the maximum subarray function
* Displaying the final result

## 9. Data Structure

A **list** is used to store the daily profit/loss values.

Example:

```python
changes = [-2, 3, -1, 5, -6, 4]
```

## 10. Validation

The program checks that the number of days is greater than zero:

```python
if n <= 0:
    print("Number of days must be greater than zero.")
    return
```

## 11. Time Complexity

Kadane's Algorithm processes the list only once.

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(n)` for storing the input list.

The algorithm itself uses **O(1)** extra space apart from the input list.

## 12. How to Run

Open the Python file in VS Code and run:

```text
python MaximumProfitStreak.py
```

Enter the number of days and the daily profit/loss values.

## 13. Conclusion

This program demonstrates the use of **Kadane's Algorithm** to efficiently find the continuous period with the maximum total profit. It is more efficient than checking every possible subarray because it solves the problem in **O(n)** time.
