from customtkinter import *
from View.Frames.crud_display import *
from Repository.repository_t_segmentos import *
from View.Frames.t_segmentos_display import *
class t_segmentos_view:

    def __init__(self):
        # Instance View
        app = CTkToplevel()
        app.title("t_segmentos_view")

        ancho = 600
        alto = 400

        repo = repository_t_segmentos()

        app.geometry(f"{ancho}x{alto}")
        title = CTkLabel(app, text="Tabla Segmentos", font=("", 40))
        title.pack(padx=1, pady=3)
        city_display_frame = t_segmentos_display(app)
        crud_display_frame = crud_display(app,
                                          repo.insert, 
                                          repo.read, 
                                          repo.update, 
                                          repo.delete, 
                                          repo.read_max_reg, 
                                          repo.read_min_reg,
                                          repo.get_atributes,
                                          repo.get_pk_atribute,
                                          [city_display_frame])

        app.mainloop()