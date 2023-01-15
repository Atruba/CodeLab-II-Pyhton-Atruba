numbers = [11, 10, 14, 13, 12, 16, 20, 18, 19, 17 ]
for x in range(len(numbers)):
    print (numbers[x])
    
highest = max(numbers)
print("The highest value in this list: ",highest)

lowest = min(numbers)
print("The lowest value in this list: ",lowest)

numbers.sort()

print("Sorted list in Ascending order: ",numbers)

numbers.sort(reverse=True)

print("Sorted list in Descending order:", numbers)

numbers.append(50)
numbers.append(60)

print("List after appending: ", numbers)


    

