import psycopg2
import json
from Entities import City 

def create_city(city: City.City):

    with open("src\Repository\db_config.json", "r") as file:
        db_config = json.load(file)

    try:
        # Establecer la conexión
        conn = psycopg2.connect(**db_config)
        print("Conexión exitosa a la base de datos")

        # Crear un cursor para ejecutar consultas
        cursor = conn.cursor()

        query = "CREATE TABLE IF NOT EXISTS cities(ID SERIAL PRIMARY KEY,CODE VARCHAR(100) UNIQUE,NAME VARCHAR(100))"
        cursor.execute(query)

        # Ejecutar una consulta
        query = f"INSERT INTO cities (CODE, NAME) VALUES ('{city.code}', '{city.name}')"
        cursor.execute(query)

        query = f"SELECT id FROM cities WHERE code = '{city.code}'"
        cursor.execute(query)

        conn.commit()

        id = cursor.fetchone()[0]

        # Cerrar el cursor
        cursor.close()

        print(id)

        return id

    except psycopg2.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
    finally:
        # Asegurarse de cerrar la conexión
        if conn:
            conn.close()
            print("Conexión cerrada")

def read_city(id=None, code=None):
    index_name = ""

    if not id == None:
        index_name = "id"
        index = id
    elif not code== None:
        index_name = "code"
        index = code

    with open("src\Repository\db_config.json", "r") as file:
        db_config = json.load(file)

    try:
        # Establecer la conexión
        conn = psycopg2.connect(**db_config)
        print("Conexión exitosa a la base de datos")

        # Crear un cursor para ejecutar consultas
        cursor = conn.cursor()

        # Ejecutar una consulta
        if index == "first":
            query = f"SELECT * FROM cities WHERE id = (SELECT MIN(id) FROM cities)"
        elif index == "last":
            query = f"SELECT * FROM cities WHERE id = (SELECT MAX(id) FROM cities)"
        elif not index_name == "":
            query = f"SELECT * FROM cities WHERE {index_name} = '{index}'"
        else:
            query = "SELECT * FROM cities"

        
        cursor.execute(query)
        conn.commit()

        data = cursor.fetchone()

        city = City.City()
        city.from_tuple(data)

        # Cerrar el cursor
        cursor.close()

    except psycopg2.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
    finally:
        # Asegurarse de cerrar la conexión
        if conn:
            conn.close()
            print("Conexión cerrada")

        return (data[0], city)

def update_city(code, name):

    with open("src\Repository\db_config.json", "r") as file:
        db_config = json.load(file)

    try:
        # Establecer la conexión
        conn = psycopg2.connect(**db_config)
        print("Conexión exitosa a la base de datos")

        # Crear un cursor para ejecutar consultas
        cursor = conn.cursor()

        query = f"UPDATE cities SET name = '{name}' WHERE code = '{code}'"
        cursor.execute(query)

        query = f"SELECT id FROM cities WHERE code = '{code}'"
        cursor.execute(query)

        conn.commit()

        id = cursor.fetchone()[0]

        # Cerrar el cursor
        cursor.close()

        print(id)

        return id

    except psycopg2.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
    finally:
        # Asegurarse de cerrar la conexión
        if conn:
            conn.close()
            print("Conexión cerrada")

def delete_city(id=None, code=None):
    index_name = ""

    if not id == None:
        index_name = "id"
        index = id
    elif not code== None:
        index_name = "code"
        index = code

    if index_name == "":
        print("Indice no recibido") 
    else:
        with open("src\Repository\db_config.json", "r") as file:
            db_config = json.load(file)

        try:
            # Establecer la conexión
            conn = psycopg2.connect(**db_config)
            print("Conexión exitosa a la base de datos")

            # Crear un cursor para ejecutar consultas
            cursor = conn.cursor()

            # Ejecutar una consulta
            query = f"DELETE FROM cities WHERE {index_name} = '{index}'"

            
            cursor.execute(query)
            conn.commit()

            print("Registro eliminado")

            # Cerrar el cursor
            cursor.close()

        except psycopg2.Error as e:
            print(f"Error al conectar a la base de datos: {e}")
        finally:
            # Asegurarse de cerrar la conexión
            if conn:
                conn.close()
                print("Conexión cerrada")

def main():
    update_city(code="BOG", name="BOGLONIA")

if __name__ == "__main__":
    main()