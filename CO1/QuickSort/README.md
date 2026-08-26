# Product Price Sorting System Using Quick Sort

## 1. Objective

To develop a Python-based product price sorting system using the Quick Sort algorithm. The program sorts products according to their prices in ascending order while maintaining the association between each product and its price.

## 2. Real-World Application

Online shopping platforms often allow customers to sort products based on price. Quick Sort can be used to efficiently arrange products from the lowest price to the highest price.

## 3. Input

The program uses a list containing:

* Product name
* Product price

Example:

* Laptop - 55000
* Mobile Phone - 25000
* Headphones - 3000
* Smart Watch - 7000
* Tablet - 18000

## 4. Output

The program displays the products in ascending order of price.

### Sample Output

```text
Products sorted by price:
Headphones - 3000
Smart Watch - 7000
Tablet - 18000
Mobile Phone - 25000
Laptop - 55000
```

## 5. Algorithm

1. Start.
2. Create a list containing product names and their corresponding prices.
3. Call the Quick Sort function with the first and last indexes of the list.
4. Select the last element as the pivot.
5. Initialize the partition index.
6. Compare each product price with the pivot price.
7. If the product price is less than or equal to the pivot:

   * Move the product to the appropriate position.
   * Swap the complete product records so that the product name remains associated with its price.
8. Place the pivot in its correct sorted position.
9. Recursively apply Quick Sort to the elements on the left side of the pivot.
10. Recursively apply Quick Sort to the elements on the right side of the pivot.
11. Continue until the subarray contains zero or one element.
12. Display the products in ascending order of price.
13. Stop.

## 6. Time Complexity

### Best Case: O(n log n)

The pivot divides the array into two approximately equal parts at each step.

### Average Case: O(n log n)

On average, Quick Sort divides the data reasonably well.

### Worst Case: O(n²)

The worst case occurs when the selected pivot produces highly unbalanced partitions, such as when the data is already sorted and the last element is consistently selected as the pivot.

Therefore:

* Best Case: **O(n log n)**
* Average Case: **O(n log n)**
* Worst Case: **O(n²)**

## 7. Space Complexity

**O(log n)** on average due to the recursive function calls.

In the worst case, the recursion depth can become **O(n)** when the partitions are highly unbalanced.

## 8. Conclusion

The Quick Sort algorithm successfully sorts the products based on their prices while preserving the relationship between product names and prices. It provides efficient average-case performance and can be useful for sorting products in online shopping applications.
