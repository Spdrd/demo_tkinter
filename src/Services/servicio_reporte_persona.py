from fpdf import FPDF
from Entities import Persona as p

def generar_reporte(datos: dict):

    # Crear un objeto FPDF
    pdf = FPDF()
    pdf.add_page()

    # Configurar fuente
    pdf.set_font("Arial", size=12)

    # Agregar texto
    pdf.cell(200, 10, txt="Titulo", ln=True, align="C")

    # Agregar otra línea de texto
    pdf.cell(200, 10, txt="Subtitulo", ln=True, align="C")

    '''ancho = 50
    pdf.image("image.png", w = ancho, x = (pdf.w - ancho) / 2)'''

    # Agregar filas
    for fila in datos:
        pdf.cell(40, 10, fila[0], border=1)  # Nombre
        pdf.cell(40, 10, fila[1], border=1)  # Edad
        pdf.ln()  # Salto de línea después de cada fila


    # Guardar el archivo
    nombre_pdf = "reporte.pdf"
    pdf.output(nombre_pdf)

    print(f"PDF generado: {nombre_pdf}")
