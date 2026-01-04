import numpy as np

A = np.array([[3, 2, 1, 4],
              [5, 2, 1, 6]])

B = np.array([[3, 2, 1, 4],
              [5, 2, 0, 6]])

C = np.array([[True, False, False],
              [True, True, True]])

lista = [A, B, C]
nazwy = ["A", "B", "C"]

print(f"czy wszystkie sa rowne w wymiarze=1?")
for nazwa, matrix in zip(nazwy, lista):
    print(f"{nazwa}: {np.all(matrix, axis=1)}")

A = np.array([[0, 0, 0],
              [0, 0, 0]])

B = np.array([[0, 0, 0],
              [0, 1, 0]])

C = np.array([[False, False, False],
              [True, False, False]])

D = np.array([[0.1, 0.0]])

lista = [A, B, C, D]
nazwy = ["A", "B", "C", "D"]

print("czy sa jakie kolwiek True/!=0 w wymiarze=0?")
for nazwa, matrix in zip(nazwy, lista):
    print(f"{nazwa}: {np.any(matrix, axis=0)}")

A = np.array([[3, 2, 1, np.nan],
              [5, np.nan, 1, 6]])

print(f"czy sa wartosci puste?: {np.isnan(A)}")

import numpy as np

A = np.array([0.4, 0.5, 0.3])
B = np.array([0.39999999, 0.5000001, 0.3])

print(f"czy sa na oko rowne?: {np.allclose(A, B)}")
print(f"czy sa rowne indeksami?: {A == B}")

A = np.array([0.4, 0.5, 0.3, 0.9])
B = np.array([0.38, 0.51, 0.3, 0.91])

print(f"czy liczby idx A sa wieksze od liczb idx B?: {A > B}")
print(f"to to samo tylko funkcja: {np.greater(A, B)}")

print(np.zeros((4,4), dtype=int))

print(f"{np.full((10, 10), 255, int)}")

matrix_of_ones = np.ones((10, 10), int)
print(matrix_of_ones * 255)

matrix = np.arange(10, 100, 1, int)
new_matrix = np.ndarray.reshape(matrix, 9, 10)
print(new_matrix)

print(np.eye(6, 6, 0, ))

np.random.seed(10)
print(np.random.rand(30))


np.random.seed(10)
matrix = np.random.randn(40)
matrix = np.ndarray.reshape(matrix, 10, 4)
print(matrix)