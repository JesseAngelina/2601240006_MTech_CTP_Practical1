# Car Parking System

## 1. Objective

To develop a Python-based car parking management system that allows vehicles to be parked, displays parking details, removes vehicles, and calculates parking charges based on the parking duration and hourly rate.

## 2. Algorithm

1. Start.
2. Set the total number of parking slots to 100.
3. Create an empty dictionary to store parking slot numbers and vehicle numbers.
4. Display the parking system menu.
5. Read the user's choice.
6. If the choice is **1 (Park Vehicle)**:

   * Check whether all 100 slots are occupied.
   * If parking is full, display "Parking is FULL!".
   * Otherwise, read the vehicle number.
   * Search for the first available parking slot.
   * Assign the vehicle to the available slot.
   * Display the allocated slot number.
7. If the choice is **2 (Show Parking)**:

   * Check whether the parking area is empty.
   * If empty, display "Parking is empty."
   * Otherwise, display all occupied slots and their vehicle numbers.
   * Calculate and display the number of available slots.
8. If the choice is **3 (Remove Vehicle & Calculate Charge)**:

   * Read the vehicle number to be removed.
   * Search for the vehicle in the parking dictionary.
   * If the vehicle is found:

     * Read the parking hours.
     * Read the rate per hour.
     * Calculate the parking charge using:
       **Parking Charge = Parking Hours × Rate per Hour**
     * Display the parking bill.
     * Remove the vehicle from the parking slot.
     * Mark the slot as available.
   * If the vehicle is not found, display "Vehicle not found."
9. If the choice is **4 (Exit)**:

   * Display "Program ended."
   * Terminate the program.
10. For any other choice, display "Invalid choice."
11. Repeat the menu until the user chooses Exit.
12. Stop.

## 3. Input

The program accepts:

* Menu choice
* Vehicle number
* Parking hours
* Rate per hour

## 4. Output

The program displays:

* Vehicle parking slot number
* Parking status
* List of parked vehicles
* Number of available slots
* Parking bill
* Vehicle number
* Slot number
* Parking hours
* Rate per hour
* Total parking charge
* Appropriate messages for full parking, unavailable vehicles, empty parking, and invalid choices

## 5. Time Complexity

Let `n` be the number of occupied parking slots, with a maximum of 100 slots.

* **Park Vehicle:** O(100), which is effectively **O(1)** because the parking capacity is fixed at 100.
* **Show Parking:** O(n)
* **Remove Vehicle:** O(n)
* **Calculate Charge:** O(1)
* **Exit:** O(1)

Therefore, the worst-case time complexity of a menu operation is **O(n)**.

Since the maximum number of slots is fixed at 100, the practical maximum is bounded by a constant.
