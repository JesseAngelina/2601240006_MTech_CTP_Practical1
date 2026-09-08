
# Q3 — Generic Types

Copy-paste this directly into your `README.md`:

````markdown
# Q3 — Generic Types

## Definition

**Generics** are a programming feature that allows a class or function to work with **different data types** while maintaining type safety and code reusability.

In Python, generics allow us to write a single class or function that can operate on different types of data instead of creating separate implementations for each type.

---

## Problem Statement

An enterprise application needs repositories for different objects. The same repository logic should be reused for different types of objects.

Apply **Generic Types** to create a reusable repository.

---

## Objective

To demonstrate how **Generic Types** can be used to create a reusable and type-safe repository that can store and retrieve objects of different types.

---

## Concept

A generic class uses a **type variable** as a placeholder for a specific data type.

Python provides:

- `TypeVar` → Creates a type variable.
- `Generic` → Used to define a generic class.
- `T` → Commonly used as the name of the generic type variable.

For example:

```python
T = TypeVar("T")
````

Here, `T` represents a type that will be specified when the generic class is used.

---

## Why Use Generics?

Generics provide:

* **Code reusability** — the same class can be used for different types.
* **Type safety** — helps ensure that objects of the expected type are used.
* **Maintainability** — avoids writing duplicate classes.
* **Flexibility** — the same repository can work with different objects.

---

## Syntax

```python
from typing import Generic, TypeVar

T = TypeVar("T")

class Repository(Generic[T]):
    ...
```

---

## Implementation

The `Repository` class is designed as a generic class.

It can be used for different types such as:

```python
Repository[User]
Repository[Product]
```

The same repository implementation can therefore be reused without creating separate repository classes.

---

## Python Program

```python
from typing import Generic, TypeVar

T = TypeVar("T")


class Repository(Generic[T]):

    def __init__(self):
        self.items: list[T] = []

    def add(self, item: T) -> None:
        self.items.append(item)

    def get_all(self) -> list[T]:
        return self.items


class User:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


user_repo = Repository[User]()

user_repo.add(User("Alice"))
user_repo.add(User("Bob"))

print(user_repo.get_all())
```

---

## Input

```text
Alice
Bob
```

The values are provided to the repository through:

```python
user_repo.add(User("Alice"))
user_repo.add(User("Bob"))
```

---

## Output

```text
[Alice, Bob]
```

---

## Explanation

### 1. Creating a Type Variable

```python
T = TypeVar("T")
```

`T` acts as a placeholder for a data type.

---

### 2. Creating a Generic Class

```python
class Repository(Generic[T]):
```

This makes `Repository` a generic class that can work with different types.

---

### 3. Storing Generic Objects

```python
self.items: list[T] = []
```

This specifies that the list contains objects of type `T`.

---

### 4. Adding an Object

```python
def add(self, item: T) -> None:
```

The `add()` method accepts an object of the specified generic type.

---

### 5. Retrieving Objects

```python
def get_all(self) -> list[T]:
```

The method returns a list containing objects of type `T`.

---

### 6. Creating a User Repository

```python
user_repo = Repository[User]()
```

Here, `T` becomes `User`.

Therefore, this repository is specifically used for storing `User` objects.

---

## Key Takeaway

Generics allow us to create **one reusable repository class** that can work with different data types while providing better type safety and reducing duplicate code.

```python
Repository[User]
Repository[Product]
```

Both can use the same `Repository` implementation.

---



