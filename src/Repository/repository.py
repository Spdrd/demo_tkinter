import psycopg2
import json
from resource_path import *

class repository:

    def __init__(self, table_name: str, atributes: tuple, atributes_types: tuple, fk_atributes = (), fk_table = ()):
        self.table_name = table_name
        self.atributes = atributes
        self.atributes_types = atributes_types
        self.fk_atributes = fk_atributes
        self.fk_table = fk_table
        self.create_table()
    
    def get_pk_atribute(self):
        return self.atributes[0]

    def atributes_to_string(self):
        
        str_atributes = "("
        for i in range(len(self.atributes)):
            str_atributes += self.atributes[i]
            if i+1 < len(self.atributes):
                str_atributes += ","
        str_atributes += ")"
        return str_atributes


    def connect_db_by_json(self):
        config_path = resource_path("src\Repository\db_config.json")
        with open(config_path, "r") as file:
            db_config = json.load(file)
        return psycopg2.connect(**db_config)

    def connect_db(self):
        return self.connect_db_by_json()

    def create_table(self):
        try:
            # Establecer la conexión
            conn = self.connect_db()
            print("Conexión exitosa a la base de datos")

            # Crear un cursor para ejecutar consultas
            cursor = conn.cursor()

            query = f"CREATE TABLE IF NOT EXISTS {self.table_name}("
            for i in range(len(self.atributes)):
                query += f"{self.atributes[i]} {self.atributes_types[i]}"
                if i+1 < len(self.atributes):
                    query += ","

            for i in range (len(self.fk_atributes)):
                    query += ","
                    query += f"FOREIGN KEY ({self.fk_atributes[i]}) REFERENCES {self.fk_table[i]}({self.fk_atributes[i]}) ON DELETE RESTRICT"
            query += ")"

            print(f"repository 57: {query}")

            cursor.execute(query)

            conn.commit()

            # Cerrar el cursor
            cursor.close()

        except psycopg2.Error as e:
            print(f"Error al conectar a la base de datos: {e}")
        finally:
            # Asegurarse de cerrar la conexión
            if conn:
                conn.close()
                print("Conexión cerrada")

    def insert(self, data):

        try:
            # Establecer la conexión
            conn = self.connect_db()
            print("Conexión exitosa a la base de datos")

            # Crear un cursor para ejecutar consultas
            cursor = conn.cursor()

            # Ejecutar una consulta
            query = f"INSERT INTO {self.table_name} {self.atributes_to_string()} VALUES {tuple(data)}"
            print(query)
            cursor.execute(query)

            query = f"SELECT ROW_NUMBER() OVER (ORDER BY {self.atributes[0]}) FROM {self.table_name}"
            print(query)
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

    def read(self, index = "", index_name = ""):

        try:
            # Establecer la conexión
            conn = self.connect_db()
            print("Conexión exitosa a la base de datos")

            # Crear un cursor para ejecutar consultas
            cursor = conn.cursor()

            # Ejecutar una consulta
            if index == "first":
                query = f"SELECT * FROM (SELECT *, ROW_NUMBER() OVER (ORDER BY {self.atributes[0]}) AS n FROM {self.table_name}) WHERE n = (SELECT MIN(n) FROM (SELECT ROW_NUMBER() OVER (ORDER BY {self.table_name}) AS n, * FROM {self.table_name}))"
            elif index == "last":
                query = f"SELECT * FROM (SELECT *, ROW_NUMBER() OVER (ORDER BY {self.atributes[0]}) AS n FROM {self.table_name}) WHERE n = (SELECT MAX(n) FROM (SELECT ROW_NUMBER() OVER (ORDER BY {self.table_name}) AS n, * FROM {self.table_name}))"
            elif index_name == "reg":
                print("a")
                query = f"SELECT * FROM (SELECT *, ROW_NUMBER() OVER (ORDER BY {self.atributes[0]}) AS n FROM {self.table_name}) WHERE n = {index}"
            elif not index_name == "":
                if isinstance(index, str):
                    query = f"SELECT * FROM {self.table_name} WHERE {index_name} = '{index}'"
                else:
                    query = f"SELECT * FROM {self.table_name} WHERE {index_name} = {index}"

            else:
                query = f"SELECT * FROM {self.table_name}"

            print(f"repository {query}")
            cursor.execute(query)
            conn.commit()
            if index_name == "":
                data = cursor.fetchall()
            else:
                data = cursor.fetchone()

            # Cerrar el cursor
            cursor.close()

        except psycopg2.Error as e:
            print(f"Error al conectar a la base de datos: {e}")
        finally:
            # Asegurarse de cerrar la conexión
            if conn:
                conn.close()
                print("Conexión cerrada")
            
            print(f"read: {data}")
            return (data)

    def update(self, data: tuple):

        try:
            # Establecer la conexión
            conn = self.connect_db()
            print("Conexión exitosa a la base de datos")

            # Crear un cursor para ejecutar consultas
            cursor = conn.cursor()
            
            query = f"UPDATE {self.table_name} SET "

            for i in range(len(self.atributes)):
                if isinstance(data[i], str):
                    query += f"{self.atributes[i]} = '{data[i]}'"
                else:
                    query += f"{self.atributes[i]} = {data[i]}"
                if i+1 < len(self.atributes):
                    query += ", "
            query += f" WHERE {self.atributes[0]} = {data[0]}"

            print(query)

            cursor.execute(query)

            query = f"SELECT n FROM (SELECT ROW_NUMBER() OVER (ORDER BY {self.atributes[0]}) AS n, * FROM {self.table_name}) WHERE {self.atributes[0]} = {data[0]};"
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

    def delete(self, index, index_name=""):

        if index_name == "":
            print("Indice no recibido") 
        else:

            try:
                # Establecer la conexión
                conn = self.connect_db()
                print("Conexión exitosa a la base de datos")

                # Crear un cursor para ejecutar consultas
                cursor = conn.cursor()

                # Ejecutar una consulta
                if isinstance(index, str):
                    print(f"index: {index}")
                    query = f"DELETE FROM {self.table_name} WHERE {index_name} = '{index}'"
                else:
                    query = f"DELETE FROM {self.table_name} WHERE {index_name} = {index}"

                print(query)
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

    def read_min_reg(self):

        try:
            # Establecer la conexión
            conn = self.connect_db()
            print("Conexión exitosa a la base de datos")

            # Crear un cursor para ejecutar consultas
            cursor = conn.cursor()

            query = f"SELECT MIN(n)FROM (SELECT ROW_NUMBER() OVER (ORDER BY {self.atributes[0]}) AS n, * FROM {self.table_name});"
            
            cursor.execute(query)
            conn.commit()

            data = cursor.fetchone()

            # Cerrar el cursor
            cursor.close()

        except psycopg2.Error as e:
            print(f"Error al conectar a la base de datos: {e}")
        finally:
            # Asegurarse de cerrar la conexión
            if conn:
                conn.close()
                print("Conexión cerrada")

            return (data[0])

    def read_max_reg(self):

        try:
            # Establecer la conexión
            conn = self.connect_db()
            print("Conexión exitosa a la base de datos")

            # Crear un cursor para ejecutar consultas
            cursor = conn.cursor()

            query = f"SELECT MAX(n)FROM (SELECT ROW_NUMBER() OVER (ORDER BY {self.atributes[0]}) AS n, * FROM {self.table_name});"
            
            cursor.execute(query)
            conn.commit()

            data = cursor.fetchone()

            # Cerrar el cursor
            cursor.close()

        except psycopg2.Error as e:
            print(f"Error al conectar a la base de datos: {e}")
        finally:
            # Asegurarse de cerrar la conexión
            if conn:
                conn.close()
                print("Conexión cerrada")
            
            return (data[0])

    def get_atributes(self):

        try:
            # Establecer la conexión
            conn = self.connect_db()
            print("Conexión exitosa a la base de datos")

            # Crear un cursor para ejecutar consultas
            cursor = conn.cursor()

            query = f"SELECT column_name FROM information_schema.columns WHERE table_name = '{self.table_name}'"

            cursor.execute(query)
            conn.commit()

            data = cursor.fetchall()

            # Cerrar el cursor
            cursor.close()

        except psycopg2.Error as e:
            print(f"Error al conectar a la base de datos: {e}")
        finally:
            # Asegurarse de cerrar la conexión
            if conn:
                conn.close()
                print("Conexión cerrada")
            print(data)
            return (data)
        

def main():
    table_name = "t_ciudades"
    atributes = ("ciu_codigo", "ciu_nombre")
    atributes_types = ("NUMERIC(5,0) PRIMARY KEY", "VARCHAR(30)")

    repo = repository(table_name, atributes, atributes_types)
    

if __name__ == "__main__":
    main()