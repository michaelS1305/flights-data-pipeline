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
dbt Silver Layer
↓
Future Gold Layer
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

### dbt Silver Layer

- Built using dbt Core and Snowflake
- Renames source columns using business-friendly naming conventions
- Standardizes data types and string values
- Implements flight deduplication logic
- Selects the latest operational state for each flight
- Documents models and sources using dbt Docs
- Includes automated data quality testing

Business Key:

- airline_code
- flight_number
- scheduled_time
- arrival_departure

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
├── Flights_dbt_proj/
│   ├── models/
│   │   ├── staging/
│   │   │   ├── source.yml
│   │   │   └── stg_flights.sql
│   │   │
│   │   ├── docs/
│   │   │   ├── doc_block.md
│   │   │   └── doc_block1.md
│   │   │
│   │   └── sources.yml
│   │
│   ├── packages.yml
│   └── dbt_project.yml
│
├── snowflake_sql/
│   ├── SETUP/
│   │   ├── 01_setup.sql
│   │   ├── 02_storage_integration.sql
│   │   ├── 03_stage.sql
│   │   └── 04_create_tables.sql
│   │
│   └── pipelines/
│       ├── load_raw.sql
│       └── refresh_current.sql
│
├── ingest.py
├── key_vault_config.py
├── logger_config.py
├── blob_storage.py
├── main.py
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
- DBT Core
- Apache Airflow (planned)
- Tableau (planned)
- Git & GitHub

---

## Current Pipeline Flow

1. Extract flight data from API
2. Save raw JSON snapshot locally
3. Upload snapshot to ADLS Gen2
4. Snowflake loads new snapshot into Bronze Raw layer
5. Snowflake refreshes structured current-state table
6. dbt transforms Bronze data into a cleaned Silver model
7. Future Gold models will support analytical reporting

---

## Planned Improvements

- Implement full Medallion Architecture (Bronze → Silver → Gold)
- Build Gold dimensional models
- Create fact and dimension tables
- Add incremental dbt models
- Implement Apache Airflow orchestration
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
