USE DATABASE flights_project;
USE SCHEMA bronze;

CREATE TABLE IF NOT EXISTS bronze.flights_raw (
    raw_data VARIANT,
    source_file_name STRING,
    loaded_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS bronze.flights_current (
    record_id INTEGER,
    operator_code STRING,
    flight_number STRING,
    operator_name STRING,
    scheduled_time TIMESTAMP,
    actual_time TIMESTAMP,
    arrival_departure STRING,
    destination_airport_code STRING,
    destination_city_en STRING,
    destination_city_he STRING,
    destination_city_alt STRING,
    destination_country_he STRING,
    destination_country_en STRING,
    terminal INTEGER,
    checkin_counter STRING,
    checkin_zone STRING,
    status_en STRING,
    status_he STRING,
    source_file_name STRING,
    loaded_at TIMESTAMP
);
