from customtkinter import *
from View.Frames.city_display_demo import *
from View.Frames.crud_display import *
from Repository import repository_cities_demo
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
                                          repository_cities_demo.create_city, 
                                          repository_cities_demo.read_city, 
                                          repository_cities_demo.update_city, 
                                          repository_cities_demo.delete_city, 
                                          repository_cities_demo.read_max_city_id, 
                                          repository_cities_demo.read_min_city_id,
                                          repository_cities_demo.get_atributes,
                                          [city_display_frame])

        app.mainloop()

def main():
    manage_ciities_view()