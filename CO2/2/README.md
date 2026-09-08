
````markdown
# Q2 — PEP 604 Union Types

## Definition

A **Union Type** allows a variable, function parameter, or return value to accept **more than one possible data type**.

**PEP 604** introduced a concise syntax using the `|` operator to represent Union Types in Python.

For example:

```python
str | int
````

means that a value can be either a `str` or an `int`.

---

## Problem Statement

A customer may provide either a **mobile number** or an **email address** as their primary contact. Apply **PEP 604 Union Type syntax** to represent the contact information.

---

## Objective

To demonstrate the use of **PEP 604 Union Types** for allowing a function parameter to accept values of different data types.

---

## Concept

Before PEP 604, Union Types were commonly written using:

```python
from typing import Union

Union[str, int]
```

PEP 604 provides a simpler and more readable syntax:

```python
str | int
```

This indicates that the value can be either a string or an integer.

### Advantages

* Simple and readable syntax
* Supports multiple possible data types
* Improves type annotations
* Helps static type-checking tools identify incorrect types

---

## Syntax

```python
type1 | type2
```

Example:

```python
str | int
```

---

## Implementation

In this program:

| Parameter    | Type         | Purpose                                            |
| ------------ | ------------ | -------------------------------------------------- |
| `contact`    | `str \| int` | Accepts either an email address or a mobile number |
| Return value | `None`       | The function only displays the contact information |

---

## Python Program

```python
def set_primary_contact(contact: str | int) -> None:
    print("Primary contact:", contact)


set_primary_contact("customer@gmail.com")
set_primary_contact(9876543210)
```

---

## Input

```text
customer@gmail.com
9876543210
```

The values are passed to the function as:

```python
set_primary_contact("customer@gmail.com")
set_primary_contact(9876543210)
```

---

## Output

```text
Primary contact: customer@gmail.com
Primary contact: 9876543210
```

---

## Explanation

```python
contact: str | int
```

specifies that the `contact` parameter can accept either:

* `str` → for an email address
* `int` → for a mobile number

```python
-> None
```

indicates that the function does not return a value.

The `|` operator is the key feature of **PEP 604 Union Type syntax**.

---

## Key Takeaway

**PEP 604 simplifies Union Type annotations by replacing the older `Union[...]` syntax with the `|` operator.**

```python
str | int
```

means:

> The value can be either a string or an integer.
