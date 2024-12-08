import customtkinter as ctk
from PIL import Image

class crud_display:

    def __init__(self, app: ctk.CTk):

        frame = ctk.CTkFrame(app)
        frame.pack(fill="y", side="left")

        elements = []

        plus_icon = Image.open("src\View\Icons\plus_icon.png")
        button_create = ctk.CTkButton(frame, text="Crear Ciudad",image=ctk.CTkImage(plus_icon), corner_radius=32)
        elements.append(button_create)

        minus_icon = Image.open("src\View\Icons\minus_icon.png")
        button_delete = ctk.CTkButton(frame, text="Eliminar Ciudad",image=ctk.CTkImage(minus_icon), corner_radius=32)
        elements.append(button_delete)

        first_icon = Image.open(r"src\View\Icons\first_icon.png")
        button_first = ctk.CTkButton(frame, text="Primera Ciudad",image=ctk.CTkImage(first_icon), corner_radius=32)
        elements.append(button_first)

        up_icon = Image.open(r"src\View\Icons\up_icon.png")
        button_up = ctk.CTkButton(frame, text="Anterior Ciudad",image=ctk.CTkImage(up_icon), corner_radius=32)
        elements.append(button_up)
        
        browse_icon = Image.open("src\View\Icons\lines_icon.png")
        button_browse = ctk.CTkButton(frame, text="Buscar Ciudad",image=ctk.CTkImage(browse_icon), corner_radius=32)
        elements.append(button_browse)

        down_icon = Image.open("src\View\Iconsdown_icon.png")
        button_down = ctk.CTkButton(frame, text="Siguiente Ciudad",image=ctk.CTkImage(down_icon), corner_radius=32)
        elements.append(button_down)

        browse_icon = Image.open("src\View\Icons\lines_icon.png")
        button_browse = ctk.CTkButton(frame, text="Siguiente Ciudad",image=ctk.CTkImage(browse_icon), corner_radius=32)
        elements.append(button_browse)

        for i in range(len(elements)):
            elements[i].grid(row=i, column=0, padx=10, pady=10)





if __name__ == "__main__":
    app = ctk.CTk()
    crud_display(app)
    app.mainloop()