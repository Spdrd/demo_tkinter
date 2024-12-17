from repository import *

class repository_t_paises(repository):
    def __init__(self):
        super().__init__("t_paises", ("pais_codigo", "pais_nombre"), ("VARCHAR(2) PRIMARY KEY", "VARCHAR(30)"))

def main():
    repo = repository_t_paises()

if __name__ == "__main__":
    main()