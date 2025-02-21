from customtkinter import *
from View.Frames.crud_display import *
from Repository.repository_t_segmentos import *
from View.Frames.t_segmentos_display import *
from Services.service_reporte_tabla import *
from View.t_view import *
class t_segmentos_view(t_view):


    def __init__(self):

        self.title = "Tabla Segmentos"
        self.repo = repository_t_segmentos()
        self.app = CTkToplevel()
        self.app.title("t_segmentos_view")
        self.s_reporte_tabla = service_reporte_tabla(self.title, ("Codigo", "Segmentos"))
        self.data_display_frame = t_segmentos_display
        super().__init__()

        self.app.mainloop()