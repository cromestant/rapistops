from rapistops.database import get_connection
from rapistops.source import Source


def save_source(source: Source) -> None:
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO source (
                    id,
                    name,
                    type,
                    organization,
                    location,
                    access_reference
                )
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (
                    source.id,
                    source.name,
                    source.type,
                    source.organization,
                    source.location,
                    source.access_reference,
                ),
            )

        connection.commit()
    finally:
        connection.close()