----->URL: https://genai-queryengine-production.up.railway.app<--------
Gen AI Query Engine - FastAPI Backend
A lightweight backend simulation of a Gen AI-powered analytics tool that allows users to input natural language queries and receive pseudo-SQL translations and simulated insights. Built using FastAPI and in-memory mock data. 
1. Accepts natural language queries
2. Converts queries to pseudo-SQL
3. Returns mock analytics data
4. Simulates query breakdown and validation
5. Basic API Key authentication
6. Includes OpenAPI (Swagger) documentation
   
Setup Instructions:
1. Clone the Repository:
git clone https://github.com/Adarsh-iips/GenAI-Query_Engine.git
cd genai_query_engine
2. (Optional) Create Virtual Environment:
python -m venv venv
venv\Scripts\activate  # On Windows
3. Install Dependencies:
pip install -r requirements.txt
4. Run the Server:
uvicorn app:app --reload
The API will now be running at:
http://127.0.0.1:8000
5. View Swagger UI Docs:
Visit-
http://127.0.0.1:8000/docs

API Key Authentication:
All endpoints require a header: X-API-Key: my-secret-key

API Documentation
POST /query
Simulates processing of a natural language query.
Request Body:
{
  "query": "Show me top customers"
}

**Response:**
```json
{
  "sql": "SELECT name, total_spent FROM customers ORDER BY total_spent DESC LIMIT 10;",
  "result": [
    {"name": "Alice", "total_spent": 5000},
    {"name": "Bob", "total_spent": 4000},
    {"name": "Charlie", "total_spent": 3000}
  ]
}

---

### `POST /explain`
Returns a breakdown of the pseudo-SQL query.

**Request Body:**
```json
{
  "query": "What is the sales revenue last quarter"
}

**Response:**
```json
{
  "pseudo_sql": "SELECT SUM(revenue) FROM sales WHERE quarter = 'Q4';"
}

---

### `POST /validate`
Checks if the query is feasible.

**Request Body:**
```json
{
  "query": "List sales data"
}

**Response:**
```json
{
  "valid": true,
  "message": "Query is feasible."
}

---

##  Sample Queries

| Natural Language Query                    | Simulated SQL                                                                 |
|------------------------------------------|-------------------------------------------------------------------------------|
| Show me top customers                    | SELECT name, total_spent FROM customers ORDER BY total_spent DESC LIMIT 10;  |
| What is the sales revenue last quarter   | SELECT SUM(revenue) FROM sales WHERE quarter = 'Q4';                         |
| Anything else                            | SELECT * FROM data; (default fallback)                                       |

---

**** Make sure to:
- Set your `Start command` to: `uvicorn app:app --host 0.0.0.0 --port $PORT`
- Add `API_KEY` in environment variables (optional)

## Contact
Built by Adarsh Sharma. Reach out for questions or feedback!

For testing:
Use curl Commands in Command Prompt

1. /query
curl -X POST https://genai-queryengine-production.up.railway.app/query ^
 -H "Content-Type: application/json" ^
 -H "X-API-Key: my-secret-key" ^
 -d "{\"query\":\"Show me top customers\"}"

2. /explain
curl -X POST https://genai-queryengine-production.up.railway.app/explain ^
 -H "Content-Type: application/json" ^
 -H "X-API-Key: my-secret-key" ^
 -d "{\"query\":\"What is the sales revenue last quarter\"}"

3. /validate
curl -X POST https://genai-queryengine-production.up.railway.app/validate ^
 -H "Content-Type: application/json" ^
 -H "X-API-Key: my-secret-key" ^
 -d "{\"query\":\"List sales data\"}"
