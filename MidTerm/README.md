# 簡介
- IMDB情緒分析資料集是NLP領域中的入門，從IMDB網站抽取的電影評論
- 以**正面(positive)**、**負面(negative)**方式標註
- 50000條電影評論，25000條用於訓練、驗證，25000條用於測試
- 資料來源:https://ai.stanford.edu/~amaas/data/sentiment/

1. 文字向量化 → 線性代數 + log
2. 分類模型 → 向量、矩陣、非線性函數
3. Loss → 資訊理論（熵、交叉熵、KL）
4. 訓練 → 微積分（梯度下降）
5.  評估 → 機率與統計
# 用到的數學
### 線性代數
詞嵌入（Embedding):詞 → 向量  
RNN / LSTM / GRU :hₜ​=tanh(wₕxₜ+Uₕ(rₜ⊙hₜ₋₁))  
全連接層:y=Wx+b  
### 非線性函數
Sigmoid : σ(x)=1/1+e^(-x)，最後二分類  
(原本就有在學Pytorch，所以對pytorch比較熟悉，所以用經典題目IMDB，有參考pytorch書籍)
