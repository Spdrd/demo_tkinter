from fpdf import FPDF

class service_reporte_tabla:

    def __init__(self, table_name, atributes):

        self.table_name = table_name
        self.atributes = atributes

    def generate_document(self, data):

        # Crear un objeto FPDF
        pdf = FPDF()
        pdf.add_page()

        # Configurar fuente
        pdf.set_font("Arial", size=12)

        # Agregar texto
        pdf.cell(200, 10, txt=self.table_name, ln=True, align="C")
        print(self.atributes)
        for atribute in self.atributes:
            pdf.cell(40, 10, str(atribute), border=1)
        
        pdf.ln()
        # Agregar filas
        for row in data:
            for i in range(len(row)):
                pdf.cell(40, 10, str(row[i]), border=1)
            pdf.ln()


        # Guardar el archivo
        nombre_pdf = "reporte.pdf"
        pdf.output(nombre_pdf)

        print(f"PDF generado: {nombre_pdf}")

def main():
    service_reporte_tabla("tabla", ("a", "b", "c")).generate_document([[1,2,3],[1,2,4]])

if __name__ == "__main__":
    main()
