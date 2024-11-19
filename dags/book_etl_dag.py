from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from extract import extract_books_data
from transform import transform_books_data
from load import load_books_data
from pytz import timezone
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info("Initializing book_etl_dag...")

local_tz = timezone("America/New_York")

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 11, 13, tzinfo=local_tz),
    'retries': 1,
}

with DAG(
    'book_etl_dag',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
) as dag:
    logging.info("Defining tasks for book_etl_dag.")

    extract_task = PythonOperator(
        task_id='extract_books_data',
        python_callable=extract_books_data
    )
    logging.info("Extract task created.")

    transform_task = PythonOperator(
        task_id='transform_books_data',
        python_callable=transform_books_data,
        op_args=[extract_task.output]
    )
    logging.info("Transform task created.")

    load_task = PythonOperator(
        task_id='load_books_data',
        python_callable=load_books_data,
        op_args=[transform_task.output]
    )
    logging.info("Load task created.")

    # Set dependencies
    extract_task >> transform_task >> load_task
    logging.info("Task dependencies set: extract -> transform -> load.")
