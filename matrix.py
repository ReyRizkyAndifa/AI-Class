# Rey Rizky Andifa_F55123079


import numpy as np
A = np.array([[3, 0], [1, -2], [1, 1]])
B = np.array([[4, -1], [0, 2]])
C = np.array([[1, 4, 2], [3, 1, 5]])
D = np.array([[1, 5, 2], [-1, 0, 1], [3, 2, 4]])
E = np.array([[6, 1, 3], [-1, 2, 2], [4, 1, 3]])


def multiply_matrices(X, Y):
    result = np.zeros((X.shape[0], Y.shape[1]))  #
    for i in range(X.shape[0]): 
        for j in range(Y.shape[1]):  
            for k in range(Y.shape[0]):  
                result[i, j] += X[i, k] * Y[k, j]
    return result


def add_matrices(X, Y):
    result = np.zeros(X.shape) 
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            result[i, j] = X[i, j] + Y[i, j]
    return result

# Fungsi untuk mengurangkan matriks menggunakan perulangan for
def subtract_matrices(X, Y):
    result = np.zeros(X.shape) 
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            result[i, j] = X[i, j] - Y[i, j]
    return result

# Perkalian A x C
try:
    AC = multiply_matrices(A, C)
    print("Hasil A x C:")
    for row in AC:
        print(row)
except ValueError as e:
    print("Error saat menghitung A x C:", e)

# Perkalian A x D
try:
    AD = multiply_matrices(A, D)
    print("\nHasil A x D:")
    for row in AD:
        print(row)
except ValueError as e:
    print("\nError saat menghitung A x D:", e)

# Penjumlahan D + E
try:
    DE_add = add_matrices(D, E)
    print("\nHasil D + E:")
    for row in DE_add:
        print(row)
except ValueError as e:
    print("\nError saat menghitung D + E:", e)

# Pengurangan D - E
try:
    DE_sub = subtract_matrices(D, E)
    print("\nHasil D - E:")
    for row in DE_sub:
        print(row)
except ValueError as e:
    print("\nError saat menghitung D - E:", e)

# Yang menggunakan Non Library
A = [
    [3, 0],
    [-1, 2],
    [1, 1]
]

B = [
    [4, -1],
    [0, 2]
]

C = [
    [1, 4, 2],
    [3, 1, 5],
]

D = [
    [1, 5, 2],
    [-1, 0, 1],
    [3, 2, 4]
]

E = [
    [6, 1, 3],
    [-1, 1, 2],
    [4, 1, 3]
]

# Fungsi untuk melakukan perkalian matriks
def multiply_matrices(X, Y):
    result = [[0 for _ in range(len(Y[0]))] for _ in range(len(X))]  
    for i in range(len(X)):  
        for j in range(len(Y[0])):  
            for k in range(len(Y)):  
                result[i][j] += X[i][k] * Y[k][j]
    return result

# Fungsi untuk menjumlahkan matriks
def add_matrices(X, Y):
    result = [[0 for _ in range(len(X[0]))] for _ in range(len(X))]  
    for i in range(len(X)):
        for j in range(len(X[0])):
            result[i][j] = X[i][j] + Y[i][j]
    return result

# Fungsi untuk mengurangkan matriks
def subtract_matrices(X, Y):
    result = [[0 for _ in range(len(X[0]))] for _ in range(len(X))]  
    for i in range(len(X)):
        for j in range(len(X[0])):
            result[i][j] = X[i][j] - Y[i][j]
    return result

# Perkalian matriks A dan C
AC = multiply_matrices(A, C)
print("Hasil perkalian matriks A dan C:")
for row in AC:
    print(row)

# Perkalian matriks A dan D
AD = multiply_matrices(A, D)
print("\nHasil perkalian matriks A dan D:")
for row in AD:
    print(row)

# Penjumlahan matriks D dan E
D_plus_E = add_matrices(D, E)
print("\nHasil penjumlahan matriks D dan E:")
for row in D_plus_E:
    print(row)

# Pengurangan matriks D dan E
D_minus_E = subtract_matrices(D, E)
print("\nHasil pengurangan matriks D dan E:")
for row in D_minus_E:
    print(row)