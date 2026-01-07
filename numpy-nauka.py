import numpy as np
from numba import njit

@njit
def fast_sum_logic(matrix, threshold):
    count = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if matrix[i, j] > threshold:
                count += 1
    return count

see_njit = False

if see_njit:
    test_m = np.random.randint(0, 10, (100, 100))
    print(f"Liczba pikseli > 5 (Numba): {fast_sum_logic(test_m, 5)}")

    print(fast_sum_logic.inspect_asm(fast_sum_logic.signatures[0]))


A = np.array([[3, 2, 1, 4],
              [5, 2, 1, 6]])

B = np.array([[3, 2, 1, 4],
              [5, 2, 0, 6]])

C = np.array([[True, False, False],
              [True, True, True]])

lista = [A, B, C]
nazwy = ["A", "B", "C"]

print("czy wszystkie sa rowne w wymiarze=1?")
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

print(np.random.rand(30))

res_numpy = np.random.normal(loc=100, scale=np.sqrt(5), size=(10, 4))
print(res_numpy)

A = np.array([[1, 4, 3],
              [5, 2, 6]])

for el in np.nditer(A):
    print(el)

print(np.linspace(0, 1, 11))

rng = np.random.default_rng(seed=42)
pula = np.arange(1, 50)
numbers = rng.choice(pula, 5, replace=False)
print(numbers)

np.random.seed(42)
pula = np.arange(1, 50)
numbers = np.random.choice(pula, 6, replace=False)
print(numbers)
import numpy as np
x = np.arange(6)
print(np.diag(x))


x = np.arange(12)
x = np.ndarray.reshape(x, (3, 4))
np.save("array.npy", x)
plik = np.load("array.npy")
print(plik)

x = np.arange(12, dtype=int)
x = np.ndarray.reshape(x, (-1, 4))
np.savetxt('array.txt', X=x, fmt="%0.2f")
y = np.loadtxt('array.txt').astype(int)
print(y)

import numpy as np
x = np.arange(12, dtype=int)
x = x.reshape((-1, 4))
x = x.tolist()
print(x)

import numpy as np
x = np.arange(12, dtype=int)
x = x.reshape((-1, 4))
x = x[::-1]
print(x)

matrix = np.ones((4, 4), dtype=float)

A = np.pad(matrix, 1)
height, width = (1, 2), (3, 4)

B = np.pad(matrix, 2, constant_values=3)

C = np.pad(matrix, (height, width))

print(f"{A}\n{B}\n{C}")
print("\n\n\n")
A = np.zeros((6, 6))
view = A.reshape(3, 2, 3, 2)
print(view)
view[:, 0, :, 0] = 10
view[:, 1, :, 0] = 5
print(f"{A}\n\n")

hightmany, hightlen, widthmany, widthlen = (2, 5, 5, 2)
A = np.zeros((10, 10))
view = A.reshape(hightmany, hightlen, widthmany, widthlen)
view[:, 0, 0, 0] = 5
print(A)