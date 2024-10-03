import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import math

x = ['yadegha','rukzack_90l','aptechka','sovet-moped','chron']
y = [21,70,60,12,5]

plt.bar(x,y,color='orange', label='podgotovka k yadeghke', alpha=0.6)
plt.plot(x,y,color='red',marker='o',markersize=15)
plt.legend(loc='best')
plt.show()