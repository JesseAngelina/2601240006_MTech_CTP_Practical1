Python Programming & Object-Oriented Programming Assignment

Overview

This repository contains 7 Python programs covering Python type hints, Union types, Generics, Dataclasses, Inheritance, and Composition.

The programs are based on the questions provided in class and demonstrate the practical use of these concepts.

Questions Covered

Q1. PEP 484 Type Hints

Scenario:
A banking system processes transactions. Developers want static type checking to reduce errors.

Concept: PEP 484 Type Hints

Type hints specify the expected data types of function parameters and return values. They improve code readability and help static type-checking tools identify type-related errors.

Key Syntax:

def function_name(parameter: type) -> return_type:

Program: Q1_PEP484_TypeHints.py

Q2. PEP 604 Union Types

Scenario:
A customer may provide either a mobile number or an email address as a primary contact.

Concept: PEP 604 Union Types

PEP 604 provides a concise way to specify that a value can have multiple possible types using the | operator.

Key Syntax:

str | int

Program: Q2_PEP604_Union.py

Q3. Generic Types

Scenario:
An enterprise application needs repositories for different objects. The same repository logic should be reused.

Concept: Generics

Generics allow a class or function to work with different data types while maintaining type safety and code reusability.

Key Concepts:

TypeVar creates a type variable.

Generic is used to define a generic class.

T represents a generic type.

Program: Q3_Generic_Types.py

Q4. PEP 695 Generic Syntax

Scenario:
A production engineering team uses Python's newer generic syntax to create a reusable data store.

Concept: PEP 695

PEP 695 provides a modern and simpler syntax for defining generic classes using type parameters directly in square brackets.

Key Syntax:

class DataStore[T]:

Program: Q4_PEP695_Generic.py

Requirement: Python 3.12 or newer.

Q5. Dataclass

Scenario:
An inventory system stores product ID, product name, quantity, and price. The class mainly stores data and requires little custom initialization logic.

Concept: Dataclasses

The @dataclass decorator is used to create data-holding classes with less boilerplate code. It automatically provides methods such as __init__(), __repr__(), and __eq__().

Key Syntax:

from dataclasses import dataclass

@dataclass
class InventoryItem:
    ...

Program: Q5_Dataclass.py

Q6. Inheritance - Banking Application

Scenario:
A banking application has Savings Account and Current Account classes. Both accounts have common attributes such as account number, account holder name, and balance, but their withdrawal rules are different.

Concept: Inheritance

Inheritance allows a child class to acquire common properties and methods from a parent class.

Class Structure:

             BankAccount
              /        \
             /          \
     SavingsAcc       CurrentAcc

BankAccount → Parent/Base class

SavingsAcc → Child/Derived class

CurrentAcc → Child/Derived class

Common attributes are defined in BankAccount.

withdraw() is overridden in each child class because the withdrawal rules differ.

Program: Q6_Inheritance_Banking.py

Q7. Composition - E-Commerce Order

Scenario:
An e-commerce order contains multiple product objects and also has a payment object.

Concept: Composition

Composition represents a strong "has-a" relationship, where one class contains objects of other classes.

Class Structure:

             Order
            /     \
           /       \
      Products    Payment
       / | \
      /  |  \
 Product Product Product

Order has multiple Product objects.

Order has a Payment object.

add_product() adds products to the order.

set_payment() assigns a payment object to the order.

Program: Q7_Composition_Ecommerce.py

Concepts Summary

Q.No

Topic

Main Concept

Q1

PEP 484

Type Hints

Q2

PEP 604

Union Types

Q3

Generic Types

TypeVar and Generic

Q4

PEP 695

Modern Generic Syntax

Q5

Dataclass

@dataclass

Q6

Banking Application

Inheritance

Q7

E-Commerce Application

Composition
