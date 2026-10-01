import psycopg


def get_connection():
    return psycopg.connect(
        dbname="rapistops",
        user="meadow",
    )