menu = {
    "Baja Taco": 4.00, "Burrito": 7.50, "Bowl": 8.50,
    "Nachos": 11.00, "Quesadilla": 8.50, "Super Burrito": 8.50,
    "Super Quesadilla": 9.50, "Taco": 3.00, "Tortilla Salad": 8.00
}

total = 0

while True:
    try:
        food = input("Item: ").title()
        if food not in menu:
            pass
        else:
            total = total + menu[food]
            amount = "{:.2f}".format(total)
            print(f"Total: ${amount}")

    except EOFError:
        print()
        break