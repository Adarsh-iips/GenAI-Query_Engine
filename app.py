from fastapi import FastAPI, Request, HTTPException, Header
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

API_KEY = "my-secret-key"

# Simulated in-memory mock data
mock_data = {
    "sales": [
        {"quarter": "Q4", "revenue": 1200000},
    ],
    "customers": [
        {"name": "Alice", "total_spent": 5000},
        {"name": "Bob", "total_spent": 4000},
        {"name": "Charlie", "total_spent": 3000},
    ]
}

class QueryRequest(BaseModel):
    query: str

def authenticate(x_api_key: str):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Gen AI Query Engine!"}

@app.post("/query")
async def process_query(request: QueryRequest, x_api_key: Optional[str] = Header(None)):
    authenticate(x_api_key)
    query = request.query.lower()

    if "sales revenue" in query and "last quarter" in query:
        return {
            "sql": "SELECT SUM(revenue) FROM sales WHERE quarter = 'Q4';",
            "result": "$1,200,000"
        }
    elif "top customers" in query:
        return {
            "sql": "SELECT name, total_spent FROM customers ORDER BY total_spent DESC LIMIT 10;",
            "result": mock_data["customers"]
        }
    return {"sql": "SELECT * FROM data;", "result": "Simulated result."}

@app.post("/explain")
async def explain_query(request: QueryRequest, x_api_key: Optional[str] = Header(None)):
    authenticate(x_api_key)
    query = request.query.lower()

    if "top customers" in query:
        return {"pseudo_sql": "SELECT name, total_spent FROM customers ORDER BY total_spent DESC LIMIT 10;"}
    elif "sales revenue" in query:
        return {"pseudo_sql": "SELECT SUM(revenue) FROM sales WHERE quarter = 'Q4';"}
    return {"pseudo_sql": "SELECT * FROM data;"}

@app.post("/validate")
async def validate_query(request: QueryRequest, x_api_key: Optional[str] = Header(None)):
    authenticate(x_api_key)
    query = request.query.lower()

    if any(keyword in query for keyword in ["sales", "customers", "products"]):
        return {"valid": True, "message": "Query is feasible."}
    return {"valid": False, "message": "Query is not recognized."}

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(status_code=exc.status_code, content={"error": exc.detail})
