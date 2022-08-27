from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "Jason",
    "email": "mlops@community.com",
    "start_date": days_ago(2)
}

dag = DAG(
    dag_id="python_example_ml_retrain",
    description="A simple ML retrain DAG using Python",
    default_args=default_args,
    # schedule_interval=timedelta(days=1),
    # on_success_callback=some_function,
    # on_failure_callback=some_other_function,
)
with DAG('Helloworld', default_args=default_args) as dag:

    t1 = BashOperator(
        task_id='task_1',
        bash_command='echo "Hello World from Task 1"',
        dag=dag)

    t2 = BashOperator(
        task_id='task_2',
        bash_command='echo "Hello World from Task 2"',
        dag=dag)

    t3 = BashOperator(
        task_id='task_3',
        bash_command='echo "Hello World from Task 3"',
        dag=dag)

    t4 = BashOperator(
        task_id='task_4',
        bash_command='echo "Hello World from Task 4"',
        dag=dag)

    t2.set_upstream(t1)
    t3.set_upstream(t1)
    t4.set_upstream(t2)
    t4.set_upstream(t3)
