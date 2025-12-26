#DFT
import math

def dft(f):
    N = len(f)
    F = []

    for k in range(N):
        real = 0.0
        imag = 0.0
        for n in range(N):
            angle = -2 * math.pi * k * n / N
            real += f[n] * math.cos(angle)
            imag += f[n] * math.sin(angle)
        F.append((real, imag))  # 用 (real, imag) 表示複數

    return F

#IDFT
def idft(F):
    N = len(F)
    f = []

    for n in range(N):
        real = 0.0
        for k in range(N):
            angle = 2 * math.pi * k * n / N
            real += (
                F[k][0] * math.cos(angle)
                - F[k][1] * math.sin(angle)
            )
        f.append(real / N)

    return f

#證：DFT → IDFT → 原函數
F = dft(f)
f_reconstructed = idft(F)

print("原始 f:")
print(f)

print("\nDFT F (real, imag):")
for x in F:
    print(x)

print("\nIDFT 還原後的 f:")
for x in f_reconstructed:
    print(round(x, 6))

