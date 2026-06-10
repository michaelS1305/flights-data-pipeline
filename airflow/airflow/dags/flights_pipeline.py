import sys

sys.path.append("/opt/project")

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from airflow.providers.snowflake.hooks.snowflake import SnowflakeHook
from datetime import datetime


from python.ingest import ingest_flights

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

    upload = EmptyOperator(task_id="upload")

    load_raw = EmptyOperator(task_id="load_raw")

    refresh_current = EmptyOperator(task_id="refresh_current")

    run_stg = EmptyOperator(task_id="run_stg")

    test_stg = EmptyOperator(task_id="test_stg")

    run_dim_airlines = EmptyOperator(task_id="run_dim_airlines")

    run_dim_airports = EmptyOperator(task_id="run_dim_airports")

    run_dim_status = EmptyOperator(task_id="run_dim_status")

    test_dim_airlines = EmptyOperator(task_id="test_dim_airlines")

    test_dim_airports = EmptyOperator(task_id="test_dim_airports")

    test_dim_status = EmptyOperator(task_id="test_dim_status")

    run_fact = EmptyOperator(task_id="run_fact")

    test_fact = EmptyOperator(task_id="test_fact")


ingest >> upload >> load_raw >> refresh_current >> run_stg


run_stg >> test_stg


run_stg >> [
    run_dim_airlines,
    run_dim_airports,
    run_dim_status
]


run_dim_airlines >> test_dim_airlines
run_dim_airports >> test_dim_airports
run_dim_status >> test_dim_status


[
    run_dim_airlines,
    run_dim_airports,
    run_dim_status
] >> run_fact


run_fact >> test_fact