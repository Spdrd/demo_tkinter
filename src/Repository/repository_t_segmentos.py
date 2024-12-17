from Repository.repository import *

class repository_t_segmentos(repository):
    def __init__(self):
        super().__init__("t_segmentos", ("seg_codigo", "seg_nombre"), ("NUMERIC(3,0) PRIMARY KEY", "VARCHAR(30)"))

def main():
    repo = repository_t_segmentos()

if __name__ == "__main__":
    main()