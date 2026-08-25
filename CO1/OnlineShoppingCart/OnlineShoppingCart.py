cart = []
discount = 0

while True:

    print("\n--- ONLINE SHOPPING CART ---")
    print("1. Add Product")
    print("2. Remove Product")
    print("3. Change Quantity")
    print("4. Apply Discount")
    print("5. Display Bill")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    # Add Product
    if choice == 1:

        product = input("Enter product name: ")
        price = float(input("Enter product price: "))
        quantity = int(input("Enter quantity: "))

        cart.append([product, price, quantity])

        print("Product added to cart.")

    # Remove Product
    elif choice == 2:

        product = input("Enter product name to remove: ")

        found = False

        for item in cart:
            if item[0] == product:
                cart.remove(item)
                print("Product removed.")
                found = True
                break

        if found == False:
            print("Product not found.")

    # Change Quantity
    elif choice == 3:

        product = input("Enter product name: ")
        quantity = int(input("Enter new quantity: "))

        found = False

        for item in cart:
            if item[0] == product:
                item[2] = quantity
                print("Quantity updated.")
                found = True
                break

        if found == False:
            print("Product not found.")

    # Apply Discount
    elif choice == 4:

        discount = float(input("Enter discount percentage: "))

        print("Discount of", discount, "% applied.")

    # Display Bill
    elif choice == 5:

        subtotal = 0

        print("\n--- FINAL BILL ---")

        for item in cart:

            product = item[0]
            price = item[1]
            quantity = item[2]

            total = price * quantity
            subtotal = subtotal + total

            print(product, "-", quantity, "x", price, "=", total)

        print("Subtotal:", subtotal)

        discount_amount = subtotal * discount / 100

        amount_after_discount = subtotal - discount_amount

        gst = amount_after_discount * 18 / 100

        final_amount = amount_after_discount + gst

        print("Discount:", discount_amount)
        print("Amount After Discount:", amount_after_discount)
        print("GST (18%):", gst)
        print("Final Bill:", final_amount)

    # Exit
    elif choice == 6:

        print("Thank you for shopping!")
        break

    else:

        print("Invalid choice.")