menu = {
    "Burger": 120,
    "Pizza": 250,
    "Fries": 80,
    "Coke": 40
}

cart = []

def show_menu():
    print("\n----- FOOD MENU -----")
    for item, price in menu.items():
        print(item, "- Rs.", price)

def add_item():
    item = input("Enter item name: ").title()

    if item in menu:
        quantity = int(input("Enter quantity: "))

        if quantity > 0:
            cart.append([item, quantity])
            print(item, "added to cart")
        else:
            print("Invalid quantity")
    else:
        print("Item not available. Please choose from menu.")

def remove_item():
    item = input("Enter item to remove: ").title()

    for food in cart:
        if food[0] == item:
            cart.remove(food)
            print(item, "removed from cart")
            return

    print("Item not found in cart")

def checkout():
    if len(cart) == 0:
        print("Your cart is empty")
        return

    subtotal = 0

    for food in cart:
        subtotal = subtotal + menu[food[0]] * food[1]

    print("\nSubtotal:", subtotal)

    coupon = input("Enter coupon code or press Enter: ").upper()

    discount = 0

    if coupon == "SAVE10":
        discount = subtotal * 0.10
    elif coupon != "":
        print("Invalid coupon code. Only SAVE10 is accepted.")

    amount = subtotal - discount
    gst = amount * 0.05

    if subtotal >= 300:
        delivery = 0
    else:
        delivery = 40

    total = amount + gst + delivery

    print("\n----- BILL -----")
    print("Subtotal:", subtotal)
    print("Discount:", discount)
    print("GST (5%):", gst)
    print("Delivery:", delivery)
    print("Total Amount:", total)
    print("Thank you for ordering!")

while True:
    print("\n===== ONLINE FOOD ORDERING SYSTEM =====")
    print("1. Show Menu")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. View Cart")
    print("5. Checkout")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_menu()

    elif choice == "2":
        show_menu()
        add_item()

    elif choice == "3":
        remove_item()

    elif choice == "4":
        print("\nYour Cart:")
        for food in cart:
            print(food[0], "Quantity:", food[1])

    elif choice == "5":
        checkout()

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Try again.")