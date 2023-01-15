year = (2017,2003,2011,2005,1987,2009,2020,2018,2009)

print("Accessing value at index -3: ",year[-3])
print("Original tuple",year)
y = reversed(year)
print("Reversed tuple",tuple(y))

count = year.count(2009)
print("Number of times 2009 in this tuple: ",count)

index = year.index(2018)
print("Index value of 2018: ",index)

print ("Length of tuple: ", len(year))

