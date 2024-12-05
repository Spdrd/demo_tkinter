from fpdf import FPDF

# Crear un objeto FPDF
pdf = FPDF()
pdf.add_page()

# Configurar fuente
pdf.set_font("Arial", size=12)

# Agregar texto
pdf.cell(200, 10, txt="Hola, este es un PDF generado con FPDF.", ln=True, align="C")

# Agregar otra línea de texto
pdf.cell(200, 10, txt="¡FPDF es fácil de usar!", ln=True, align="C")

ancho = 50

pdf.image("image.png", w = ancho, x = (pdf.w - ancho) / 2)

pdf.cell(40, 10, "Nombre", border=1, align="C")
pdf.cell(40, 10, "Edad", border=1, align="C")
pdf.cell(40, 10, "Ciudad", border=1, align="C")
pdf.ln()  # Salto de línea

# Datos de la tabla
datos = [
    ["Alice", "30", "Bogotá"],
    ["Bob", "25", "Medellín"],
    ["Charlie", "35", "Cali"]
]

# Agregar filas
for fila in datos:
    pdf.cell(40, 10, fila[0], border=1)  # Nombre
    pdf.cell(40, 10, fila[1], border=1)  # Edad
    pdf.cell(40, 10, fila[2], border=1)  # Ciudad
    pdf.ln()  # Salto de línea después de cada fila


# Guardar el archivo
nombre_pdf = "ejemplo_fpdf.pdf"
pdf.output(nombre_pdf)

print(f"PDF generado: {nombre_pdf}")
