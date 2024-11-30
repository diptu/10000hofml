from airflow import DAG
from airflow.providers.http.hooks.http import HttpHook
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.decorators import task
from airflow.utils.dates import days_ago
import requests
import json

# Latitude and longitude for the desired location (London in this case)
OFFSET = 0
LIMIT = 20
POSTGRES_CONN_ID = "postgres_default"
API_CONN_ID = "pokeapi_etl"
URL = "https://pokeapi.co/api/v2/"

default_args = {"owner": "airflow", "start_date": days_ago(1)}

## DAG
with DAG(
    dag_id="pokimon_etl_pipeline",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False,
) as dags:

    @task()
    def extract_pokimon_data():
        """Extract pokimon data from Open-Meteo API using Airflow Connection."""

        # Use HTTP Hook to get connection details from Airflow connection

        http_hook = HttpHook(http_conn_id=API_CONN_ID, method="GET")

        ## Build the API endpoint
        ## https://pokeapi.co/api/v2/pokemon?limit=20&offset=0
        endpoint = f"pokemon?offset={OFFSET}&limit={LIMIT}"

        ## Make the request via the HTTP Hook
        response = http_hook.run(endpoint)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to fetch pokimon data: {response.status_code}")

    @task()
    def transform_pokimon_data(pokimon_data):
        """Transform the extracted pokimon data."""
        transformed_data = {
            "name": pokimon_data["name"],
            "url": pokimon_data["url"],
        }
        return transformed_data

    @task()
    def load_pokimon_data(transformed_data):
        """Load transformed data into PostgreSQL."""
        pg_hook = PostgresHook(postgres_conn_id=POSTGRES_CONN_ID)
        conn = pg_hook.get_conn()
        cursor = conn.cursor()

        # Create table if it doesn't exist
        cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS pokimon (

            id INT PRIMARY KEY AUTOINCREMENT,
            name string NOT NULL unique,
            url string NOT NULL unique,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        )

        # Insert transformed data into the table
        cursor.execute(
            """
        INSERT INTO pokimon (name, url, created_at)
        VALUES (%s, %s, %s)
        """,
            (
                transformed_data["name"],
                transformed_data["url"],
            ),
        )

        conn.commit()
        cursor.close()

    ## DAG Worflow- ETL Pipeline
    pokimon_data = extract_pokimon_data()
    transformed_data = transform_pokimon_data(pokimon_data)
    load_pokimon_data(transformed_data)
