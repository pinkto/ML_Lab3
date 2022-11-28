import numpy as np
import matplotlib.pyplot as plt

def createCircleTensor(height=500, width=500, radius=250, color=None):
    image = np.zeros([height, width, 3], dtype=np.uint8)  #Creating a tensor filled with zeros

    x0 = width / 2  #Center of the circle in the middle of the width
    y0 = height / 2  #Center of the circle in the middle of the height

    for x in range(0, width):
        for y in range(0, height):
            if (x - x0) ** 2 + (y - y0) ** 2 <= radius ** 2:  #The circle equation
                image[x, y] = color

    return image

circle = createCircleTensor(height = 250, width = 250, radius = 100,color = [0,0,255])

plt.imshow(circle, interpolation='nearest')
plt.show()

np.save("/Users/annaabdeeva/PycharmProjects/ML LAB_3 - Boldyreva, Samorokov/circle.npy", circle)

circle2 = np.load("/Users/annaabdeeva/PycharmProjects/ML LAB_3 - Boldyreva, Samorokov/circle.npy")

#Check
plt.imshow(circle2, interpolation='nearest')
plt.show()