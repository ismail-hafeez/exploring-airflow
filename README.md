# How to get started with Apache Airflow

`sudo add-apt-repository ppa:deadsnakes/ppa`

`sudo apt update`

`sudo apt install python3.11 python3.11-venv`

`python3.11 -m venv venv`

`source venv/bin/activate`

`export AIRFLOW_VERSION=2.9.1`

`export PYTHON_VERSION=3.11`

`export CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"`

`pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"`

## === OPTIONAL ===
`pip install "apache-airflow[celery,postgres,redis]==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"`


`export AIRFLOW_HOME=~/airflow`
`airflow db init`
`airflow users create \
    --username  \
    --firstname  \
    --lastname  \
    --role Admin \
    --email  \
    --password `
`airflow webserver --port 8080`
## === In a new terminal (with virtualenv activated), start the scheduler: ===
`airflow scheduler`

