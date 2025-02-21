from View.t_ciiu_view import t_ciiu_view
from View.t_ciudades_view import t_ciudades_view
from View.t_oficinas_view import t_oficinas_view
from View.t_paises_view import t_paises_view
from View.t_segmentos_view import t_segmentos_view
from View.t_tipos_cliente_view import t_tipos_cliente_view

from customtkinter import *
class menu_view():

    def __init__(self):
        # Crear la ventana principal
        self.app = CTk()
        self.app.geometry("400x300")
        self.app.title("menu_view")

        # Etiqueta para el título
        titulo_label = CTkLabel(self.app, text="Selecciona una opción", font=("Arial", 18))
        titulo_label.pack(pady=20)

        # Opciones para el ComboBox
        self.opciones = ["CIIU", "Ciudades", "Oficinas", "Paises", "Segmentos", "Tipos de Cliente"]

        # Crear el ComboBox
        self.combobox = CTkComboBox(self.app, values=self.opciones)
        self.combobox.pack(pady=10)

        # Etiqueta para confirmar la selección
        self.confirmacion_label = CTkLabel(self.app, text="", font=("Arial", 14))
        self.confirmacion_label.pack(pady=20)

        # Crear el botón para confirmar
        boton_confirmar = CTkButton(self.app, text="Confirmar selección", command=self.confirmar_seleccion)
        boton_confirmar.pack(pady=10)



        # Ejecutar la aplicación
        self.app.mainloop()

# Función para confirmar la selección al presionar el botón
    def confirmar_seleccion(self):
        
        seleccion = self.combobox.get()
        print(seleccion)
        if seleccion:
            self.confirmacion_label.configure(text=f"Abriendo: {seleccion}")
        if seleccion == "Ciudades":
            t_ciudades_view()
        elif seleccion == "CIIU":
            t_ciiu_view()
        elif seleccion == "Oficinas":
            t_oficinas_view()
        elif seleccion == "Paises":
            t_paises_view()
        elif seleccion == "Segmentos":
            t_segmentos_view()
        elif seleccion == "Tipos de Cliente":
            t_tipos_cliente_view()
        else:
            self.confirmacion_label.configure(text="No has seleccionado nada.")
