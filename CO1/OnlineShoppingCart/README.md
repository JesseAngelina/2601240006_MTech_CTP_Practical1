# Online Shopping Cart System

## 1. Objective

To develop a Python-based online shopping cart system that allows users to add and remove products, change product quantities, apply discounts, and calculate the final bill including GST.

## 2. Algorithm

1. Start.
2. Create an empty shopping cart and initialize the discount to zero.
3. Display the shopping cart menu.
4. Read the user's choice.
5. If the choice is **1 (Add Product)**:

   * Read the product name, price, and quantity.
   * Add the product details to the cart.
6. If the choice is **2 (Remove Product)**:

   * Read the product name.
   * Search for the product in the cart.
   * If found, remove it.
   * Otherwise, display "Product not found."
7. If the choice is **3 (Change Quantity)**:

   * Read the product name and new quantity.
   * Search for the product in the cart.
   * If found, update its quantity.
   * Otherwise, display "Product not found."
8. If the choice is **4 (Apply Discount)**:

   * Read the discount percentage.
   * Store the discount value.
9. If the choice is **5 (Display Bill)**:

   * Initialize the subtotal to zero.
   * Traverse all products in the cart.
   * Calculate the total price for each product.
   * Add each product total to the subtotal.
   * Calculate the discount amount.
   * Calculate the amount after discount.
   * Calculate 18% GST.
   * Calculate and display the final bill.
10. If the choice is **6 (Exit)**:

    * Display the thank-you message.
    * Terminate the program.
11. For any other choice, display "Invalid choice."
12. Repeat the menu until the user chooses Exit.
13. Stop.

## 3. Input

The program accepts the following inputs:

* User's menu choice
* Product name
* Product price
* Product quantity
* Discount percentage

## 4. Output

The program displays:

* Product added or removed from the cart
* Updated product quantity
* Applied discount
* Product-wise bill details
* Subtotal
* Discount amount
* Amount after discount
* GST at 18%
* Final bill amount
* Appropriate messages for invalid choices or unavailable products

  
## 5. Time Complexity

**O(n)**

Where `n` is the number of products in the shopping cart.

* **Add Product:** O(1)
* **Remove Product:** O(n)
* **Change Quantity:** O(n)
* **Apply Discount:** O(1)
* **Display Bill:** O(n)
* **Exit:** O(1)

The overall time complexity for a single menu operation is **O(n)** in the worst case because removing, changing quantity, and displaying the bill may require traversing the cart.

The cart stores the details of `n` products.
