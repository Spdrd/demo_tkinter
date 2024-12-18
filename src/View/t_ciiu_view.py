from customtkinter import *
from View.Frames.crud_display import *
from Repository.repository_t_ciiu import *
from View.Frames.t_ciiu_display import *
from Services.service_reporte_tabla import *
from View.t_view import *

class t_ciiu_view(t_view):

    def __init__(self):
        super().__init__()
        # Instance View
        app = CTkToplevel()
        app.title("t_ciiu_view")

        repo = repository_t_ciiu()
        s_reporte_tabla = service_reporte_tabla("Tabla CIIU", ("Codigo", "CIIU"), repo.read())

        app.geometry(f"{self.w}x{self.h}")
        title = CTkLabel(app, text="Tabla CIIU", font=("", 40))
        title.pack(padx=1, pady=3)
        city_display_frame = t_ciiu_display(app)
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