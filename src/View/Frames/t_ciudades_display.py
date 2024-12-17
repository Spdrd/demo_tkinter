from customtkinter import *
from View.Frames.t_display import *

class t_ciudades_display(t_display):

    def __init__(self, app):

        frame = CTkFrame(app)
        frame.pack(fill="x", padx=1, pady=1)

        # Create elements

        elements = []
        elements_types = []
        
        label_codigo = CTkLabel(frame, text= "Codigo:")
        entry_codigo = CTkEntry(frame, placeholder_text="Codigo de la ciudad")
        label_mensaje_codigo = CTkLabel(frame, text="")
        elements_types.append("num")
        elements.append((label_codigo, entry_codigo,label_mensaje_codigo))

        label_nombre = CTkLabel(frame, text= "Ciudad:")
        entry_nombre = CTkEntry(frame, placeholder_text="Nombre de la ciudad")
        label_mensaje_nombre = CTkLabel(frame, text="")
        elements_types.append("str")
        elements.append((label_nombre, entry_nombre, label_mensaje_nombre))

        super().__init__(elements, elements_types)
        
        

def main():
    pass
 
if __name__ == "__main__":
    main()