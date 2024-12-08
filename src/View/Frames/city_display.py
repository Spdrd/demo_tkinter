import customtkinter as ctk
from Entities import City

class city_display():

    def __init__(self, app: ctk.CTk):

        frame = ctk.CTkFrame(app)
        frame.pack(fill="y", side="left", padx=1)

        # Create elements

        elements = []
        
        self.code_label = ctk.CTkLabel(frame, text= "Codigo:")
        self.code_entry = ctk.CTkEntry(frame, placeholder_text="Codigo de la ciudad")
        elements.append((self.code_label, self.code_entry))

        self.name_label = ctk.CTkLabel(frame, text= "Ciudad:")
        self.name_entry = ctk.CTkEntry(frame, placeholder_text="Nombre de la ciudad")
        elements.append((self.name_label, self.name_entry))
        for i in range(len(elements)):
            elements[i][0].grid(row=i, column=0, padx=10, pady=10)
            elements[i][1].grid(row=i, column=1, padx=10, pady=10)
    
    def get_info(self):
        return City.City(self.name_entry.get(), code=self.code_entry.get())

if __name__ == "__main__":
    app = ctk.CTk()
    city_display(app)
    app.mainloop()