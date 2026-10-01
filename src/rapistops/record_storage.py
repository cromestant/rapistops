from rapistops.database import get_connection
from rapistops.record import Record


def save_record(record: Record) -> None:
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO record (
                    id,
                    source_id,
                    provenance_id,
                    type,
                    title,
                    source_reference,
                    created_at,
                    published_at,
                    collected_at
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """,
                (
                    record.id,
                    record.source_id,
                    record.provenance_id,
                    record.type,
                    record.title,
                    record.source_reference,
                    record.created_at,
                    record.published_at,
                    record.collected_at,
                ),
            )

        connection.commit()
    finally:
        connection.close()