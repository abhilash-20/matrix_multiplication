import numpy as np
import requests

# Generate two 10x10 matrices
A = np.array([
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [2, 3, 4, 5, 6, 7, 8, 9, 10, 1],
    [3, 4, 5, 6, 7, 8, 9, 10, 1, 2],
    [4, 5, 6, 7, 8, 9, 10, 1, 2, 3],
    [5, 6, 7, 8, 9, 10, 1, 2, 3, 4],
    [6, 7, 8, 9, 10, 1, 2, 3, 4, 5],
    [7, 8, 9, 10, 1, 2, 3, 4, 5, 6],
    [8, 9, 10, 1, 2, 3, 4, 5, 6, 7],
    [9, 10, 1, 2, 3, 4, 5, 6, 7, 8],
    [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
])

B = np.array([
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
    [9, 8, 7, 6, 5, 4, 3, 2, 1, 10],
    [8, 7, 6, 5, 4, 3, 2, 1, 10, 9],
    [7, 6, 5, 4, 3, 2, 1, 10, 9, 8],
    [6, 5, 4, 3, 2, 1, 10, 9, 8, 7],
    [5, 4, 3, 2, 1, 10, 9, 8, 7, 6],
    [4, 3, 2, 1, 10, 9, 8, 7, 6, 5],
    [3, 2, 1, 10, 9, 8, 7, 6, 5, 4],
    [2, 1, 10, 9, 8, 7, 6, 5, 4, 3],
    [1, 10, 9, 8, 7, 6, 5, 4, 3, 2]
])

# Split matrix A into 2 parts (horizontal split)
A1 = A[:5, :]
A2 = A[5:, :]

# Send A1 to worker 1
response1 = requests.post("https://worker-1-evjv.onrender.com/multiply", json={
    "A_part": A1.tolist(),
    "B": B.tolist()
})
C1 = response1.json()["C_part"]

# Send A2 to worker 2
response2 = requests.post("https://worker-2-jvt5.onrender.com/multiply", json={
    "A_part": A2.tolist(),
    "B": B.tolist()
})
C2 = response2.json()["C_part"]

# Combine results
C = np.vstack([C1, C2])

print("Matrix A:")
print(A)
print("\nMatrix B:")
print(B)
print("\nResult Matrix C (A x B):")
print(C)
