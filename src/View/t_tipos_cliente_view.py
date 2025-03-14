from customtkinter import *
from View.Frames.crud_display import *
from Repository.repository_t_tipos_cliente import *
from View.Frames.t_tipos_cliente_display import *
from Services.service_reporte_tabla import *
from View.t_view import *
class t_tipos_cliente_view(t_view):

    def __init__(self):
        
        self.title = "Tabla Tipos Cliente"
        self.repo = repository_t_tipos_cliente()
        self.app = CTkToplevel()
        self.app.title("t_tipos_cliente_view")
        self.s_reporte_tabla = service_reporte_tabla(self.title, ("Codigo", "Tipo Cliente"))
        self.data_display_frame = t_tipos_cliente_display
        super().__init__()

        self.app.mainloop()