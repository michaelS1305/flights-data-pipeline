import sys
sys.path.append("/opt/project")

import os
import subprocess
from pathlib import Path


from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.snowflake.hooks.snowflake import SnowflakeHook
from datetime import datetime
from python.ingest import ingest_flights
from python.blob_storage import upload_file_to_blob
from python.key_vault_config import get_secret

def upload_task(**context):

    file_path = context["ti"].xcom_pull(
        task_ids="ingest"
    )

    local_file_path = Path(file_path)

    blob_name = (
        f"raw/flights/"
        f"{local_file_path.parent.parent.name}/"
        f"{local_file_path.parent.name}/"
        f"{local_file_path.name}"
    )

    upload_file_to_blob(
        local_file_path=local_file_path,
        blob_name=blob_name
    )


def load_raw():

    hook = SnowflakeHook(
        snowflake_conn_id="snowflake_flights"
    )

    with open(
        "/opt/project/snowflake_sql/pipelines/01_load_raw.sql",
        "r"
    ) as file:

        sql = file.read()

    hook.run(sql)

def refresh_current():

    hook = SnowflakeHook(
        snowflake_conn_id="snowflake_flights"
    )

    with open(
        "/opt/project/snowflake_sql/pipelines/02_refresh_current.sql",
        "r"
    ) as file:

        sql = file.read()

    hook.run(sql)

def dbt_run():

    os.environ["SNOWFLAKE_PASSWORD"] = get_secret(
        "snowflake-password"
    )

    subprocess.run(
        [
            "dbt",
            "run",
            "--project-dir",
            "/opt/project/Flights_dbt_proj"
        ],
        check=True
    )

def dbt_test():

    os.environ["SNOWFLAKE_PASSWORD"] = get_secret(
        "snowflake-password"
    )

    subprocess.run(
        [
            "dbt",
            "test",
            "--project-dir",
            "/opt/project/Flights_dbt_proj"
        ],
        check=True
    )

with DAG(
    dag_id="flights_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    ingest = PythonOperator(
        task_id="ingest",
        python_callable=ingest_flights
    )

    upload = PythonOperator(
        task_id="upload",
        python_callable=upload_task
    )

    load_bronze = PythonOperator(
        task_id="load_raw",
        python_callable=load_raw
    )

    refresh_current_task = PythonOperator(
        task_id="refresh_current",
        python_callable=refresh_current
    )  

    run_stg = PythonOperator(
        task_id="dbt_run",
        python_callable=dbt_run
    )

    test_stg = PythonOperator(
        task_id="dbt_test",
        python_callable=dbt_test
    ) 


ingest >> upload >> load_bronze >> refresh_current_task >> run_stg >> test_stg

