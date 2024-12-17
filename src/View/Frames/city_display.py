from customtkinter import *
from Entities.City_demo import *

class city_display():

    def __init__(self, app):

        frame = CTkFrame(app)
        frame.pack(fill="x", padx=1, pady=1)

        # Create elements

        elements = []
        
        self.code_label = CTkLabel(frame, text= "Codigo:")
        self.code_entry = CTkEntry(frame, placeholder_text="Codigo de la ciudad")
        elements.append((self.code_label, self.code_entry))

        self.name_label = CTkLabel(frame, text= "Ciudad:")
        self.name_entry = CTkEntry(frame, placeholder_text="Nombre de la ciudad")
        elements.append((self.name_label, self.name_entry))
        for i in range(len(elements)):
            elements[i][0].grid(row=i, column=0, padx=10, pady=10)
            elements[i][1].grid(row=i, column=1, padx=10, pady=10)

    def get_info(self):
        return City(code=self.code_entry.get(), name=self.name_entry.get())
    
    def get_code(self):
        return self.code_entry.get()
    
    def get_name(self):
        return self.name_entry.get()
    
    def set_info(self, city: City):
        self.code_entry.delete(0, END)
        self.name_entry.delete(0, END)
        self.code_entry.insert(0, city.code)
        self.name_entry.insert(0, city.name)

def main():
    app = CTk()
    view = city_display(app)
    city= City("aa", "bb")
    view.set_info(city)
    app.mainloop()
 
if __name__ == "__main__":
    main()