from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from slack_notifications import send_slack_message
from extract import extract_books_data
from transform import transform_books_data
from load import load_books_data
from pytz import timezone
import logging
import os


# Define the Slack notification messages
def notify_start():
    slack_api_token = os.getenv("SLACK_API_TOKEN")
    print(f"SLACK_API_TOKEN: {slack_api_token}")
    send_slack_message("ETL Pipeline: Starting the process 🚀")


def notify_success():
    send_slack_message("ETL Pipeline: Process completed successfully ✅")


def notify_failure(context):
    send_slack_message(f"ETL Pipeline: Failed! ❌\nError: {context['exception']}")


# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info("Initializing book_etl_dag...")

local_tz = timezone("America/New_York")

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 11, 13, tzinfo=local_tz),
    'retries': 1,
    'on_failure_callback': notify_failure
}

with DAG(
    'book_etl_dag',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
) as dag:
    logging.info("Defining tasks for book_etl_dag.")

    start_notification = PythonOperator(
        task_id='notify_start',
        python_callable=notify_start
    )

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

    success_notification = PythonOperator(
        task_id='notify_success',
        python_callable=notify_success
    )

    # Set dependencies
    start_notification >> extract_task >> transform_task >> load_task >> success_notification
    logging.info("Task dependencies set: start -> extract -> transform -> load ->success.")
