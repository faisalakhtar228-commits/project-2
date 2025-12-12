import math

def calculator():
    print("\n===== ADVANCED CALCULATOR =====")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (x^n)")
    print("6. Square Root (√x)")
    print("7. Sine (sin)")
    print("8. Cosine (cos)")
    print("9. Tangent (tan)")
    print("10. Log (natural log)")
    print("11. Log10")
    print("0. Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 0:
        print("Exiting calculator...")
        return False

    # Basic operations
    if choice in [1, 2, 3, 4, 5]:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == 1:
            print("Result:", a + b)
        elif choice == 2:
            print("Result:", a - b)
        elif choice == 3:
            print("Result:", a * b)
        elif choice == 4:
            if b == 0:
                print("Error: Division by zero!")
            else:
                print("Result:", a / b)
        elif choice == 5:
            print("Result:", math.pow(a, b))

    # Single value functions
    elif choice in [6, 7, 8, 9, 10, 11]:
        x = float(input("Enter number: "))

        if choice == 6:
            print("Result:", math.sqrt(x))
        elif choice == 7:
            print("Result:", math.sin(math.radians(x)))
        elif choice == 8:
            print("Result:", math.cos(math.radians(x)))
        elif choice == 9:
            print("Result:", math.tan(math.radians(x)))
        elif choice == 10:
            print("Result:", math.log(x))
        elif choice == 11:
            print("Result:", math.log10(x))

    else:
        print("Invalid choice!")

    return True


# Main Program Loop
while True:
    if not calculator():
        break

