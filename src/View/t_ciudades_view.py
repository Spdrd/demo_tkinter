from customtkinter import *
from View.Frames.crud_display import *
from Repository.repository_t_ciudades import *
from View.Frames.t_ciudades_display import *
from Services.service_reporte_tabla import *
from View.t_view import *

class t_ciudades_view(t_view):

    def __init__(self):
        self.title = "Tabla Ciudades"
        self.repo = repository_t_ciudades()
        self.app = CTkToplevel()
        self.app.title("t_ciudades_view")
        self.s_reporte_tabla = service_reporte_tabla(self.title, ("Codigo", "Ciudad"))
        self.data_display_frame = t_ciudades_display
        super().__init__()

        self.app.mainloop()
