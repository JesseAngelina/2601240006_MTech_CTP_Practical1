# 16. Cloud API Integration

A cloud application receives data from multiple sources. Objects from different classes may provide a `read()` method, and the same processing function should work with all of them.

## Question

**(a)** Explain how duck typing can be used in this situation. **[2]**

**(b)** Write a Python function that accepts any object supporting `read()`. **[3]**

**(c)** Explain why explicit type checking may not be necessary, and state one advantage and one limitation of duck typing. **[3]**

---

## Solution

Different objects from different classes can provide the same `read()` method.

Python uses **duck typing**, which means the type or class of an object is less important than the methods or operations it supports.

If an object has a `read()` method, the processing function can use it without checking which class the object belongs to.

---

## (a) Duck Typing in Cloud API Integration

Duck typing allows objects from different classes to be used by the same function, as long as they provide the required `read()` method.

### Example

Consider two different classes:

```python
class FileSource:
    def read(self):
        return "Data from file"


class CloudSource:
    def read(self):
        return "Data from cloud"
```

Both classes have a `read()` method. Although the classes are different, the same processing function can work with both objects.

### 1. Duck Typing

Python does **not** need to check whether the object belongs to `FileSource` or `CloudSource`. It only checks whether the object can perform the required operation:

```
Does the object have read()?
        │
       YES
        │
        ▼
   Process the data
```

Therefore, both objects can be passed to the same function.

### 2. Same Function for Different Objects

The same processing function can accept objects from different classes:

```python
process_data(FileSource())
process_data(CloudSource())
```

---

## (b) Python Function

```python
def process_data(source):
    if hasattr(source, "read") and callable(source.read):
        print(source.read())
    else:
        print("Error: object does not support read()")


class FileSource:
    def read(self):
        return "Data from file"


class CloudSource:
    def read(self):
        return "Data from cloud"


sources = [FileSource(), CloudSource()]

for src in sources:
    process_data(src)
```

### Output

```
Data from file
Data from cloud
```

---

## (c) Why Explicit Type Checking Is Not Necessary

Python is **dynamically typed**, so the interpreter checks what an object can do at **runtime**, based on its available methods, not on a declared class or interface.

- The processing function does not need to know in advance which classes it will receive.
- Any object that "behaves like" a readable source (i.e., provides `read()`) is automatically compatible.
- This matches the Python data model, where behavior is defined by supported operations rather than inheritance.

### Advantage

**Flexibility and extensibility** — new data source classes can be added without changing the processing function, as long as they implement `read()`.

### Limitation

**Runtime errors instead of compile-time errors** — if an object passed in does not actually support `read()`, the error (`AttributeError`) is only discovered when the code runs, not beforehand.

---

## Time Complexity Note

Duck typing itself does not add asymptotic overhead — the extra cost is only the `hasattr()`/`callable()` check, which is **O(1)**.
