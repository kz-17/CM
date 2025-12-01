# 用numpy求解
import numpy as np

# c = [c0, c1, ..., cn]  
c = [1, 0, -3, 0, 2]   # 例如 f(x) = 2x^4 - 3x^2 + 1

roots = np.roots(list(reversed(c)))
print(roots)
