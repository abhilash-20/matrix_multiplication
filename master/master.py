import numpy as np
import requests

# Generate two 10x10 matrices
A = np.random.randint(1, 10, (10, 10))
B = np.random.randint(1, 10, (10, 10))

# Split matrix A into 2 parts (horizontal split)
A1 = A[:5, :]
A2 = A[5:, :]

# Send A1 to worker 1
response1 = requests.post("https://worker1.onrender.com/multiply", json={
    "A_part": A1.tolist(),
    "B": B.tolist()
})
C1 = response1.json()["C_part"]

# Send A2 to worker 2
response2 = requests.post("https://worker2.onrender.com/multiply", json={
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
