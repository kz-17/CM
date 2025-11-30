# 1.計算一公平銅板，連續投擲 10000 次，全部得到正面的機率。 (p^10000)
p = 0.5
n = 10000
prob = p ** n
print(prob)

#2. log(p^n) = n log(p) 計算 log(p^n)，然後代入 p=0.5，算出 log(0.5^10000)
import math

p = 0.5
n = 10000

log_value = n * math.log(p)
print(log_value )
print(math.exp(log_value)) 

# 3.『熵，交叉熵，KL 散度，互熵（互資訊）』
import math

def entropy(p):
    return -sum(pi * math.log(pi) for pi in p if pi > 0)

def cross_entropy(p, q):
    return -sum(pi * math.log(qi) for pi, qi in zip(p, q) if pi > 0 and qi > 0)

def kl_divergence(p, q):
    return sum(pi * math.log(pi / qi) for pi, qi in zip(p, q) if pi > 0 and qi > 0)

def mutual_information(p_xy, p_x, p_y):
    I = 0
    for i in range(len(p_x)):
        for j in range(len(p_y)):
            if p_xy[i][j] > 0:
                I += p_xy[i][j] * math.log(p_xy[i][j] / (p_x[i] * p_y[j]))
    return I


# Example
p = [0.4, 0.6]
q = [0.5, 0.5]

print("Entropy H(p) =", entropy(p))
print("Cross-entropy H(p,q) =", cross_entropy(p, q))
print("KL(p||q) =", kl_divergence(p, q))

# 4. 驗證 cross_entropy(p,p) > cross_entropy(p,q), 當 q != p 時
import math

def entropy(p):
    return -sum(pi * math.log(pi) for pi in p if pi > 0)

def cross_entropy(p, q):
    return -sum(pi * math.log(qi) for pi, qi in zip(p, q) if pi > 0 and qi > 0)

def kl_divergence(p, q):
    return sum(pi * math.log(pi / qi) for pi, qi in zip(p, q) if pi > 0 and qi > 0)

def mutual_information(p_xy, p_x, p_y):
    I = 0
    for i in range(len(p_x)):
        for j in range(len(p_y)):
            if p_xy[i][j] > 0:
                I += p_xy[i][j] * math.log(p_xy[i][j] / (p_x[i] * p_y[j]))
    return I


# Example
p = [0.4, 0.6]
q = [0.5, 0.5]

print("Entropy H(p) =", entropy(p))
print("Cross-entropy H(p,q) =", cross_entropy(p, q))
print("KL(p||q) =", kl_divergence(p, q))

# 5. 『7-4 漢明碼』的編碼與解碼程式
p = [0.4, 0.6]
q = [0.5, 0.5]

H_pp = cross_entropy(p, p)
H_pq = cross_entropy(p, q)

print("H(p,p) =", H_pp)
print("H(p,q) =", H_pq)
print("H(p,p) < H(p,q)?", H_pp < H_pq)

# 6. 『夏農信道編碼定理』和『夏農-哈特利定理 (Shannon–Hartley Theorem)』
# 『夏農信道編碼定理』:如果信道的傳輸速率𝑅，R 小於信道容量 𝐶，那麼可以設計一種編碼，使得錯誤率可以逼近 0。
# 夏農-哈特利定理 : 在有限頻寬與有限噪音下，信道能傳輸的最高資料量是有限的

