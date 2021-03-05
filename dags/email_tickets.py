import datetime as dt

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.providers.http.operators.http import SimpleHttpOperator

SERVICE_ROOT= "mail"
EMAIL_FETCH_SVC = "fetch_mail"

def fetch_emails():
    pass

def print_world():
    print('world')

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5),
}

with DAG('create_ticket_from_email',
         default_args=default_args,
         schedule_interval='0 * * * *',
         ) as dag:

    print_hello = BashOperator(task_id='print_hello',
                               bash_command='echo "hello"')
    sleep = BashOperator(task_id='sleep',
                         bash_command='sleep 5')
    print_world = PythonOperator(task_id='print_world',
                                 python_callable=print_world)
