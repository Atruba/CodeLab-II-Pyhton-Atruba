def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def modulus(x, y):
    return x % y

print("Menu: ")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulus")
x=int(input("Choose your option: "))

if x in ('1', '2', '3', '4', '5'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if x == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif x == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif x == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif x == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        elif x == '5':
            print(num1, "/", num2, "=", modulus(num1, num2))
        
        message = input("Let's do next calculation? (yes/no): ")
       
        if message == "no":
        break
        
    
else:
        print("Invalid Input")