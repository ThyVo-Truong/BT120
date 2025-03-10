import numpy as np

# Tạo ngẫu nhiên một ma trận có N dòng và M cột với các giá trị từ -100 tới 100
N, M = 3, 3  # Thay đổi N và M tùy theo nhu cầu
A = np.random.randint(-100, 100, size=(N, M))

print("Ma trận gốc:")
print(A)

# (1) Tính định thức ma trận
if N == M:
    det_A = np.linalg.det(A)
    print("\nĐịnh thức của ma trận A:")
    print(det_A)
else:
    print("\nKhông xác định định thức cho ma trận không vuông.")

# (2) Tìm ma trận nghịch đảo
if N == M:
    inv_A = np.linalg.inv(A)
    print("\nMa trận nghịch đảo của A:")
    print(inv_A)
else:
    print("\nKhông xác định nghịch đảo cho ma trận không vuông.")

# (3) Sắp xếp ma trận theo hàng
sorted_by_row = np.sort(A, axis=1)
print("\nMa trận sắp xếp theo hàng:")
print(sorted_by_row)

# (4) Sắp xếp ma trận theo cột
sorted_by_col = np.sort(A, axis=0)
print("\nMa trận sắp xếp theo cột:")
print(sorted_by_col)

# (5) Sắp xếp ma trận theo giá trị trung bình của từng hàng
sorted_by_row_mean = A[np.argsort(A.mean(axis=1))]
print("\nMa trận sắp xếp theo giá trị trung bình của từng hàng:")
print(sorted_by_row_mean)

# (6) Thay đổi giá trị của một phần tử trong ma trận
row, col, new_value = 1, 1, 50  # Thay đổi theo nhu cầu
A[row, col] = new_value
print("\nMa trận sau khi thay đổi một phần tử:")
print(A)

# (7) Thay đổi giá trị một cột của ma trận theo điều kiện
column_to_change = 1  # Thay đổi vị trí cột theo nhu cầu
A[:, column_to_change] += 2
print("\nMa trận sau khi thay đổi giá trị của một cột:")
print(A)

# (8) Cộng thêm một vector vào từng hàng của ma trận
vector_to_add = np.random.randint(-10, 10, size=M)
A_plus_vector = A + vector_to_add
print("\nMa trận sau khi cộng thêm một vector vào từng hàng:")
print(A_plus_vector)

# (9) Tính hạng của ma trận
rank_A = np.linalg.matrix_rank(A)
print("\nHạng của ma trận:")
print(rank_A)

# (10) Tính phân tích Singular Value Decomposition (SVD)
U, S, Vt = np.linalg.svd(A)
print("\nPhân tích Singular Value Decomposition (SVD):")
print("Ma trận U:")
print(U)
print("Giá trị đặc trưng (S):")
print(S)
print("Ma trận Vt:")
print(Vt)
