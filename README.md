有ChatGPT網址的，代表使用AI生成，自己有嘗試看懂
# HW1
HW!: https://github.com/kz-17/CM/blob/main/HW1
1. 自創
2. 使用Sympy模組
- f(x) = x的三次方
- diff(): 計算f的微分
- integral(): 計算a=0、b=3中，f的定積分

# HW2
HW2:https://github.com/kz-17/CM/tree/main/HW2
1. 自創
2. 使用公式解解出兩根
 - f(x) = x**2+x+1 => 複數解
- f(x) = x**2+2*x+1 => 重根
- f(x) = x**2-2*x-3 => 異解 先使用root2()求出兩解，再判斷是否相似，最後帶回去查看f(x)是否為0
3. Outputs:
- eq1 root: ((-0.5+0.8660254037844386j), (-0.5-0.8660254037844386j)) False (1.1102230246251565e-16+0j) (1.1102230246251565e-16+0j)
- eq2 root: ((-1+0j), (-1+0j)) True 0j 0j
- eq2 root: ((3+0j), (-1+0j)) False 0j 0j
# HW4
HW4:https://github.com/kz-17/CM/tree/main/HW4  
ChatGPT : https://chatgpt.com/share/694f4f8e-0dbc-8012-995e-a888b68304db
Durand–Kerner method（Weierstrass method）
image
1. 一種數值演算法，用來同時逼近多項式的所有根（包含複數根），透過迭代公式逐步收斂到正確解
2. 每次更新時，分母是「與其他近似根的距離乘積」，避免不同根收斂到同一點
3. 經過多次迭代後，所有xi都會收斂到真實根 (使用ChatGPT)
# HW5
HW5:https://github.com/kz-17/CM/tree/main/HW5
GhatGPT:https://chatgpt.com/share/690d8c47-dde4-8012-896b-ae29115c3a2a
## 有限體
### 概念
體(Field):一種代數結構，具備加法與乘法，並且這兩種運算都滿足交換律、結合律、分配律，且每個非零元素都有乘法反元素 ###特性
1.若一個有限體有 q 個元素，則 q=p^n，其中 p 是質數，n 是正整數，ex.GF(5) = {0, 1, 2, 3, 4}
2. 除了 0 以外的元素可以由某個元素（稱為原根）的冪生成
3. 對於每個 p^n，在同構意義下，只有一個有限體 GF(p^n) 
# HW6
HW6:https://github.com/kz-17/CM/tree/main/HW6
ChatGPT:https://chatgpt.com/share/694f5066-6d68-8012-9da5-855bcb83d458  
1. 直線交點:解二元一次方程組 → 線性代數的克拉瑪法則
2.  圓交點:從幾何出發，兩圓的交點在「兩圓中心連線的垂直平分線附近」，推導使用向量、勾股定理。 其實是一個幾何版的「解二元二次方程」。
3. 線與圓交點:線 → 參數式 代入圓 → 得一元二次方程 使用判別式判斷是否相交。
4. 垂足:垂足是在直線上，且點向量到垂足向量與直線方向向量正交。 用投影公式可直接求出
5. 變換（平移、縮放、旋轉） 線性代數與仿射變換（affine transform）：平移＝向量加法、縮放＝對座標分量乘常數、旋轉＝套用 旋轉矩陣
- 所有幾何物件都可用矩陣乘法處理
# HW8
HW8 : https://github.com/kz-17/CM/tree/main/HW8  
ChatGPT : https://chatgpt.com/share/692bbaad-b104-8012-bb90-fcb6348ebf7e  
1.計算公平銅板連續投擲 10000 次全部正面機率，機率會趨近於0
2.用 log(p^n) = n log(p) 計算 log(p^n)，然後代入 p=0.5，算出 log(0.5^10000)
理論上 : log(0.5^10000) = 10000 log(0.5) 實際上 : 0.5^10000會趨近於0，使用math.log(0.5^10000)會變成math.log(0)，因為定義域為大於0，所以報錯
3.『熵，交叉熵，KL 散度，互熵（互資訊）』
H(p)=−i∑​pi​logpi​H(p,q)=−i∑​pi​logqi​DKL​(p∥q)=i∑​pi​logqi​pi​​I(X;Y)=H(X)−H(X∣Y)
4.驗證 cross_entropy(p,p) > cross_entropy(p,q), 當 q != p 時
理論上 : H(p,p)≤H(p,q) <=> p=q
5. 7-4 漢明碼（Hamming (7,4)）編碼與解碼
Hamming(7,4) 將 4 位資料編成 7 位，使單一錯誤可糾正
6. 『夏農信道編碼定理』和『夏農-哈特利定理 (Shannon–Hartley Theorem)』
『夏農信道編碼定理』: 無雜訊傳輸在理論上是可能的，但必須使用足夠長且複雜的編碼 『夏農-哈特利定理 (Shannon–Hartley Theorem)』:傳輸速率受頻寬與訊噪比限制，提升其中任一項可提升最大通訊速
# HW9
HW9 : https://github.com/kz-17/CM/tree/main/HW9
(原創，對於上學期線性代數的印象)
  1.線性代數中的『線性』指的是什麼？為何要稱為『代數』
答:
滿足以下兩條件：
對任意向量 u, v 和任意實數（或複數） a, b：T(au+bv)=aT(u)+bT(v)
把所有頻率的旋轉圓，依照它們的權重 F[k]，全部加回來

可加性：T(u+v)=T(u)+T(v)
齊次性：T(αu)=αT(u) 代數指研究一組帶有運算規則的元素的結構
2.數學中的『空間』是什麼？為何『向量空間』被稱為空間
答:
現代數學中，「空間」= 一個集合 + 結構
向量空間:滿足「加減、伸縮」的幾何直覺

3.矩陣和向量之間有何關係？矩陣代表的意義是什麼？
答:
矩陣 = 線性變換的座標表示 向量 → 一個空間的元素 矩陣 → 把向量變成另一個向量的「線性規則」

4.如何用矩陣代表 2D / 3D 幾何學中的『平移，縮放，旋轉』操作？
答:
2D 平移矩陣:
1 0 dx
0 1 dy
0 0 1
2D 縮放:
sx 0 0
0 sy 0
0 0 1
2D 旋轉矩陣:
cosθ -sinθ 0
sinθ cosθ 0
0 0 1

5.行列式的意義是什麼？如何用遞迴公式計算矩陣的行列式？行列式和體積有什麼關係？
答:
行列式 = 空間被矩陣拉伸的「體積倍數」

A=PDP−1
A=LU，det(A)=det(L)det(U)
6.特徵值和特徵向量的意義是什麼？特徵值分解有何用途？
答:
Av=λv
矩陣 A 的作用在向量 v 上，不會改變方向、只會「伸縮」 λ 倍

7.QR 分解是什麼？
答:
A=QR:Q：正交矩陣（旋轉）、R：上三角矩陣（縮放 + 斜率）

8.如何反覆用 QR 分解，完成特徵值分解？
答:
Ak+1​=Rk​Q，會使 A 趨近於上三角矩陣，其對角線即特徵值。

9.SVD 分解是什麼？和特徵值分解有何關係？
答:
A=UΣVT
V：在輸入空間中找出最佳方向
Σ：沿這些方向的伸縮量（奇異值）
U：伸縮後的方向


# HW10
HW10:https://github.com/kz-17/CM/tree/main/HW10  
ChatGPT:https://chatgpt.com/share/694e3c7e-ac28-8012-a5ed-4937ada898af
1. DHT
把「時間（或空間）上的訊號 f[n]」，拆成「各種不同頻率的旋轉圓（複數指數）」的加權和
2. IDFT

# HW11
HW11:https://github.com/kz-17/CM/tree/main/HW11
ChatGPT:https://chatgpt.com/share/694e3f96-809c-8012-9285-05144b73e3e0
- 建立特徵方程、求根、分類根、組合通解

10.主成分分析是什麼？和 SVD 分解有何關係？
答:
PCA = covariance matrix 的 SVD
