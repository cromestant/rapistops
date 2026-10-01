from rapistops.database import get_connection
from rapistops.provenance import Provenance


def save_provenance(provenance: Provenance) -> None:
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO provenance (
                    id,
                    source_id,
                    collected_at,
                    collection_method,
                    source_reference,
                    collection_context
                )
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (
                    provenance.id,
                    provenance.source_id,
                    provenance.collected_at,
                    provenance.collection_method,
                    provenance.source_reference,
                    provenance.collection_context,
                ),
            )

        connection.commit()
    finally:
        connection.close()