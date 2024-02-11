import matplotlib.pyplot as plt
import numpy as np
import random

detail = 20
zScale = 0.1
bounds = 5
xyScale = 0.5
xOffset = 1
yOffset = 1
speed = 0.1



def render(x,y,detailInput, zScaleInput, boundsInput = 6 ,xOffsetInput = 0, yOffsetInput = 0, jitterInput = 0, angle = 0, phaseInput = 4):
    

    equilibrium = 0
    amplitude = 0.25
    phase = ((2*np.pi)/phaseInput)
    
    z = []

    for i in range(len(x)):
        


        xVal = equilibrium + amplitude * np.sin(phase * x[i])
        yVal = equilibrium + amplitude * np.sin(phase * y[i])

        xVal = xVal * np.cos(angle) - yVal * np.sin(angle)
        yVal = xVal * np.sin(angle) + yVal * np.cos(angle)
        
        z.append(yVal)

    

    
    
    print(detailInput, zScaleInput, boundsInput, xOffsetInput, yOffsetInput)
    text = "Double sin wave with x,y: " + str(detailInput*2)
    ax.scatter(x, y, z, zdir='z', c=z, label=text)
    ax.set_zlim(-xyScale, xyScale)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')





ax = plt.figure(figsize=(14, 9)).add_subplot(projection='3d')
ax.view_init(elev=20., azim=-35, roll=0)





x = []
y = []

for i in range(-detail,detail,1):##Generate points
    for j in range(-detail,detail,1):
        x.append((i/detail*detail) + random.uniform(0,0.1))
        y.append((j/detail*detail) + random.uniform(0,0.1))


for i in range(100):
    #xOffset = i*speed
    #yOffset = (i/2)*speed
    angle = i/10
    render(x,y,detail, zScale,bounds,xyScale,xOffset,yOffset, angle=angle, phaseInput=20)
    plt.pause(0.1)
    ax.clear()

plt.show()


