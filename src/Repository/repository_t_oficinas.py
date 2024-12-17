from repository import *

class repository_t_oficinas(repository):
    def __init__(self):
        super().__init__("t_oficinas", ("ofi_codigo", "ofi_nombre"), ("NUMERIC(4,0) PRIMARY KEY", "VARCHAR(30)"))

def main():
    repo = repository_t_oficinas()

if __name__ == "__main__":
    main()