from customtkinter import *
from View.Frames.crud_display import *
from Repository.repository_t_oficinas import *
from View.Frames.t_oficinas_display import *
from Services.service_reporte_tabla import *
from View.t_view import *

class t_oficinas_view(t_view):

    

    def __init__(self):
        self.title = "Tabla Oficinas"
        self.repo = repository_t_oficinas()
        self.app = CTkToplevel()
        self.app.title("t_oficinas_view")
        self.s_reporte_tabla = service_reporte_tabla(self.title, ("Codigo", "Oficina"))
        self.data_display_frame = t_oficinas_display
        super().__init__()

        self.app.mainloop()
