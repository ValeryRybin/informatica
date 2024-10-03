import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import math

x = [1,2,3,4,5]
y = [20,60,770,20,1000]

plt.plot(x,y, color='blue', marker='^', markersize = 10)

plt.xlabel('Ось x')
plt.ylabel('Ось y')
plt.title('крутой график')

plt.grid(True, which='major', axis='both', linestyle='dashdot')

plt.show()