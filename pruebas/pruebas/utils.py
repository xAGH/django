import psycopg2
import os

CONNECTION_DETAILS = {
    'host': os.environ.get('POSTGRES_HOST'),
    'port': os.environ.get('POSTGRES_PORT'),
    'user': os.environ.get('POSTGRES_USER'),
    'password': os.environ.get('POSTGRES_PASSWORD'),
    'database': os.environ.get('POSTGRES_DB'),
}

def set_schema(schema_name: str, conn) -> None:
    cursosr = conn.cursor()
    print("Cambiado a" + schema_name)
    cursosr.execute(f"SET search_path TO {schema_name}")
    conn.commit()
    cursosr.close()