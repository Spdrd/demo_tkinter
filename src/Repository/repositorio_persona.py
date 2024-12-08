import psycopg2
import json

def insert_city():

    with open("src\Repository\db_config.json", "r") as file:
        db_config = json.load(file)

    try:
        # Establecer la conexión
        conn = psycopg2.connect(**db_config)
        print("Conexión exitosa a la base de datos")

        # Crear un cursor para ejecutar consultas
        cursor = conn.cursor()

        # Ejecutar una consulta
        query = "INSERT INTO cities (CODE, NAME) VALUES ('BOG', 'Bogota')"
        query = "SELECT * FROM cities"
        cursor.execute(query)

        # Obtener los resultados
        rows = cursor.fetchall()
        for row in rows:
            print(row)

        # Cerrar el cursor
        cursor.close()

    except psycopg2.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
    finally:
        # Asegurarse de cerrar la conexión
        if conn:
            conn.close()
            print("Conexión cerrada")

if __name__ == "__main__":
    insert_city()