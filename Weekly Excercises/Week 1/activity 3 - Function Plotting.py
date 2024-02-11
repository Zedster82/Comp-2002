import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm

plotPoints = 100




x = np.linspace(-np.pi, np.pi, 100)
#x = [j * 2 for j in x]

color = iter(cm.rainbow(np.linspace(0, 1, plotPoints)))
for i in range(plotPoints):
   xIteration = x[i]
   y = np.sin(xIteration)
   c = next(color)
   plt.scatter(xIteration, y, c=c)

#plt.scatter(x,y)
plt.show()