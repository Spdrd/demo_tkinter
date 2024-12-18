import tkinter as tk
from Entities import Persona as p
from Services import service_reporte_tabla

personas = []

# Ventana
ventana = tk.Tk()

# Labels / Entrys
titulo_pagina = tk.Label(ventana, text="Ingresar Persona")

titulo_nombre = tk.Label(ventana, text="Nombre: ")
input_nombre = tk.Entry(ventana, width=30)

titulo_apellido = tk.Label(ventana, text="Apellido: ")
input_apellido = tk.Entry(ventana, width=30)

visualisar_nombre = tk.Label(ventana, text="Nombre ingresado: ")
visualisar_apellido = tk.Label(ventana, text="Apellido ingresado: ")

# Funciones Botones
def obtener_datos():

    contenido_nombre = input_nombre.get()
    contenido_apellido = input_apellido.get()

    visualisar_nombre.config(text=f"Nombre ingresado: {contenido_nombre}")
    visualisar_apellido.config(text=f"Nombre ingresado: {contenido_apellido}")

    print(contenido_nombre)
    print(contenido_apellido)

    personas.append(p.Persona(contenido_nombre, contenido_apellido).to_arr())
    service_reporte_tabla.generar_reporte(personas)

# Buttons
boton_ingresar = tk.Button(
    ventana, 
    text="Ingresar", 
    command=obtener_datos
    )

def pantalla():
    # Crear la ventana principal

    # Crear algunos widgets
    
    # Usar el método grid para posicionar los widgets en la cuadrícula
    titulo_pagina.grid(row=0, column=0, padx=10, pady=10)

    titulo_nombre.grid(row=1, column=0, padx=10, pady=10)
    input_nombre.grid(row=1, column=1, padx=10, pady=10)
    
    titulo_apellido.grid(row=2, column=0, padx=10, pady=10)
    input_apellido.grid(row=2, column=1, padx=10, pady=10)

    boton_ingresar.grid(row=3, column=2, padx=10, pady=10)

    visualisar_nombre.grid(row=4, column=0, padx=10, pady=10)
    visualisar_apellido.grid(row=5, column=0, padx=10, pady=10)




    # Ejecutar el bucle principal
    ventana.mainloop()
