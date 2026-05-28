# Flights Data Pipeline

Cloud-based data engineering project that ingests flight data from the Israeli Government API, stores raw snapshots in Azure Data Lake Storage Gen2, and builds a Snowflake Bronze layer for analytics-ready processing and future Medallion Architecture expansion.

## Architecture Overview

```text
Data.gov.il Flights API
↓
Python API Ingestion
↓
Azure Data Lake Storage Gen2 (Raw JSON Snapshots)
↓
Snowflake External Stage
↓
Bronze Raw Layer (VARIANT JSON)
↓
Bronze Current Layer (Structured Snapshot)
↓
Future Silver / Gold Layers
↓
Tableau Dashboards
```

---

## Current Features

### Data Ingestion
- Extracts flight data from the Data.gov.il Flights API
- Saves raw JSON snapshots using partitioned ingestion folders
- Uploads snapshots to Azure Data Lake Storage Gen2
- Supports incremental snapshot ingestion

---

### Snowflake Bronze Layer

## Bronze Raw Table
- Stores raw API snapshots as semi-structured JSON
- Uses Snowflake VARIANT datatype
- Maintains historical raw ingestion history
- Stores ingestion metadata:
  - source file name
  - ingestion timestamp

## Bronze Current Table
- Parses and flattens latest snapshot JSON
- Creates structured analytics-ready flight table
- Uses LATERAL FLATTEN for JSON array expansion
- Performs datatype casting and column standardization
- Always represents the latest API snapshot state

### Cloud Integration
- Azure Data Lake Storage Gen2 integration
- Azure Key Vault secret management
- Snowflake External Stage integration
- Snowflake Storage Integration authentication


### Monitoring & Logging
- Structured logging system
- Execution stage tracking
- Error handling with try/except blocks

### Project Structure

```text
project/
│
├── snowflake_sql/
│    ├── SETUP/
│    │   ├── 01_setup.sql
│    │   ├── 02_storage_integration.sql
│    │   ├── 03_stage.sql
│    │   └── 04_create_tables.sql   
│    │
│    └── pipelines/
│        ├── load_raw.sql
│        └── refresh_current.sql
│
├── python/
│   ├── ingest.py
│   ├── upload_to_adls.py
│   ├── key_vault_config.py
│   ├── logger_config.py
│   └── main.py
│
└── data/
    └── raw/
        └── flights/
```

---

## Technologies Used

- Python
- Snowflake
- Azure Data Lake Storage Gen2
- Azure Key Vault
- SQL
- REST APIs
- Apache Airflow (planned)
- dbt (planned)
- Tableau (planned)
- Git & GitHub

---

## Current Pipeline Flow

1. Extract flight data from API
2. Save raw JSON snapshot locally
3. Upload snapshot to ADLS Gen2
4. Snowflake loads new snapshot into Bronze Raw layer
5. Snowflake refreshes structured current-state table
6. Future transformations will populate Silver and Gold layers

---

## Planned Improvements

- Implement full Medallion Architecture (Bronze → Silver → Gold)
- Add Apache Airflow orchestration
- Build transformations and modeling using dbt
- Build Silver deduplication and business-key logic
- Add Gold dimensional models and KPI layers
- Add automated data quality testing
- Build Tableau dashboards

---

## Future Analytics Ideas

- Flight delay analysis
- Airline traffic trends
- Airport congestion analytics
- Arrival vs departure monitoring
- Destination popularity analysis
- Flight status tracking
- Terminal activity analysis

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

### Execute Snowflake pipeline

Run SQL scripts in order:

01_setup.sql
02_storage_integration.sql
03_stage.sql
04_create_tables.sql
pipelines/load_raw.sql
pipelines/refresh_current.sql
 
---

## Author

Michael Sandrovich
