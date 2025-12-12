#定義點
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


#定義線
class Line:
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C

#定義圓
class Circle:
    def __init__(self, h, k, r):
        self.h = h
        self.k = k
        self.r = r
#兩直線交點
def line_intersection(L1, L2):
    A1, B1, C1 = L1.A, L1.B, L1.C
    A2, B2, C2 = L2.A, L2.B, L2.C
    D = A1 * B2 - A2 * B1
    if D == 0:
        return None  # 平行或重合
    x = (B1 * C2 - B2 * C1) / D
    y = (C1 * A2 - C2 * A1) / D
    return Point(x, y)

#兩圓交點
import math

def circle_intersection(C1, C2):
    x1, y1, r1 = C1.h, C1.k, C1.r
    x2, y2, r2 = C2.h, C2.k, C2.r

    dx = x2 - x1
    dy = y2 - y1
    d = math.hypot(dx, dy)

    if d > r1 + r2 or d < abs(r1 - r2) or d == 0:
        return []  # 無交點或重合

    a = (r1*r1 - r2*r2 + d*d) / (2*d)
    h = math.sqrt(r1*r1 - a*a)

    xm = x1 + a * dx / d
    ym = y1 + a * dy / d

    xs1 = xm + h * dy / d
    ys1 = ym - h * dx / d

    xs2 = xm - h * dy / d
    ys2 = ym + h * dx / d

    return [Point(xs1, ys1), Point(xs2, ys2)]
    
#直線與圓的交點
def line_circle_intersection(L, C):
    A, B, D = L.A, L.B, L.C
    h, k, r = C.h, C.k, C.r

    # 找線上的任意點（令 x=0 try）
    if B != 0:
        x0 = 0
        y0 = -D / B
    else:
        y0 = 0
        x0 = -D / A

    # direction vector
    dx = B
    dy = -A

    # Solve quadratic (x0 + dx t - h)^2 + (y0 + dy t - k)^2 = r^2
    a = dx*dx + dy*dy
    b = 2*(dx*(x0 - h) + dy*(y0 - k))
    c = (x0 - h)**2 + (y0 - k)**2 - r*r

    disc = b*b - 4*a*c
    if disc < 0:
        return []

    t1 = (-b + math.sqrt(disc)) / (2*a)
    t2 = (-b - math.sqrt(disc)) / (2*a)

    P1 = Point(x0 + dx*t1, y0 + dy*t1)
    P2 = Point(x0 + dx*t2, y0 + dy*t2)

    return [P1, P2]

#線外一點到直線的垂足
def foot_of_perpendicular(L, P):
    A, B, C = L.A, L.B, L.C
    x0, y0 = P.x, P.y

    d = (A*x0 + B*y0 + C) / (A*A + B*B)

    x = x0 - A * d
    y = y0 - B * d

    return Point(x, y)

#利用垂足驗證畢氏定理
def dist2(P, Q):
    return (P.x - Q.x)**2 + (P.y - Q.y)**2

def verify_pythagoras(P, H, Q):
    return abs(dist2(P, H) + dist2(H, Q) - dist2(P, Q)) < 1e-6

#平移、縮放、旋轉
def transform_triangle(T, f):
    return Triangle(f(T.A), f(T.B), f(T.C))
