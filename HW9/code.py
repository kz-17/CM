#遞迴行列式
def det_recursive(A):
    n = len(A)
    if n == 1:
        return A[0][0]
    if n == 2:
        return A[0][0]*A[1][1] - A[0][1]*A[1][0]

    total = 0
    for j in range(n):
        minor = [row[:j] + row[j+1:] for row in A[1:]]
        total += ((-1)**j) * A[0][j] * det_recursive(minor)
    return total

#LU 分解 + 行列式
import numpy as np

def lu_decomposition(A):
    A = A.astype(float)
    n = A.shape[0]
    L = np.eye(n)
    U = A.copy()

    for i in range(n):
        for j in range(i+1, n):
            factor = U[j,i]/U[i,i]
            L[j,i] = factor
            U[j] -= factor * U[i]
    return L, U

def det_lu(A):
    L, U = lu_decomposition(A)
    return np.prod(np.diag(U))

#驗證 LU、Eigen、SVD
A = np.random.randn(4,4)

# LU
L, U = lu_decomposition(A)
print(np.allclose(L @ U, A))

# Eigen
eigvals, P = np.linalg.eig(A)
D = np.diag(eigvals)
print(np.allclose(P @ D @ np.linalg.inv(P), A))

# SVD
U, S, Vt = np.linalg.svd(A)
Sigma = np.zeros_like(A)
np.fill_diagonal(Sigma, S)
print(np.allclose(U @ Sigma @ Vt, A))

#用 Eigen 做 SVD
def svd_from_eigen(A):
    AtA = A.T @ A
    eigvals, V = np.linalg.eig(AtA)
    idx = np.argsort(-eigvals)
    eigvals = eigvals[idx]
    V = V[:, idx]

    S = np.sqrt(eigvals)
    U = A @ V / S
    return U, S, V.T

#PCA 主成份分析
def pca(X, k):
    X = X - np.mean(X, axis=0)
    C = X.T @ X / (len(X)-1)
    eigvals, eigvecs = np.linalg.eig(C)

    idx = np.argsort(-eigvals)
    eigvecs = eigvecs[:, idx]
    eigvals = eigvals[idx]

    W = eigvecs[:, :k]
    Z = X @ W
    return Z, W, eigvals[:k]

