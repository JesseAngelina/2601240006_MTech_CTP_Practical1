# Q7 — Composition: E-Commerce Order

````markdown
# Q7 — Composition: E-Commerce Order

## Definition

**Composition** is an Object-Oriented Programming (OOP) concept that represents a **"has-a" relationship** between classes.

In composition, one class contains objects of other classes as its attributes or members. It allows complex objects to be built using smaller, independent objects.

---

## Problem Statement

An e-commerce system contains an **Order** that consists of multiple **Product** objects. The order also contains a **Payment** object.

Apply **composition** to model the system using a **has-a relationship**.

---

## Objective

To demonstrate the use of **composition** by creating an `Order` class that contains multiple `Product` objects and a `Payment` object.

---

## Concept

In this program:

- `Order` contains multiple `Product` objects.
- `Order` contains a `Payment` object.
- Products and payment are separate classes.
- The `Order` class combines these objects to represent a complete order.

### Class Relationship

```text
                    Order
                   /     \
                  /       \
                 ↓         ↓
           Products      Payment
              |
       ┌──────┼──────┐
       ↓      ↓      ↓
    Product Product Product
````

This represents a **"has-a" relationship**:

```text
Order has Products
Order has Payment
```

---

## Advantages of Composition

* Promotes code reusability.
* Creates a clear relationship between objects.
* Makes complex systems easier to design.
* Allows individual classes to be developed independently.
* Improves flexibility and maintainability.

---

## Implementation

The system contains three classes:

### 1. Product

Stores:

* Product ID
* Product name
* Product price

### 2. Payment

Stores:

* Payment mode
* Payment amount

### 3. Order

Stores:

* Order ID
* Multiple products
* Payment details

The `Order` class uses objects of `Product` and `Payment`, demonstrating composition.

---

## Python Program

```python
class Product:

    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def display_product(self):
        print("Product ID:", self.product_id)
        print("Name:", self.name)
        print("Price:", self.price)


class Payment:

    def __init__(self, payment_mode, amount):
        self.payment_mode = payment_mode
        self.amount = amount

    def payment_method(self):
        print("Payment Mode:", self.payment_mode)
        print("Amount:", self.amount)


class Order:

    def __init__(self, order_id):
        self.order_id = order_id
        self.products = []
        self.payment = None

    def add_product(self, product):
        self.products.append(product)

    def set_payment(self, payment):
        self.payment = payment

    def display_order(self):
        print("Order ID:", self.order_id)
        print("Products:")

        total = 0

        for product in self.products:
            product.display_product()
            total += product.price

        print("Total Amount:", total)

        if self.payment:
            print("Payment Details:")
            self.payment.payment_method()


# Creating an order
order = Order(1)

# Creating products
product1 = Product("103", "Laptop", 50000)
product2 = Product("104", "Mouse", 1000)
product3 = Product("105", "Keyboard", 2000)

# Adding products to the order
order.add_product(product1)
order.add_product(product2)
order.add_product(product3)

# Creating and adding payment
payment = Payment("Credit Card", 53000)
order.set_payment(payment)

# Displaying order details
order.display_order()
```

---

## Input

```text
Order ID: 1

Product 1:
Product ID: 103
Name: Laptop
Price: 50000

Product 2:
Product ID: 104
Name: Mouse
Price: 1000

Product 3:
Product ID: 105
Name: Keyboard
Price: 2000

Payment Mode: Credit Card
Amount: 53000
```

The objects are created using:

```python
order = Order(1)

product1 = Product("103", "Laptop", 50000)
product2 = Product("104", "Mouse", 1000)
product3 = Product("105", "Keyboard", 2000)

payment = Payment("Credit Card", 53000)
```

---

## Output

```text
Order ID: 1
Products:
Product ID: 103
Name: Laptop
Price: 50000
Product ID: 104
Name: Mouse
Price: 1000
Product ID: 105
Name: Keyboard
Price: 2000
Total Amount: 53000
Payment Details:
Payment Mode: Credit Card
Amount: 53000
```

---

## Explanation

### 1. Creating the Order

```python
order = Order(1)
```

An `Order` object is created.

---

### 2. Adding Products

```python
order.add_product(product1)
order.add_product(product2)
order.add_product(product3)
```

The `Order` object contains multiple `Product` objects.

Therefore:

```text
Order HAS Products
```

---

### 3. Adding Payment

```python
order.set_payment(payment)
```

The `Order` object contains a `Payment` object.

Therefore:

```text
Order HAS Payment
```

---

### 4. Composition

The important part of the program is:

```python
self.products = []
self.payment = None
```

The `Order` class stores objects belonging to other classes.

This demonstrates the **has-a relationship** and therefore represents **composition**.

---

## Key Takeaway

**Composition allows a class to be built using objects of other classes and represents a "has-a" relationship.**

In this e-commerce system:

```text
Order
 ├── has Products
 └── has Payment
```

The `Order` class combines `Product` and `Payment` objects to represent a complete e-commerce order.

---



