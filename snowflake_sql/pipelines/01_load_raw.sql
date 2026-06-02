USE DATABASE flights_project;
USE SCHEMA bronze;
USE WAREHOUSE flights_wh;

COPY INTO bronze.flights_raw
FROM (
    SELECT
        $1 AS raw_data,
        METADATA$FILENAME AS source_file_name,
        CURRENT_TIMESTAMP() AS loaded_at
    FROM @flights_project.staging.flights_stage
)
FILE_FORMAT = (
    FORMAT_NAME = flights_project.staging.json_format
);
