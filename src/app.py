from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/add/")
async def add(a: float, b: float):
    return {"result": a + b}

@app.get("/subtract/")
async def subtract(a: float, b: float):
    return {"result": a - b}

@app.get("/multiply/")
async def multiply(a: float, b: float):
    return {"result": a * b}

@app.get("/divide/")
async def divide(a: float, b: float):
    if b == 0:
        raise HTTPException(status_code=400, detail="Division by zero is not allowed.")
    return {"result": a / b}