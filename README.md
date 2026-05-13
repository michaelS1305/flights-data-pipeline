# Flights Data Pipeline

Cloud-based data engineering project that ingests flight data from the Israeli Government API, processes and transforms the data into analytics-ready datasets, and stores all layers in Azure Blob Storage.

## Architecture Overview

```text
API
↓
Raw JSON Ingestion
↓
Azure Blob Storage (Raw Layer)
↓
Processed Transformations
↓
Parquet Files
↓
Azure Blob Storage (Processed Layer)
```

---

## Current Features

### Data Ingestion
- Extracts flight data from the Data.gov.il API
- Stores raw JSON files locally using partitioned folder structure
- Uploads raw data to Azure Blob Storage

### Data Processing
- Cleans and transforms raw flight data
- Renames and standardizes column names
- Performs datatype casting
- Handles invalid datetime values safely
- Removes duplicate rows
- Standardizes text columns
- Saves processed data as Parquet files

### Cloud Integration
- Azure Blob Storage integration
- Azure Key Vault secret management
- Secure connection string handling

### Monitoring & Logging
- Structured logging system
- Execution stage tracking
- Error handling with try/except blocks
- Record count and processing metadata logging

### Project Structure

```text
data/
│
├── raw/
│   └── flights/
│
├── processed/
│   └── flights/
│
├── ingest.py
├── transform_flights.py
├── blob_storage.py
├── key_vault_config.py
├── logger_config.py
└── main.py
```

---

## Technologies Used

- Python
- Pandas
- Azure Blob Storage
- Azure Key Vault
- REST APIs
- Parquet
- Git & GitHub

---

## Current Pipeline Flow

1. Extract flight data from API
2. Save raw JSON locally
3. Upload raw files to Azure Blob Storage
4. Transform and clean raw data
5. Save processed data as Parquet
6. Upload processed files to Azure Blob Storage

---

## Planned Improvements

- Implement full Medallion Architecture (Bronze → Silver → Gold)
- Add Apache Airflow orchestration
- Build dimensional models using dbt
- Add automated data quality validation
- Add monitoring dashboards
- Implement CI/CD workflows
- Add Docker containerization
- Expand analytics and KPI layers

---

## Future Analytics Ideas

- Flight delay analysis
- Airline traffic trends
- Arrival vs departure analytics
- Terminal usage analysis
- Destination popularity metrics
- Flight status monitoring

---

## How to Run

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the pipeline

```bash
python main.py
```

---

## Author

מיכאל סנדרוביץ'
