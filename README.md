# NCR_Atleos_Task_Thomas

## What it does

-- Stores service requests (unique ID, description, customer details) in a local SQL database.
-- Expose a containerized API: given a service request ID, it returns that request as JSON.

## Stack

--**Python 3.13 / FastAPI** - the API, with automatic OpenAPI docs at '/docs'.
-- **SQLite** - the SQL database. A single file, no server to install.
-- **Docker / Docker Compose** - containerizes the API.

You need Docker installed. From the project root:

```bash
# 1. Build the database from the schema (creates data/service_requests.db)
sqlite3 data/service_requests.db < db/init.sql

# 2. Build and start the containerized API
docker compose up --build
```

Then, in another terminal:

```bash
curl localhost:8000/service-requests/1
```

Response:

```json
{
  "id": 1,
  "description": "Replace failed compressor on production line 3",
  "customer_name": "Acme Manufacturing",
  "customer_email": "ops@acme.example",
  "customer_phone": "+44 20 7946 0001"
}
```

# Interactive API docs are at http://localhost:8000/docs.


# Endpoints

Method, Path, Response

GET, /service-requests/{id}, 200 with the request as JSON, or 404

GET, /health, 200 {"status": "ok"} (checks the database)

A non-integer ID (e.g. /service-requests/abc) returns 422, rejected by validation before it reaches the database.

## Design decisions 

- **SQLite over a database server.** The brief allowed any SQL database and asked for it to run
  locally. SQLite gives a real relational store — schema, constraints, SQL — with nothing to
  install and no server to manage.
- **The database runs locally; only the API is containerized**, which is what the brief asks for.
  The database file is mounted into the container read-only.
- **A single flat table.** The brief describes a service request as *containing* customer details,
  so the customer fields live on the request itself.
- **Integer IDs**, kept simple so a request is easy to look up (`/service-requests/1`).
- **Parameterized queries** (`WHERE id = ?`) — the ID is never interpolated into the SQL string,
  so the endpoint is not vulnerable to SQL injection.

What I'd add next

- PostgreSQL with connection pooling and migrations for a real deployment.
- UUID identifiers.
- Automated tests in CI.

Project structure

app/main.py       the API (one file)
db/init.sql       schema + seed data
data/             the SQLite file lives here (generated, not committed)
Dockerfile        builds the API image
compose.yaml      runs the container