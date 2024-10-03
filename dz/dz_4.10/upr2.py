import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import math

amount = [18,70,19,19,10,53]
groups = ['самосир','чопиксы','тоба','суматра','холм','палатка']
colours = ["red", "violet", "yellow", "purple", "blue", "grey"]
plt.pie(amount,labels=groups, colors=colours, autopct='%1.f%%')
plt.show()