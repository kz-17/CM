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
