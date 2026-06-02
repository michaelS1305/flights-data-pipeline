CREATE OR REPLACE DATABASE flights_project;

CREATE OR REPLACE  SCHEMA flights_project.bronze;
CREATE OR REPLACE  SCHEMA flights_project.silver;
CREATE OR REPLACE  SCHEMA flights_project.gold;
CREATE OR REPLACE  SCHEMA flights_project.staging;

CREATE OR REPLACE  WAREHOUSE flights_wh
WITH
  WAREHOUSE_SIZE = 'XSMALL'
  AUTO_SUSPEND = 60
  AUTO_RESUME = TRUE;








