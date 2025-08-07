# Import libraries
from datetime import timedelta, datetime
from airflow.models import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.email import EmailOperator
from utils.helper import process_temperature

# DAG default arguments
default_args = {
    'owner': 'Ismail',
    'start_date': datetime(2025, 8, 6),
    'email': 'ismailhafeez13@gmail.com',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    dag_id='email_dag',
    default_args=default_args,
    description='sends an email',
    schedule_interval=timedelta(seconds=30),
    catchup=False
)

# Task 1 - PythonOperator
task1 = PythonOperator(
    task_id='python_task',
    python_callable=process_temperature,
    provide_context=True,
    dag=dag,
)

# Task 2 - EmailOperator
task2 = EmailOperator(
    task_id='mail_task',
    to='ismailhafeez13@gmail.com',
    subject='Airflow Email Operator example',
    html_content="""
        <p>This is a test email sent from Airflow<br>
        <strong>Ain't it cool?</strong><br>
        Temperature: {{ ti.xcom_pull(task_ids='python_task') }}</p>
    """,
    dag=dag,
)

# Set the task order
task1 >> task2
