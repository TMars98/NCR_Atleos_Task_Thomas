import os 
import sqlite3

from fastapi import FastAPI, HTTPException

DB_PATH = os.environ.get("DB_PATH", "data/service_requests.db")

app = FastAPI(title="Service Request API")

def get_connection() -> sqlite3.Connection:
    connection = sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True)
    connection.row_factory = sqlite3.Row
    return connection

@app.get("/health")
def health() -> dict:
    connection = get_connection()
    try:
        connection.execute("SELECT 1")
    finally:
        connection.close()
    return {"status": "ok"}

@app.get("/service-requests/{request_id}")
def get_service_request(request_id: int) -> dict:
    connection = get_connection()
    try:
        row = connection.execute(
            "SELECT id, description, customer_name, customer_email, customer_phone "
            "FROM service_requests WHERE id = ?",
            (request_id,),
        ).fetchone()
    finally:
        connection.close()
    
    if row is None:
        raise HTTPException(status_code=404, detail="Service request not found")
    
    return dict(row)
    
    