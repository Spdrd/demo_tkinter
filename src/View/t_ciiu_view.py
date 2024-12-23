from customtkinter import *
from View.Frames.crud_display import *
from Repository.repository_t_ciiu import *
from View.Frames.t_ciiu_display import *
from Services.service_reporte_tabla import *
from View.t_view import *

class t_ciiu_view(t_view):

    def __init__(self):
        self.title = "Tabla CIIU"
        self.repo = repository_t_ciiu()
        self.app = CTkToplevel()
        self.app.title("t_ciiu_view")
        title_frame = CTkLabel(self.app, text=self.title, font=("", 40))
        title_frame.pack(padx=1, pady=3)
        self.s_reporte_tabla = service_reporte_tabla(self.title, ("Codigo", "CIIU"))
        self.data_display_frame = t_ciiu_display(self.app)
        super().__init__()

        self.app.mainloop()