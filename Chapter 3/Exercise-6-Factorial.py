def factorial(n):
	if n==1:
        return n
    else:
    return n*factorial(n-1)

number = int(input("Please Enter a number: "))  

if number < 0:  
   print("Please enter a positive number")  
elif number == 0:  
   print("The factorial of 0 is 1")  
else:  
   print("The factorial of",number,"is",factorial(number))  

