from customtkinter import *
from View.Frames.t_display import *

class t_clientes_display(t_display):

    def __init__(self, app, tipos_cliente):

        frame = CTkFrame(app)
        frame.pack(fill="x", padx=1, pady=1)
        self.combo_maps = tipos_cliente
        print(self.combo_maps)

        # Create elements

        elements = []
        elements_types = []
        
        label_codigo = CTkLabel(frame, text= "Codigo:")
        entry_codigo = CTkEntry(frame, placeholder_text="Codigo Cliente")
        label_mensaje_codigo = CTkLabel(frame, text="")
        elements_types.append("num")
        elements.append((label_codigo, entry_codigo,label_mensaje_codigo))

        label_nombre = CTkLabel(frame, text= "Tipo Cliente:")
        entry_nombre = CTkComboBox(frame, values=(tuple(tipos_cliente.keys())))
        label_mensaje_nombre = CTkLabel(frame, text="")
        elements_types.append("combo")
        elements.append((label_nombre, entry_nombre, label_mensaje_nombre))

        super().__init__(elements, elements_types)
        
        

def main():
    pass
 
if __name__ == "__main__":
    main()