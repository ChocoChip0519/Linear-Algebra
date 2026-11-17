import numpy as np

np.set_printoptions(precision=4, suppress=True)

# ---------------------------------------------------------
# 실습 7-1: 특성다항식과 고유값
# MATLAB: A=[2, 3; 3, -6];  poly(A)  eig(A)
# ---------------------------------------------------------
print("=== 실습 7-1 ===")
A = np.array([[2, 3],
              [3, -6]])

print("poly(A) =")
print(np.poly(A))          # 특성다항식 계수 [1, 4, -21] -> λ^2 + 4λ - 21

print("eig(A) =")
print(np.real_if_close(np.linalg.eigvals(A)))  # 고유값 3, -7

# ---------------------------------------------------------
# 실습 7-2: 고유값과 고유벡터
# MATLAB: A=[3, 2; 3, -2];  [X, lamda] = eig(A)
# ---------------------------------------------------------
print("\n=== 실습 7-2 ===")
A = np.array([[3, 2],
              [3, -2]])

w, X = np.linalg.eig(A)
w, X = np.real_if_close(w), np.real_if_close(X)  # 허수부가 0이면 실수로
lamda = np.diag(w)         # MATLAB처럼 고유값을 대각행렬로

print("X =")
print(X)
print("lamda =")
print(lamda)

# ---------------------------------------------------------
# 실습 7-3: 고유값과 고유벡터
# MATLAB: A=[3, -1, -1; -12, 0, 5; 4, -2, -1];  [X, lamda] = eig(A)
# ---------------------------------------------------------
print("\n=== 실습 7-3 ===")
A = np.array([[3, -1, -1],
              [-12, 0, 5],
              [4, -2, -1]])

w, X = np.linalg.eig(A)
w, X = np.real_if_close(w), np.real_if_close(X)  # 허수부가 0이면 실수로
lamda = np.diag(w)

print("X =")
print(X)
print("lamda =")
print(lamda)

# ---------------------------------------------------------
# 실습 7-4: 삼각행렬의 고유값 (주대각선의 값)
# (1) MATLAB: A=[0, 0, 0; 0, 2, 5; 0, 0, -1];  eig(A)   -> 상부삼각행렬
# (2) MATLAB: A=[4, 0, 0; 0, 0, 0; 1, 0, -3];  eig(A)   -> 하부삼각행렬
# ---------------------------------------------------------
print("\n=== 실습 7-4 ===")
A = np.array([[0, 0, 0],
              [0, 2, 5],
              [0, 0, -1]])
print("(1) eig(A) =")
print(np.real_if_close(np.linalg.eigvals(A)))

B = np.array([[4, 0, 0],
              [0, 0, 0],
              [1, 0, -3]])
print("(2) eig(B) =")
print(np.real_if_close(np.linalg.eigvals(B)))