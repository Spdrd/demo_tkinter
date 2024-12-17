import customtkinter as ctk
from PIL import Image
from View.Frames.table_view import *

w_buttons = 50

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
                 pk_func, 
                 display):

        self.min_id_func = min_id_func
        self.max_id_func = max_id_func
        self.table_atributes_func = table_atributes_func
        self.pk_func = pk_func

        if not self.check_empty(r_func):
            self.check_min_max()
            self.on_id = self.min_id

        frame = ctk.CTkFrame(app)
        frame.pack(fill="x", padx=1, pady=1)

        elements = []

        plus_icon = Image.open(r"src\View\Icons\plus_icon.png")
        button_create = ctk.CTkButton(frame,
                                      text="", 
                                      corner_radius=32, 

                                      image=ctk.CTkImage(plus_icon),
                                      width=w_buttons,
                                      command=lambda: self.on_create(c_func, display[0]))
        elements.append(button_create)

        update_icon = Image.open(r"src\View\Icons\update_icon.png")
        button_update = ctk.CTkButton(frame,
                                      text="",
                                      image=ctk.CTkImage(update_icon), 
                                      corner_radius=32, 
                                      width=w_buttons,
                                      command=lambda: u_func(display[0].get_info()))
        elements.append(button_update)

        minus_icon = Image.open(r"src\View\Icons\minus_icon.png")
        button_delete = ctk.CTkButton(frame,
                                      text="",
                                      image=ctk.CTkImage(minus_icon), 
                                      corner_radius=32, 
                                      width=w_buttons,
                                      command=lambda: self.on_delete(d_func, display[0]))
        elements.append(button_delete)

        first_icon = Image.open(r"src\View\Icons\first_icon.png")
        button_first = ctk.CTkButton(frame,
                                     text="",
                                     image=ctk.CTkImage(first_icon), 
                                     corner_radius=32, 
                                      width=w_buttons,
                                     command=lambda: self.on_first(r_func, display[0]))
        elements.append(button_first)

        up_icon = Image.open(r"src\View\Icons\up_icon.png")
        button_up = ctk.CTkButton(frame,
                                  text="",
                                  image=ctk.CTkImage(up_icon), 
                                  corner_radius=32, 
                                  width=w_buttons,
                                  command= lambda: self.on_back(r_func, display[0]))
        elements.append(button_up)
        
        browse_icon = Image.open(r"src\View\Icons\lines_icon.png")
        button_browse = ctk.CTkButton(frame,
                                      text="", 
                                      image=ctk.CTkImage(browse_icon), 
                                      corner_radius=32,
                                      width=w_buttons,
                                      command=lambda: self.on_browse(table_atributes_func, r_func))
        elements.append(button_browse)

        down_icon = Image.open(r"src\View\Icons\down_icon.png")
        button_down = ctk.CTkButton(frame,
                                    text="",
                                    image=ctk.CTkImage(down_icon), 
                                    corner_radius=32, 
                                    width=w_buttons,
                                    command=lambda: self.on_next(r_func, display[0]))
        elements.append(button_down)

        last_icon = Image.open(r"src\View\Icons\last_icon.png")
        button_last = ctk.CTkButton(frame,
                                    text="",
                                    image=ctk.CTkImage(last_icon), 
                                    corner_radius=32, 
                                    width=w_buttons,
                                    command=lambda: self.on_last(r_func, display[0]))
        elements.append(button_last)

        for i in range(len(elements)):
            elements[i].grid(row=0, column=i, padx=10, pady=10)
    
    def check_empty(self, func):
        is_empty = func() == []
        if is_empty:
            self.on_id = 0
            self.min_id = 0
            self.max_id = 0
    
        return is_empty
    
    def check_min_max(self):
        self.min_id = self.min_id_func()
        self.max_id = self.max_id_func()

    def on_create(self, func, display):
        self.on_id = func(display.get_info())
        self.check_min_max()
    
    def on_delete(self, func, display):
        func(index=display.get_pk(), index_name=self.pk_func())
        self.check_min_max()

    def on_first(self, func, display):
        data = func(index="first")[0]
        print(data)
        self.on_id = data[len(data)-1]
        display.set_info(data)
        

    def on_last(self, func, display):
        data = func(index="last")[0]
        print(data)
        self.on_id = data[len(data)-1]
        display.set_info(data)

    def on_back(self, func, display):
        id = self.on_id
        while True:
            self.check_empty(func)
            if not id == self.min_id:
                id -= 1
            data = func(index=id, index_name="reg")
            print(f"data: {data}")
            if (not data == -1) or id == 0:
                break
        if not id == 0:
            self.on_id = data[len(data)-1]
            display.set_info(data)

    def on_next(self, func, display):
        id = self.on_id
        while True:
            self.check_empty(func)
            if not id == self.max_id:
                id += 1
            data = func(index=id, index_name="reg")
            print(f"data: {data}")
            if (not data == -1) or id == 0:
                break
        if not id == 0:
            self.on_id = data[len(data)-1]
            display.set_info(data)

    def on_browse(self, head_func, data_func):
        dialog = ctk.CTk()
        dialog.title("Tabla Ciudades")
        headings = head_func()
        data = data_func()
        print(f"headings: {headings}")
        print(f"data: {data}")
        frame = table_display(dialog, headings, data)
        dialog.mainloop()


def main():
    app = ctk.CTk()
    crud_display(app)
    app.mainloop()


if __name__ == "__main__":
    main()