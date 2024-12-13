from View import manage_cities_view_demo
from Repository import repository_cities_demo
from Entities import City_demo

if __name__ == "__main__":
    repository_cities_demo.create_cities_table()
    manage_cities_view_demo.main()