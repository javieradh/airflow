from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def print_hello():
    print("Hello, World from Airflow!")

with DAG(
    'hello_world_dag',
    start_date=datetime(2024, 2, 27),
    schedule_interval='@daily',
    catchup=False,
) as dag:
    hello_task = PythonOperator(
        task_id='print_hello',
        python_callable=print_hello
    )
