from airflow import DAG

from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

from datetime import datetime

Workflow= DAG(
    start_date=datetime(2023,1,1),
    dag_id="Moubawab_dag",
    schedule_interval="0 6 2 * *"
)



