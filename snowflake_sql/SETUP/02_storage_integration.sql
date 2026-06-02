CREATE OR REPLACE STORAGE INTEGRATION snowflake_azure_integration
TYPE = EXTERNAL_STAGE
STORAGE_PROVIDER = AZURE
ENABLED = TRUE
AZURE_TENANT_ID = '99036d2a-39b9-4f02-a5e0-158b112fa7e4'
STORAGE_ALLOWED_LOCATIONS =('azure://flightsdatalake1.blob.core.windows.net/data/raw/flights/');

DESC INTEGRATION snowflake_azure_integration;