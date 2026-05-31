from contextlib import contextmanager

import psycopg2

from .config import settings


@contextmanager
def get_connection():
    connection = psycopg2.connect(**settings.require_database())
    try:
        yield connection
        connection.commit()
    except Exception:
        connection.rollback()
        raise
    finally:
        connection.close()
