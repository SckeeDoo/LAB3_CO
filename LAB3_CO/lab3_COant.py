from math import *

xMin = 0
yMin = 0
initX = 1.1
initY = 0.8

i = 0

alpha = 0.01     
precision = 0.00000001

def functionOne(x, y):
    return 2 * x / 9 * cos( (x**2 / 9) + y**2)

def functionTwo(x, y):
    return 2 * y * cos((x**2 / 9) + y**2)



while ( (abs(initX - xMin)) > precision and (abs(initY - yMin)) > precision ):
    if initX>=3 or initX<=-3 or initY >=1 or initY <=-1:
        continue
    i +=1
    xMin = initX
    initX = xMin - alpha * functionOne(xMin, yMin)
    yMin = initY
    initY = yMin - alpha * functionTwo(xMin, yMin)

print ("Number of iterations = ", i )
print ("X mininum = ", initX)
print ("Y mininum = ", initY)
