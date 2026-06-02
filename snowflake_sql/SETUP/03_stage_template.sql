USE DATABASE flights_project;
USE SCHEMA staging;
USE WAREHOUSE flights_wh;

CREATE OR REPLACE FILE FORMAT flights_project.staging.json_format
TYPE = JSON;

CREATE OR REPLACE STAGE flights_stage
URL = 'azure://flightsdatalake1.blob.core.windows.net/data/raw/flights/'
STORAGE_INTEGRATION = snowflake_azure_integration
FILE_FORMAT = json_format;

