from math import *
import numpy as np
import matplotlib.pyplot as plt

xMin = -3
xMax = 3
yMin = -1
yMax = 1
step_size = 0.01
precision = 0.00000000001
i = 0
 
def xPartialDer(x, y):
    return 2/9*x*cos(x**2/9+y**2)

def yPartialDer(y, x):
	return 2*y*cos(x**2/9+y**2)

while abs(xMax - xMin) and abs(yMax - yMin)  > precision:
    xMin = xMax 
    gradient = xPartialDer(xMin, 0) 
    move = gradient * step_size
    xMax = xMin - move
    yMin = yMax 
    gradient = yPartialDer(yMin, 0) 
    move = gradient * step_size
    yMax = yMin - move
    i = i + 1
    plt.plot(2/9*x*cos(x**2/9+y**2))



    
print ("Number of iteration ", i)
print("Local minimum for X occurs at ", xMin)
print("Local minimum for Y occurs at ", yMin)

plt.ylabel('some numbers')
plt.show()