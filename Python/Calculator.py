def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def mul(x, y):
    return x * y
def div(x, y):
    return x / y
def mod(x, y):
    return x % y

while True:
    print("Please select any option : ")
    print("1. Add ")
    print("2. Sub ")
    print("3. Mul ")
    print("4. Div ")
    print("5. Mod ")

    choice = input("Please enter your choice : ")

    if choice in ('1', '2', '3', '4', '5'):
        num1 = float(input("Please enter first number : "))
        num2 = float(input("Please enter second number : "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", sub(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", mul(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", div(num1, num2))

        elif choice == '5':
            print(num1, "%", num2, "=", mod(num1, num2))

        next_calculation = input("Continue to y and Exit to n : (y/n) : ")
        if next_calculation == "n":
            print("Exit")
            break

    else:
        print("Please enter valid input")