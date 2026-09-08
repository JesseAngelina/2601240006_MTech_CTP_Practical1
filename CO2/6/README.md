# Q6 — Inheritance: Banking Application



````markdown
# Q6 — Inheritance: Banking Application

## Definition

**Inheritance** is an Object-Oriented Programming (OOP) concept in which a **child class** acquires the properties and methods of a **parent class**.

It promotes **code reusability** and allows child classes to provide their own specific behavior by overriding methods of the parent class.

---

## Problem Statement

A banking application has **Savings Account** and **Current Account** classes.

Both accounts have common attributes such as:

- Account number
- Account holder name
- Balance

However, their **withdrawal rules are different**.

Apply **inheritance** to design the banking application.

---

## Objective

To demonstrate the use of **inheritance** by creating a common parent class for bank accounts and specialized child classes for Savings and Current Accounts.

---

## Concept

In this program:

- `BankAccount` is the **parent/base class**.
- `SavingsAcc` is a **child/derived class**.
- `CurrentAcc` is a **child/derived class**.
- Common attributes and methods are defined in `BankAccount`.
- The `withdraw()` method is **overridden** in both child classes to implement different withdrawal rules.

### Class Relationship

```text
                 BankAccount
                 /         \
                /           \
        SavingsAcc       CurrentAcc
````

This represents an **"is-a" relationship**:

```text
SavingsAcc is a BankAccount
CurrentAcc is a BankAccount
```

---

## Advantages of Inheritance

* Promotes code reusability.
* Avoids duplication of common code.
* Allows specialized behavior in child classes.
* Makes the program easier to maintain.
* Supports method overriding.

---

## Implementation

The parent class `BankAccount` contains the common attributes:

```text
Account Number
Account Holder Name
Balance
```

The child classes implement their own `withdraw()` behavior.

### Savings Account

A withdrawal is allowed only when the withdrawal amount does not exceed the available balance.

### Current Account

A current account allows withdrawal up to a specified **overdraft limit** in addition to the available balance.

---

## Python Program

```python
class BankAccount:

    def __init__(self, acc_no, balance, name):
        self.acc_no = acc_no
        self.balance = balance
        self.name = name

    def deposit(self, amt):
        self.balance += amt
        print("Deposit:", amt)

    def display(self):
        print("Account Holder Name:", self.name)
        print("Account No:", self.acc_no)
        print("Account Balance:", self.balance)

    def withdraw(self, amt):
        print("Withdrawal rule: General account")


class SavingsAcc(BankAccount):

    def withdraw(self, amt):
        if amt <= self.balance:
            self.balance -= amt
            print("Withdrawal successful")
        else:
            print("Insufficient balance")


class CurrentAcc(BankAccount):

    def withdraw(self, amt):
        overdraft_limit = 1000

        if amt <= self.balance + overdraft_limit:
            self.balance -= amt
            print("Withdrawal successful")
        else:
            print("Withdrawal exceeds overdraft limit")


# Creating Savings Account
saving = SavingsAcc(101, 10000, "Jesse")

saving.withdraw(8000)
saving.display()

print()

# Creating Current Account
current = CurrentAcc(102, 10000, "Jesse")

current.withdraw(8000)
current.display()
```

---

## Input

### Savings Account

```text
Account Number: 101
Balance: 10000
Account Holder: Jesse
Withdrawal Amount: 8000
```

### Current Account

```text
Account Number: 102
Balance: 10000
Account Holder: Jesse
Withdrawal Amount: 8000
```

---

## Output

```text
Withdrawal successful
Account Holder Name: Jesse
Account No: 101
Account Balance: 2000

Withdrawal successful
Account Holder Name: Jesse
Account No: 102
Account Balance: 2000
```

---

## Explanation

### 1. Parent Class

```python
class BankAccount:
```

`BankAccount` is the parent class containing the common properties and methods of bank accounts.

### 2. Child Class

```python
class SavingsAcc(BankAccount):
```

`SavingsAcc` inherits the properties and methods of `BankAccount`.

### 3. Another Child Class

```python
class CurrentAcc(BankAccount):
```

`CurrentAcc` also inherits from `BankAccount`.

### 4. Method Overriding

Both child classes define their own:

```python
def withdraw(self, amt):
```

This is called **method overriding** because the child classes provide their own implementation of the `withdraw()` method.

### 5. Code Reusability

The child classes automatically receive:

```text
__init__()
deposit()
display()
```

from the parent class, so these methods do not need to be rewritten.

---

## Key Takeaway

**Inheritance allows child classes to reuse common properties and methods from a parent class while providing their own specialized behavior.**

In this banking application:

```text
BankAccount
     ↓
 ┌───────────────┐
 ↓               ↓
SavingsAcc    CurrentAcc
```

The `withdraw()` method is overridden to implement different withdrawal rules for each account type.

---


