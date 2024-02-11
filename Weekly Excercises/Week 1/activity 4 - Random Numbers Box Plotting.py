import numpy as np
import matplotlib.pyplot as plt
import time


plotPoints = 100

def bubbleSort(array):
    start = time.time()
    n = len(array)
    swapped = False
    for i in range(n-1):#loop through all numbers
        for j in range(n-i-1):#n numbers where i numbers are already sorted
            if array[j] > array[j + 1]:
                swapped = True
                array[j], array[j + 1] = array[j + 1], array[j]
    end = time.time()
    print(end - start)
    return array



x = np.random.randn(plotPoints)
y = np.random.rand(plotPoints)



bins = np.linspace(-10, 10, 200)

plt.hist(x, bins, alpha=0.4, label='Random')
plt.hist(y, bins, alpha=0.4, label='Uniform')
plt.legend(loc='upper right')
plt.xlabel("Value")
plt.ylabel("Count of Value")
text = "*Plotted using "+str(plotPoints) + " points for each*"
plt.figtext(0, 0.01, text, ha="left", fontsize=10 )
plt.show()





