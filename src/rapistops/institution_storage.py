from rapistops.database import get_connection
from rapistops.institution import Institution


def save_institution(institution: Institution) -> None:
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO institution (
                    id,
                    name,
                    type,
                    jurisdiction,
                    location,
                    description,
                    created_at,
                    updated_at
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """,
                (
                    institution.id,
                    institution.name,
                    institution.type,
                    institution.jurisdiction,
                    institution.location,
                    institution.description,
                    institution.created_at,
                    institution.updated_at,
                ),
            )

        connection.commit()
    finally:
        connection.close()