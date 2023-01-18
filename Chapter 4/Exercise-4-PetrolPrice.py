import statistics
with open("PP.txt", "r") as f:
	lines = f.readlines()
	liters = []
	cost = []
	pData= [i.split() for i in lines]
	for l in lines:
		data = l.split()
		liters.append((data[0]))
		cost.append((data[1]))

my_int = 7

conversionl = [eval(i) for i in liters] 
conversionc = [eval(i) for i in cost]  

per_liter = [i / j for i, j in zip(conversionc, conversionl)]
average = sum(per_liter) / len(conversionc)


print(f'Fuel Data: {pData}')
print(f'\nOverall avg price per litres bought: {average}') 
print(per_liter)