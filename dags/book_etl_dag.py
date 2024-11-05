from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from extract import extract_books_data
from transform import transform_books_data
from load import load_books_data

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 11, 5),
    'retries': 1,
}

with DAG(
    'book_etl_dag',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
) as dag:

    extract_task = PythonOperator(
        task_id='extract_books_data',
        python_callable=extract_books_data
    )

    transform_task = PythonOperator(
        task_id='transform_books_data',
        python_callable=transform_books_data,
        op_args=[extract_task.output]
    )

    load_task = PythonOperator(
        task_id='load_books_data',
        python_callable=load_books_data,
        op_args=[transform_task.output]
    )

    extract_task >> transform_task >> load_task
