from customtkinter import *
from View.Frames.crud_display import *
from View.Frames.t_ciiu_display import *
from Services.service_reporte_tabla import *
from customtkinter import *

class t_view:

    def __init__(self):
        
        self.w = 700
        self.h = 400

        self.app.geometry(f"{self.w}x{self.h}")

        title_frame = CTkLabel(self.app, text=self.title, font=("", 40))
        title_frame.pack(padx=1, pady=3)
        display_frame = self.data_display_frame(self.app)
        crud_display(self.app,
                                          self.repo.insert, 
                                          self.repo.read, 
                                          self.repo.update, 
                                          self.repo.delete, 
                                          self.repo.read_max_reg, 
                                          self.repo.read_min_reg,
                                          self.repo.get_atributes,
                                          self.repo.get_pk_atribute,
                                          self.s_reporte_tabla.generate_document,
                                          [display_frame])