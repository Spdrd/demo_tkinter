from reportlab.pdfgen import canvas

contenido = ["cosa1", "cosa2", "cosa3"]

# Crear un archivo PDF
nombre_pdf = "ejemplo_reportlab.pdf"
pdf = canvas.Canvas(nombre_pdf)

# Agregar contenido al PDF

for i in range(len(contenido)):
    pdf.drawString(100, 750 - i * 40, contenido[i])

# Dibujar formas
'''
pdf.rect(50, 700, 200, 100, stroke=1, fill=0)
pdf.line(50, 750, 250, 750)
'''
# Guardar el archivo
pdf.save()

print(f"PDF generado: {nombre_pdf}")
