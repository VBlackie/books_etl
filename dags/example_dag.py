from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

# Define the default_args dictionary
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 11, 4),
    'retries': 1,
}

# Instantiate the DAG
with DAG(
    'example_dag',
    default_args=default_args,
    schedule_interval='@daily',  # Run once a day
    catchup=False,
) as dag:

    # Define a simple Python function
    def print_hello():
        print("Hello, Airflow!")

    # Create a PythonOperator task
    hello_task = PythonOperator(
        task_id='print_hello',
        python_callable=print_hello
    )

# The DAG will automatically include the task
