# Library imports
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

# DAG arguments
default_args = {
    'owner': 'ismail',
    'start_date': datetime(2025, 7, 27),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

# DAG definition
dag = DAG(
    'simple_example',
    description='A simple DAG',
    default_args=default_args,
    schedule_interval=timedelta(seconds=5),
    catchup=False  # <- Add this line
)

# Task definitions
task1 = BashOperator(
    task_id='print_hello',
    bash_command="echo 'Greetings. The date and time are:'",
    dag=dag
)

task2 = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag
)

# Task pipeline
task1 >> task2
