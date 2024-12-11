import customtkinter as ctk
from PIL import Image
from Entities import City
from View.Frames import table_display

w_buttons = 100

class crud_display:

    def __init__(self, 
                 app: ctk.CTk, 
                 c_func, 
                 r_func, 
                 u_func, 
                 d_func, 
                 max_id_func, 
                 min_id_func,
                 table_atributes_func, 
                 display):

        self.on_id = -1
        self.min_id_func = min_id_func
        self.max_id_func = max_id_func
        self.check_min_max()

        frame = ctk.CTkFrame(app)
        frame.pack(fill="y", side="left")

        elements = []

        plus_icon = Image.open("src\View\Icons\plus_icon.png")
        button_create = ctk.CTkButton(frame, 
                                      text="Crear Ciudad",
                                      image=ctk.CTkImage(plus_icon), 
                                      corner_radius=32, 
                                      width=w_buttons, 
                                      command=lambda: self.on_create(c_func, display[0]))
        elements.append(button_create)

        update_icon = Image.open(r"src\View\Icons\update_icon.png")
        button_update = ctk.CTkButton(frame, 
                                      text="Actualizar Ciudad",
                                      image=ctk.CTkImage(update_icon), 
                                      corner_radius=32, 
                                      width=w_buttons, 
                                      command=lambda: u_func(display[0].get_info()))
        elements.append(button_update)

        minus_icon = Image.open("src\View\Icons\minus_icon.png")
        button_delete = ctk.CTkButton(frame, 
                                      text="Eliminar Ciudad",
                                      image=ctk.CTkImage(minus_icon), 
                                      corner_radius=32, 
                                      width=w_buttons, 
                                      command=lambda: self.on_delete(d_func, display[0]))
        elements.append(button_delete)

        first_icon = Image.open(r"src\View\Icons\first_icon.png")
        button_first = ctk.CTkButton(frame, 
                                     text="Primera Ciudad",
                                     image=ctk.CTkImage(first_icon), 
                                     corner_radius=32, 
                                     width=w_buttons, 
                                     command=lambda: self.on_first(r_func, display[0]))
        elements.append(button_first)

        up_icon = Image.open(r"src\View\Icons\up_icon.png")
        button_up = ctk.CTkButton(frame, 
                                  text="Anterior Ciudad",
                                  image=ctk.CTkImage(up_icon), 
                                  corner_radius=32, width=w_buttons, 
                                  command= lambda: self.on_back(r_func, display[0]))
        elements.append(button_up)
        
        browse_icon = Image.open("src\View\Icons\lines_icon.png")
        button_browse = ctk.CTkButton(frame, 
                                      text="Buscar Ciudad",
                                      image=ctk.CTkImage(browse_icon), 
                                      corner_radius=32, 
                                      width=w_buttons,
                                      command=lambda: self.on_browse(table_atributes_func, r_func))
        elements.append(button_browse)

        down_icon = Image.open("src\View\Icons\down_icon.png")
        button_down = ctk.CTkButton(frame, text="Siguiente Ciudad",
                                    image=ctk.CTkImage(down_icon), 
                                    corner_radius=32, width=w_buttons, 
                                    command=lambda: self.on_next(r_func, display[0]))
        elements.append(button_down)

        last_icon = Image.open("src\View\Icons\last_icon.png")
        button_last = ctk.CTkButton(frame, text="Ultima Ciudad",
                                    image=ctk.CTkImage(last_icon), 
                                    corner_radius=32, 
                                    width=w_buttons, 
                                    command=lambda: self.on_last(r_func, display[0]))
        elements.append(button_last)

        for i in range(len(elements)):
            elements[i].grid(row=i, column=0, padx=10, pady=10)

    def check_min_max(self):
        self.min_id = self.min_id_func()
        self.max_id = self.max_id_func()

    def on_create(self, func, display):
        func(display.get_info())
        self.check_min_max()
    
    def on_delete(self, func, display):
        func(code=display.get_code())
        self.check_min_max()

    def on_first(self, func, display):
        data = func(id="first")
        self.on_id = data[0]
        display.set_info(data[1])
        

    def on_last(self, func, display):
        data = func(id="last")
        self.on_id = data[0]
        display.set_info(data[1])

    def on_back(self, func, display):
        id = self.on_id
        while True:
            if id == -1:
                id = 1
            elif not id == self.min_id:
                id -= 1
            data = func(id=id)
            if not data == -1:
                break

        self.on_id = data[0]
        display.set_info(data[1])

    def on_next(self, func, display):
        id = self.on_id
        while True:
            if id == -1:
                id = 1
            elif not id == self.max_id:
                id += 1
            data = func(id=id)
            if not data == -1:
                break

        self.on_id = data[0]
        display.set_info(data[1])

    def on_browse(self, head_func, data_func):
        dialog = ctk.CTk()
        dialog.title("Tabla Ciudades")
        headings = head_func()
        data = data_func()[0]
        print(f"headings: {headings}")
        print(f"data: {data}")
        frame = table_display.table_display(dialog, headings, data)
        dialog.mainloop()


def main():
    app = ctk.CTk()
    crud_display(app)
    app.mainloop()


if __name__ == "__main__":
    main()