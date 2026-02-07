# Data Ingestion & Reporting Pipeline

A production-style backend system that ingests data from an external API, normalizes and stores it in a database, and exposes aggregated insights through REST APIs.

This project demonstrates how backend and data engineering systems collect external data, persist it reliably, and provide reporting endpoints for downstream consumption.


## Problem Statement

Organizations often rely on data from external systems (APIs) to generate insights and reports.  
This project simulates a real-world data pipeline that ingests external data, processes it, and exposes meaningful summaries through APIs.


## System Overview

The system follows a simple and reliable pipeline:<br>
External API → Data Ingestion → Data Transformation → Database → Reporting APIs


1. Data is fetched from an external public API  
2. Raw responses are normalized into a structured format  
3. Records are stored in a relational database  
4. Aggregated reports are exposed via REST APIs  


## Key Features

- Ingests data from an external API on demand
- Normalizes and persists structured records
- Stores time-series data in a relational database
- Exposes reporting APIs for aggregated insights
- Clean separation of ingestion, transformation, and reporting logic


## Architecture

Client<br>
↓<br>
Ingestion API (FastAPI)<br>
↓<br>
Fetch & Transform Layer<br>
↓<br>
Database (SQLite)<br>
↓<br>
Reporting APIs<br>


## API Screenshots

### Swagger API Overview
<img width="1920" height="989" alt="image" src="https://github.com/user-attachments/assets/9a8f0c6a-b4db-4177-96e2-bc6af41b16d3" />

### Reporting Summary
<img width="1920" height="2451" alt="image" src="https://github.com/user-attachments/assets/76129d45-0e8b-4a72-b69d-997a9e1eb5aa" />
<img width="1920" height="2559" alt="image" src="https://github.com/user-attachments/assets/1c7b66a6-eca4-4401-9426-0d41f084e946" />


## Tech Stack

- Python 3.10
- FastAPI
- SQLAlchemy
- SQLite
- Pandas
- Requests
- REST APIs


## API Overview

### Ingestion
- `POST /ingest/weather` – Fetches data from the external API and stores it

### Reports
- `GET /reports/summary` – Aggregated metrics (record count, average values per city)
- `GET /reports/latest` – Latest available record per city


## How to Run Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Access Swagger UI:
http://127.0.0.1:8000/docs

## Note: Why This Project

This project focuses on backend data pipelines rather than UI or visualization.
It reflects real-world patterns used in data ingestion, reporting services, and backend analytics systems.


## Caution

This project is intended for learning and demonstration purposes only.
