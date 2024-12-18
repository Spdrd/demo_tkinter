from customtkinter import *
from View.Frames.crud_display import *
from Repository.repository_t_paises import *
from View.Frames.t_paises_display import *
from Services.service_reporte_tabla import *
from View.t_view import *

class t_paises_view(t_view):

    def __init__(self):
        super().__init__()
        # Instance View
        app = CTkToplevel()
        app.title("t_paises_view")

        repo = repository_t_paises()
        s_reporte_tabla = service_reporte_tabla("Tabla Paises", ("Codigo", "Pais"), repo.read())

        app.geometry(f"{self.w}x{self.h}")
        title = CTkLabel(app, text="Tabla Paises", font=("", 40))
        title.pack(padx=1, pady=3)
        city_display_frame = t_paises_display(app)
        crud_display_frame = crud_display(app,
                                          repo.insert, 
                                          repo.read, 
                                          repo.update, 
                                          repo.delete, 
                                          repo.read_max_reg, 
                                          repo.read_min_reg,
                                          repo.get_atributes,
                                          repo.get_pk_atribute,
                                          s_reporte_tabla.generate_document,    
                                          [city_display_frame])

        app.mainloop()