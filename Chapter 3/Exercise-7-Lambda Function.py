marks = [("CodeLab I",67),("web Development", 75),("CodeLabII",74),("Smartphone Apps",68),("Games Development",70),("Responsive web",65)]

marks = tuple(sorted(list(marks), key=lambda x: x[1]))

print("Marks low to high: ", marks)

newList = sorted(marks, key = lambda x : x[1],reverse=True)
print("Marks high to low: ",newList)






