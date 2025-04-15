from fastapi import FastAPI, HTTPException

app = FastAPI(
    servers=[
        {"url": "http://127.0.0.1:8000", "description": "Production calculator environment"},
    ]
)

@app.get("/add", summary="Precisely adds two numbers together.", operation_id="add")
def add(a: float, b: float):
    return {"result": a + b}

@app.get("/subtract", summary="Precisely subtracts two numbers.", operation_id="subtract")
def subtract(a: float, b: float):
    return {"result": a - b}

@app.get("/multiply", summary="Precisely multiplies two numbers.", operation_id="multiply")
def multiply(a: float, b: float):
    return {"result": a * b}

@app.get("/divide", summary="Precisely divides two numbers.", operation_id="divide")
def divide(a: float, b: float):
    if b == 0:
        raise HTTPException(status_code=400, detail="Division by zero is not allowed")
    return {"result": a / b}