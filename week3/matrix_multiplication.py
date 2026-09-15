A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

B = [
    [1, 2],
    [3, 4],
    [5, 6]
]

row_a = len(A) # A와 행 개수 :4
clos_a = len(A[0]) # A의 열 개수 : 3
row_b = len(B) # B의 행 개수 : 3
clos_b = len(B[0]) # B의 열 개수 : 2

# 행렬 곱셈 가능 여부 확인
if clos_a != row_b:
    raise ValueError("A의 열 개수와 B의 행 개수가 같아야 합니다.")

#결과 행렬 C: 4행 2열, 모든 원소를 0으로 초기화
C = [[0 for _ in range(clos_b)] for _ in range(row_a)]

# 행렬 곱셈 수행
for i in range(row_a): # A의 행 인덱스
    for j in range(clos_b): # B의 열 인덱스
        for k in range(clos_a): # A의 열 인덱스 또는 B의 행 인덱스
            C[i][j] += A[i][k] * B[k][j]

print("A * B =")
for row in C:
    print(row)