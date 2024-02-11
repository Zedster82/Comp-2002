import matplotlib.pyplot as plt
import numpy as np
import random



def render(detailInput, zScaleInput, boundsInput, xyScaledInput,xOffsetInput = 0, yOffsetInput = 0):
    x = []
    y = []
    random.seed(10)
    for i in range(-detailInput,detailInput,1):
        for j in range(-detailInput,detailInput,1):
            x.append((i/detailInput*boundsInput) + random.uniform(0,0.1))
            y.append((j/detailInput*boundsInput) + random.uniform(0,0.1))

    x2 = [j * xyScaledInput for j in x]
    y2 = [j * xyScaledInput for j in y]

    x2 = [j + xOffsetInput for j in x]
    y2 = [j + yOffsetInput for j in y]

    z = (np.sin(x2) * np.sin(y2))*zScaleInput
    
    print(detailInput, zScaleInput, boundsInput, xyScaledInput,xOffsetInput, yOffsetInput)
    text = "Double sin wave with x,y: " + str(detailInput*2)
    ax.scatter(x, y, z, zdir='z', c=z, label=text)
    ax.set_zlim(-xyScale, xyScale)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')





ax = plt.figure(figsize=(14, 9)).add_subplot(projection='3d')
ax.view_init(elev=20., azim=-35, roll=0)



detail = 20
zScale = 1
bounds = 10
xyScale = 10
xOffset = 1
yOffset = 1
speed = 0.1



for i in range(300):
    xOffset = i*speed
    yOffset = (i/2)*speed
    render(detail,zScale,bounds,xyScale,xOffset,yOffset)
    plt.pause(0.06)
    ax.clear()

plt.show()


