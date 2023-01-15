import matplotlib.pyplot as plt
import numpy as np
 
# create data
x = ['Male', 'Female']
y1 = np.array([279, 200 ])
y2 = np.array([81, 156])
y3 = np.array([132, 160])
y4 = np.array([492, 516])
 
# plot bars in stack manner
plt.bar(x, y1, color='r')
plt.bar(x, y2, bottom=y1, color='b')
plt.bar(x, y3, bottom=y1+y2, color='y')
plt.bar(x, y4, bottom=y1+y2+y3, color='g')
plt.xlabel("Gender")
plt.ylabel("Number of people watching")
plt.legend(["Game", "Commercials", "won't watch", "Total"])
plt.title("Stack bar graph")
plt.show()