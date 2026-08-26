# README – Closest Pair of Coins

## 1. Project Title

**Closest Pair of Coins using Brute Force**

## 2. Description

This Python program finds the **two closest coins** among a set of coins placed on a 2D coordinate plane.

Each coin is represented using its **x-coordinate and y-coordinate**. The program calculates the distance between every possible pair of coins and identifies the pair having the **minimum distance**.

## 3. Objective

The main objectives of this program are:

* Accept the number of coins from the user.
* Store the `(x, y)` coordinates of each coin.
* Calculate the distance between pairs of coins.
* Find the pair with the smallest distance.
* Display the closest pair and their minimum distance.

## 4. Algorithm Used

**Brute Force Algorithm**

The program compares **every possible pair of coins**.

For each pair:

1. Calculate the distance between the two coins.
2. Compare it with the current minimum distance.
3. If the new distance is smaller, update the minimum distance.
4. Store that pair of coins.
5. Continue until all pairs have been checked.

## 5. Distance Formula

The program uses the **Euclidean distance formula**:

```text
Distance = √((x₂ - x₁)² + (y₂ - y₁)²)
```

In the program:

```python
dx = coin1[0] - coin2[0]
dy = coin1[1] - coin2[1]

return math.sqrt(dx * dx + dy * dy)
```

## 6. Input

The program takes:

* Number of coins
* X-coordinate
* Y-coordinate

Example:

```text
Enter number of coins: 4

Enter coordinates for coin 1 (x y): 1 2
Enter coordinates for coin 2 (x y): 5 6
Enter coordinates for coin 3 (x y): 2 3
Enter coordinates for coin 4 (x y): 10 10
```

## 7. Output

```text
--- RESULT ---

Coin 1: (1, 2)
Coin 2: (2, 3)
Minimum distance: 1.41 units
```

## 8. Main Functions

### `distance()`

```python
def distance(coin1, coin2):
```

Calculates the Euclidean distance between two coins.

### `closest_pair()`

```python
def closest_pair(coins):
```

Checks every possible pair of coins and finds the pair with the minimum distance.

### `main()`

```python
def main():
```

Handles:

* User input
* Storing coordinates
* Calling the closest-pair function
* Displaying the result

## 9. Data Structure

A **list of tuples** is used to store the coordinates.

Example:

```python
coins = [
    (1, 2),
    (5, 6),
    (2, 3)
]
```

Each tuple represents one coin:

```text
(x, y)
```



## 10. Time Complexity

The program uses two nested loops:

```python
for i in range(len(coins)):
    for j in range(i + 1, len(coins)):
```

Therefore:

* **Time Complexity:** `O(n²)`
* **Space Complexity:** `O(n)`

This approach is called **Brute Force** because it checks every possible pair.


## 11. Conclusion

This program demonstrates how the **Brute Force approach** can be used to solve the Closest Pair problem. It calculates the distance between every pair of coins and identifies the two coins that are closest to each other.
