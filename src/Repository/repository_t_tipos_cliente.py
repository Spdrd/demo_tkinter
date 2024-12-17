from repository import *

class repository_t_tipos_cliente(repository):
    def __init__(self):
        super().__init__("t_tipos_cliente", ("ticli_codigo", "ticli_nombre"), ("NUMERIC(2,0) PRIMARY KEY", "VARCHAR(30)"))

def main():
    repo = repository_t_tipos_cliente()

if __name__ == "__main__":
    main()