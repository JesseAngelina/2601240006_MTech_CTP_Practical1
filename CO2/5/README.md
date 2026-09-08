# Q5 — Dataclass

Copy-paste this directly into your `README.md`:

````markdown
# Q5 — Dataclass

## Definition

A **dataclass** is a special type of Python class designed mainly for **storing data**.

The `@dataclass` decorator automatically generates common methods such as `__init__()`, `__repr__()`, and `__eq__()`. This reduces boilerplate code and makes data-oriented classes easier to create and maintain.

---

## Problem Statement

An inventory system stores the following information about a product:

- Product ID
- Product Name
- Quantity
- Price

The class mainly stores data and requires little custom initialization logic. Apply a **dataclass** to model the inventory item.

---

## Objective

To demonstrate the use of the **`@dataclass` decorator** to create a simple and efficient data-holding class.

---

## Concept

Normally, when creating a class to store data, we have to manually write an `__init__()` method.

For example:

```python
class Product:
    def __init__(self, product_id, product_name, quantity, price):
        self.product_id = product_id
        self.product_name = product_name
        self.quantity = quantity
        self.price = price
````

Using a dataclass, the same data structure can be written more simply:

```python
from dataclasses import dataclass

@dataclass
class InventoryItem:
    product_id: int
    product_name: str
    quantity: int
    price: float
```

The `@dataclass` decorator automatically creates the required constructor and other useful methods.

---

## Syntax

```python
from dataclasses import dataclass

@dataclass
class ClassName:
    attribute: type
```

---

## Advantages of Dataclasses

* Reduces boilerplate code.
* Automatically generates `__init__()`.
* Provides a useful `__repr__()` for displaying objects.
* Automatically supports value-based equality using `__eq__()`.
* Makes data-holding classes clean and readable.

---

## Implementation

The `InventoryItem` dataclass contains four attributes:

| Attribute      | Type    | Description               |
| -------------- | ------- | ------------------------- |
| `product_id`   | `int`   | Unique product identifier |
| `product_name` | `str`   | Name of the product       |
| `quantity`     | `int`   | Number of items available |
| `price`        | `float` | Price of the product      |

---

## Python Program

```python
from dataclasses import dataclass


@dataclass
class InventoryItem:
    product_id: int
    product_name: str
    quantity: int
    price: float


item = InventoryItem(101, "Laptop", 10, 55000.0)

print(item)
```

---

## Input

```text
Product ID: 101
Product Name: Laptop
Quantity: 10
Price: 55000.0
```

The values are passed to the dataclass constructor as:

```python
InventoryItem(101, "Laptop", 10, 55000.0)
```

---

## Output

```text
InventoryItem(product_id=101, product_name='Laptop', quantity=10, price=55000.0)
```

---

## Explanation

### 1. Importing Dataclass

```python
from dataclasses import dataclass
```

The `dataclass` decorator is imported from Python's built-in `dataclasses` module.

### 2. Declaring the Dataclass

```python
@dataclass
class InventoryItem:
```

The `@dataclass` decorator tells Python to automatically generate common methods for the class.

### 3. Defining Attributes

```python
product_id: int
product_name: str
quantity: int
price: float
```

These define the data stored by each inventory item.

### 4. Creating an Object

```python
item = InventoryItem(101, "Laptop", 10, 55000.0)
```

The automatically generated `__init__()` method initializes the object.

### 5. Displaying the Object

```python
print(item)
```

The automatically generated `__repr__()` method produces a readable representation of the object.

---

## Key Takeaway

A **dataclass** is useful when a class primarily stores data. The `@dataclass` decorator automatically provides common methods, reducing the amount of code that needs to be written manually.

```python
@dataclass
class InventoryItem:
    product_id: int
    product_name: str
    quantity: int
    price: float
```





**Key thing to remember for Q5:**
`@dataclass` = **less code for classes that mainly store data**.
