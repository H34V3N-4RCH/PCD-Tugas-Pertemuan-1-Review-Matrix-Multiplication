"""
Nama: Ridho Ahmad Irawan
NIM: F1G124049
Kelas: A
Mata Kuliah: Pengolahan Citra Digital
Tugas: 1
"""

import numpy as np

# Definisi matriks 3D dengan ordo 3x3
A = np.array([
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ],
    [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]
])

B = np.array([
    [
        [1, 3, 5],
        [7, 9, 1],
        [3, 5, 7]
    ],
    [
        [2, 4, 6],
        [8, 2, 4],
        [6, 8, 2]
    ]
])

C = A @ B

print("\nPROSES PER LEMBAR")
print("Lembar 1 (A[0] @ B[0]):")
print(C[0])

print("\nLembar 2 (A[1] @ B[1]):")
print(C[1])

print("\nHASIL LENGKAP ARRAY 3D")
print(C)