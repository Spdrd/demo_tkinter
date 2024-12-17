from Repository.repository import *

class repository_t_ciiu(repository):
    def __init__(self):
        super().__init__("t_ciiu", ("ciiu_codigo", "ciiu_nombre"), ("NUMERIC(4,0) PRIMARY KEY", "VARCHAR(40)"))

def main():
    repo = repository_t_ciiu()

if __name__ == "__main__":
    main()