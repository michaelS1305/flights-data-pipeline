{% docs bronze_flights_current %}

# Bronze Flights Current

This source table contains structured flight records parsed from the latest raw JSON snapshot ingested from the Israeli Government Flights API (data.gov.il).

## Ingestion Process

The ingestion pipeline performs the following steps:

1. Extracts flight data from the public Flights API.
2. Stores raw JSON snapshots in Azure Data Lake Storage Gen2.
3. Loads raw files into Snowflake using an External Stage and COPY INTO.
4. Parses the latest snapshot into a structured Bronze table.

## Table Purpose

The `flights_current` table represents the most recent operational state of airport arrivals and departures available from the source system.

This table serves as the primary source for downstream dbt transformations and Silver layer modeling.

## Data Characteristics

- Snapshot-based dataset
- Contains arrivals and departures
- Includes operational flight status information
- Refreshed from the latest available API snapshot
- Used as the source-of-truth input for Silver transformations

{% enddocs %}