1. 計算公平銅板連續投擲 10000 次全部正面機率
   機率會趨近於0
2. 用 log(p^n) = n log(p) 計算 log(p^n)，然後代入 p=0.5，算出 log(0.5^10000)
   理論上 : log(0.5^10000) = 10000 log(0.5)
   實際上 :  0.5^10000會趨近於0，使用math.log(0.5^10000)會變成math.log(0)，因為定義域為大於0，所以報錯
3. 『熵，交叉熵，KL 散度，互熵（互資訊）』
   H(p)=−i∑​pi​logpi​
   H(p,q)=−i∑​pi​logqi​
   DKL​(p∥q)=i∑​pi​logqi​pi​​
   I(X;Y)=H(X)−H(X∣Y)
4. 驗證 cross_entropy(p,p) > cross_entropy(p,q), 當 q != p 時
     理論上 : H(p,p)≤H(p,q) <=> p=q
5. 7-4 漢明碼（Hamming (7,4)）編碼與解碼
   Hamming(7,4) 將 4 位資料編成 7 位，使單一錯誤可糾正
6. 『夏農信道編碼定理』和『夏農-哈特利定理 (Shannon–Hartley Theorem)』
   『夏農信道編碼定理』: 無雜訊傳輸在理論上是可能的，但必須使用足夠長且複雜的編碼
  『夏農-哈特利定理 (Shannon–Hartley Theorem)』:傳輸速率受頻寬與訊噪比限制，提升其中任一項可提升最大通訊速率
