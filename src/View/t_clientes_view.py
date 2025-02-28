from customtkinter import *
from View.Frames.crud_display import *
from Repository.repository_t_clientes import *
from View.Frames.t_clientes_display import *
from Services.service_reporte_tabla import *
from View.t_view import *
from Repository.repository_t_tipos_cliente import *

class t_clientes_view(t_view):

    def __init__(self):
        self.title = "Tabla Clientes"
        self.repo = repository_t_clientes()
        self.app = CTkToplevel()
        self.app.title("t_clientes_view")
        self.s_reporte_tabla = service_reporte_tabla(self.title, ("Id", "Tipo Cliente"))
        self.data_display_frame = t_clientes_display
        repo_t_cli = repository_t_tipos_cliente()

        tipos_cliente_raw = repo_t_cli.read()
        tipos_cliente_map = {}

        for tc in tipos_cliente_raw:
            tipos_cliente_map[tc[1]] = tc[0]
            
        print(f"t_clientes_view: {tipos_cliente_map}")

        super().__init__(args_display = (tipos_cliente_map))

        self.app.mainloop()