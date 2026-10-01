from rapistops.database import get_connection
from rapistops.person import Person


def save_person(person: Person) -> None:
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO person (
                    id,
                    name,
                    identifiers,
                    description,
                    created_at,
                    updated_at
                )
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (
                    person.id,
                    person.name,
                    person.identifiers,
                    person.description,
                    person.created_at,
                    person.updated_at,
                ),
            )

        connection.commit()
    finally:
        connection.close()