from View import manage_cities_view
from Repository import repository_cities
from Entities import City

if __name__ == "__main__":
    repository_cities.create_cities_table()
    manage_cities_view.main()