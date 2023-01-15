num_1=int(input("Enter your 1st number:"))
num_2=int(input("Enter your 2nd number:"))
num_3=int(input("Enter your 3rd number:"))

if (num_1 >= num_2) and (num_1 >= num_3):
   largest = num_1
elif (num_2 >= num_1) and (num_2 >= num_3):
   largest = num_2
else:
   largest = num_3

print("The largest number is", largest)