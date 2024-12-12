from customtkinter import *
from View.Frames.city_display import *
from View.Frames.crud_display import *
from Repository import repository_cities
class manage_ciities_view:

    def __init__(self):
        # Instance View
        app = CTk()
        app.title("Ciudades")

        ancho = 600
        alto = 400

        app.geometry(f"{ancho}x{alto}")
        title = CTkLabel(app, text="Tabla Ciudades", font=("", 40))
        title.pack(padx=1, pady=3)
        city_display_frame = city_display(app)
        crud_display_frame = crud_display(app, 
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