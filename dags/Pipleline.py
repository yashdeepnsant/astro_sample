"""
Pipleline
DAG auto-generated by Astro Cloud IDE.
"""

from airflow.decorators import dag
from astro import sql as aql
from astro.table import Table, Metadata
import pandas as pd
import pendulum


@aql.dataframe(task_id="hello_world")
def hello_world_func():
    return "Hello World"

@aql.run_raw_sql(conn_id="conn_snf", task_id="hello_sql", results_format="pandas_dataframe")
def hello_sql_func():
    return """
    select * from prices_data limit 10;
    """

@aql.dataframe(task_id="data_dependency")
def data_dependency_func(hello_world: pd.DataFrame):
    my_string = hello_world
    return my_string

default_args={
    "owner": "yashdeepsant@eaton.com,Open in Cloud IDE",
}

@dag(
    default_args=default_args,
    schedule="*/5 * * * *",
    start_date=pendulum.from_format("2023-09-03", "YYYY-MM-DD").in_tz("Asia/Kolkata"),
    catchup=True,
    owner_links={
        "yashdeepsant@eaton.com": "mailto:yashdeepsant@eaton.com",
        "Open in Cloud IDE": "https://cloud.astronomer.io/cllyrswtd00k001mvcn1z9xau/cloud-ide/clm2ysuyu001w01mao4iroaxp/clm2yytnm001x01maknm4an50",
    },
)
def Pipleline():
    hello_world = hello_world_func()

    hello_sql = hello_sql_func()

    data_dependency = data_dependency_func(
        hello_world,
    )

    hello_sql << hello_world

dag_obj = Pipleline()
