import cmath
import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt


#3x^2 + 2x + 12
a = 3
b = 2
c = 12

def get_y(x):
    a*(x**2) + b*x + c
def get_x(y):
    return (-b + cmath.sqrt(b**2 - (4*a*(c-y))))/(a*2), (-b - cmath.sqrt(b**2 - (4*a*(c-y))))/(a*2)

def generate_data(min, max):
    xc, yc, zc = [], [], []
    for y in range(min, max):
        temp = get_x(y)
        zc.append(y)
        xc.append(temp[0].real)
        yc.append(temp[0].imag)

        zc.append(y)
        xc.append(temp[1].real)
        yc.append(temp[1].imag)
    return np.array(xc), np.array(yc), np.array(zc)

x, y, z = generate_data(-1000,1000)
fig = plt.figure(figsize = (12,10))
ax = plt.axes(projection='3d')

surf = ax.scatter(x, y, z, c = 'r', s = 10)

# Set axes label
ax.set_xlabel('X axis', labelpad=20)
ax.set_ylabel('Imaginary axis', labelpad=20)
ax.set_zlabel('Y axis', labelpad=20)

plt.show()
