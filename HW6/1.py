#定義點(1, 1)
import math
import matplotlib.pyplot as plt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        return self.x, self.y
point = Point(1, 1)
plt.grid()
plt.scatter(*point.show())

#定義線(0, 0)到(1, 1)
import math
import matplotlib.pyplot as plt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        return self.x, self.y
point = Point(1, 1)
print(*point.show())
points = point.show()
X = [0, points[0]]
y = [0, points[1]]
plt.grid()
plt.plot(X, y)

#定億圓
import math
import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2*np.pi, 100)  
X = np.cos(theta)
y = np.sin(theta)

plt.plot(X, y)
plt.axis('equal')
plt.grid()
