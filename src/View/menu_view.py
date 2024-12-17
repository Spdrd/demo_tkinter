import customtkinter as ctk
from View.t_ciudades_view import *
class menu_view():

    def __init__(self):
        # Crear la ventana principal
        self.app = ctk.CTk()
        self.app.geometry("400x300")
        self.app.title("Ejemplo de ComboBox con Botón")

        # Etiqueta para el título
        titulo_label = ctk.CTkLabel(self.app, text="Selecciona una opción", font=("Arial", 18))
        titulo_label.pack(pady=20)

        # Opciones para el ComboBox
        self.opciones = ["CIIU", "Ciudades", "Oficinas", "Países", "Segmentos", "Tipos de Cliente"]

        # Crear el ComboBox
        self.combobox = ctk.CTkComboBox(self.app, values=self.opciones)
        self.combobox.pack(pady=10)

        # Etiqueta para confirmar la selección
        self.confirmacion_label = ctk.CTkLabel(self.app, text="", font=("Arial", 14))
        self.confirmacion_label.pack(pady=20)

        # Crear el botón para confirmar
        boton_confirmar = ctk.CTkButton(self.app, text="Confirmar selección", command=self.confirmar_seleccion)
        boton_confirmar.pack(pady=10)



        # Ejecutar la aplicación
        self.app.mainloop()

# Función para confirmar la selección al presionar el botón
    def confirmar_seleccion(self):
        seleccion = self.combobox.get()
        print(seleccion)
        if seleccion == "Ciudades":
            self.confirmacion_label.configure(text=f"Abriendo: {seleccion}")
            t_ciudades_view()

        else:
            self.confirmacion_label.configure(text="No has seleccionado nada.")
