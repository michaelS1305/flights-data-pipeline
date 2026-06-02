USE DATABASE flights_project;
USE SCHEMA bronze;
USE WAREHOUSE flights_wh;

CREATE OR REPLACE TABLE bronze.flights_current AS
SELECT
    f.value:_id::INTEGER         AS record_id,
    f.value:CHOPER::STRING      AS operator_code,
    f.value:CHFLTN::STRING      AS flight_number,
    f.value:CHOPERD::STRING     AS operator_name,
    f.value:CHSTOL::TIMESTAMP   AS scheduled_time,
    f.value:CHPTOL::TIMESTAMP   AS actual_time,
    f.value:CHAORD::STRING      AS arrival_departure,
    f.value:CHLOC1::STRING      AS destination_airport_code,
    f.value:CHLOC1D::STRING     AS destination_city_en,
    f.value:CHLOC1TH::STRING    AS destination_city_he,
    f.value:CHLOC1T::STRING     AS destination_city_alt,
    f.value:CHLOC1CH::STRING    AS destination_country_he,
    f.value:CHLOCCT::STRING     AS destination_country_en,
    f.value:CHTERM::INTEGER     AS terminal,
    f.value:CHCINT::STRING      AS checkin_counter,
    f.value:CHCKZN::STRING      AS checkin_zone,
    f.value:CHRMINE::STRING     AS status_en,
    f.value:CHRMINH::STRING     AS status_he,
    r.source_file_name,
    r.loaded_at
FROM bronze.flights_raw r,
LATERAL FLATTEN(input => r.raw_data:result:records) f
QUALIFY r.loaded_at = MAX(r.loaded_at) OVER ();
