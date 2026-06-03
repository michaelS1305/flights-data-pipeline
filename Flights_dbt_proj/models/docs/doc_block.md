{% docs stg_flights_overview %}

# Silver Staging Flights

This model transforms and standardizes flight records from the Bronze layer into an analytics-ready Silver dataset.

## Transformations Applied

### Column Standardization

Source column names are renamed to business-friendly names following a consistent naming convention.

### Data Type Standardization

Relevant fields are cast into appropriate Snowflake data types, including:

- Timestamps
- String fields
- Terminal identifiers

### String Cleaning

String values are standardized using trimming operations to remove unnecessary whitespace.

### Flight Deduplication

The source data may contain multiple records representing updates to the same flight over time.

To ensure a single record per flight, the model applies a deduplication strategy using a window function and keeps only the most recent flight state.

## Business Key

A flight is uniquely identified by the following combination of columns:

- airline_code
- flight_number
- scheduled_time
- arrival_departure

This business key was derived through exploratory analysis of the source data and validated for uniqueness after deduplication.

## Output

The resulting model contains one latest record per flight and serves as the foundation for future Gold layer dimensional models and analytical reporting.

{% enddocs %}