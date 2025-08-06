from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np

app = FastAPI()

class MatrixMul(BaseModel):
    A_part: list
    B: list

@app.post("/multiply")
def multiply(data: MatrixMul):
    A = np.array(data.A_part)
    B = np.array(data.B)
    C_part = np.dot(A, B)
    return {"C_part": C_part.tolist()}
