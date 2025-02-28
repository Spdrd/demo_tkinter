from Repository.repository import *

class repository_t_clientes(repository):
    def __init__(self):
        super().__init__(
            "t_clientes", 
            ("id_cliente", "ticli_codigo"), 
            ("SERIAL PRIMARY KEY", "NUMERIC(2,0)"),
            fk_atributes= ("ticli_codigo",),
            fk_table = ("t_tipos_cliente",)
            )

def main():
    repo = repository_t_clientes()

if __name__ == "__main__":
    main()