#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import psycopg2

# Obtiene la URL de la base de datos desde las variables de entorno
DATABASE_URL = os.environ['DATABASE_URL']

# Intenta establecer la conexión con la base de datos
try:
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    print("Conexión exitosa a la base de datos PostgreSQL")

    # Ejemplo de consulta: seleccionar la versión del servidor
    cursor = conn.cursor()
    cursor.execute("SELECT version();")
    version = cursor.fetchone()
    print("Versión del servidor PostgreSQL:", version)

    # Cierra la conexión
    cursor.close()
    conn.close()

except psycopg2.OperationalError as e:
    print("Error al conectar a la base de datos PostgreSQL:", e)


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gettingstarted.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
