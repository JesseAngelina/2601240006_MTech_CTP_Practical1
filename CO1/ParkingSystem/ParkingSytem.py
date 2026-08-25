TOTAL_SLOTS = 100

parking = {}

while True:

    print("\n--- PARKING SYSTEM ---")
    print("1. Park Vehicle")
    print("2. Show Parking")
    print("3. Remove Vehicle & Calculate Charge")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    # Park Vehicle
    if choice == 1:

        if len(parking) == TOTAL_SLOTS:
            print("Parking is FULL!")

        else:
            vehicle = input("Enter vehicle number: ")

            for slot in range(1, TOTAL_SLOTS + 1):

                if slot not in parking:
                    parking[slot] = vehicle

                    print("Vehicle", vehicle, "parked in Slot", slot)
                    break

    # Show Parking
    elif choice == 2:

        print("\n--- PARKING DETAILS ---")

        if len(parking) == 0:
            print("Parking is empty.")

        else:
            for slot, vehicle in parking.items():
                print("Slot", slot, ":", vehicle)

            print("Available Slots:",
                  TOTAL_SLOTS - len(parking))

    # Remove Vehicle and Calculate Charge
    elif choice == 3:

        vehicle = input("Enter vehicle number to remove: ")

        found = False

        for slot in list(parking):

            if parking[slot] == vehicle:

                hours = int(input("Enter parking hours: "))
                rate = float(input("Enter rate per hour: "))

                charge = hours * rate

                print("\n--- PARKING BILL ---")
                print("Vehicle:", vehicle)
                print("Slot:", slot)
                print("Parking Hours:", hours)
                print("Rate per Hour:", rate)
                print("Parking Charge:", charge)

                del parking[slot]

                print("Vehicle removed successfully.")
                print("Slot", slot, "is now available.")

                found = True
                break

        if found == False:
            print("Vehicle not found.")

    # Exit
    elif choice == 4:

        print("Program ended.")
        break

    else:

        print("Invalid choice.")