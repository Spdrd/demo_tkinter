from Repository.repository import *

class repository_t_ciudades(repository):
    def __init__(self):
        super().__init__("t_ciudades", ("ciu_codigo", "ciu_nombre"), ("NUMERIC(5,0) PRIMARY KEY", "VARCHAR(30)"))

def main():
    repo = repository_t_ciudades()

if __name__ == "__main__":
    main()