def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def modulus(a, b):
    return a % b

def greater(a, b):
    return a > b


print("Choose your option:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Modulus")
print("6.Check greater Number")

while True:
    # User input
    choice = input("Enter choice(1/2/3/4/5/6): ")

    # Options check
    if choice in ('1', '2', '3', '4','5','6'):
        try:
            num1 = float(input("Your First number: "))
            num2 = float(input("Your Second number: "))
        except ValueError:
            print("Invalid input.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '5':
            print(num1, "/", num2, "=", modulus(num1, num2))
        
        elif choice == '6':
            print(num1, "/", num2, "=", greater(num1, num2))
        
        #For calculating again
        next_calculation = input("Do you want to quit? (press Q): ")
        if next_calculation == "Q":
          break
    else:
        print("Invalid Input")