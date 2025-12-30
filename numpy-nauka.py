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