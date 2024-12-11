import customtkinter as ctk
from View.Frames import city_display
from View.Frames import crud_display
from Repository import repository_cities
class manage_ciities_view:

    def __init__(self):
        # Instance View
        app = ctk.CTk()
        app.title("Ciudades")

        ancho = 380
        alto = 400

        app.geometry(f"{ancho}x{alto}")
        city_display_frame = city_display.city_display(app)
        crud_display_frame = crud_display.crud_display(app, 
                                                       repository_cities.create_city, 
                                                       repository_cities.read_city, 
                                                       repository_cities.update_city, 
                                                       repository_cities.delete_city, 
                                                       repository_cities.read_max_city_id, 
                                                       repository_cities.read_min_city_id,
                                                       repository_cities.get_atributes,
                                                       [city_display_frame])

        app.mainloop()

def main():
    manage_ciities_view()