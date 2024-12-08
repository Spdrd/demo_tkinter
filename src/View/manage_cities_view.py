import customtkinter as ctk
from PIL import Image
from Frames import city_display
from Frames import crud_display

# Instance View
app = ctk.CTk()
app.title("Ciudades")

ancho = 380
alto = 400

app.geometry(f"{ancho}x{alto}")
city_display_frame = city_display.city_display(app)
crud_display_frame = crud_display.crud_display(app)

app.mainloop()