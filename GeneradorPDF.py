from fpdf import FPDF
import os

class GeneradorPDF:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self.directorio = "facturas"
        if not os.path.exists(self.directorio):
            os.makedirs(self.directorio)

    def generar_factura(self, factura, alumno, clases=None, detalles_pago=None):
        pdf = FPDF()
        pdf.add_page()

        # Encabezado de la factura
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(0, 10, "Factura", 0, 1, 'C')
        pdf.ln(10)

        # Encabezado de la empresa
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(0, 10, "Informática I", 0, 1, 'C')
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 10, "UAX 2025", 0, 1, 'C')
        pdf.cell(0, 10, "Teléfono: 123-456-7890", 0, 1, 'C')
        pdf.cell(0, 10, "Email: ivan.barroso@example.com", 0, 1, 'C')
        pdf.ln(10)

        # Información del alumno
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 10, "Datos del Alumno", 0, 1)
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 10, f"DNI: {alumno.dni}", 0, 1)
        pdf.cell(0, 10, f"Nombre: {alumno.nombre} {alumno.primer_apellido} {alumno.segundo_apellido}", 0, 1)
        pdf.cell(0, 10, f"Fecha de Nacimiento: {alumno.fecha_nacimiento}", 0, 1)
        pdf.cell(0, 10, f"Permiso: {alumno.permiso_opta}", 0, 1)
        pdf.ln(10)

        # Detalles de la factura
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 10, "Detalles de la Factura", 0, 1)
        pdf.set_font("Arial", size=12)
        pdf.cell(40, 10, "Descripción", 1)
        pdf.cell(40, 10, "Cantidad", 1)
        pdf.cell(40, 10, "Precio Unitario", 1)
        pdf.cell(40, 10, "Total (Euros)", 1)
        pdf.ln(10)

        pdf.cell(40, 10, "Matrícula", 1)
        pdf.cell(40, 10, "1", 1)
        pdf.cell(40, 10, f"{factura.precio_matricula}", 1)
        precio_total_matriculas = max(factura.precio_matricula * factura.num_renovaciones, factura.precio_matricula)
        pdf.cell(40, 10, f"{precio_total_matriculas}", 1)
        pdf.ln(10)

        pdf.cell(40, 10, "Clases Incluidas", 1)
        pdf.cell(40, 10, f"{factura.num_clases_incluidas}", 1)
        pdf.cell(40, 10, f"{factura.precio_clase}", 1)
        pdf.cell(40, 10, f"-", 1)
        pdf.ln(10)

        pdf.cell(40, 10, "Clases Dadas", 1)
        pdf.cell(40, 10, f"{factura.num_clases_dadas}", 1)
        pdf.cell(40, 10, f"{factura.precio_clase}", 1)
        clases_excedentes = max(0, factura.num_clases_dadas - factura.num_clases_incluidas)
        pdf.cell(40, 10, f"{clases_excedentes * factura.precio_clase}", 1)
        pdf.ln(10)

        pdf.cell(40, 10, "Exámenes", 1)
        pdf.cell(40, 10, f"{factura.num_examenes}", 1)
        pdf.cell(40, 10, f"{factura.precio_examen}", 1)
        pdf.cell(40, 10, f"{factura.num_examenes * factura.precio_examen}", 1)
        pdf.ln(10)

        pdf.cell(40, 10, "Renovaciones", 1)
        pdf.cell(40, 10, f"{factura.num_renovaciones}", 1)
        pdf.cell(40, 10, f"{factura.precio_renovacion}", 1)
        pdf.cell(40, 10, f"{factura.num_renovaciones * factura.precio_renovacion}", 1)
        pdf.ln(10)

        pdf.cell(40, 10, "Anticipos", 1)
        pdf.cell(40, 10, "1", 1)
        pdf.cell(40, 10, f"{factura.anticipos}", 1)
        pdf.cell(40, 10, f"{factura.anticipos}", 1)
        pdf.ln(10)

        # Detalles de las clases (si se proporcionan)
        if clases:
            pdf.set_font("Arial", 'B', 12)
            pdf.cell(0, 10, "Detalles de las Clases", 0, 1)
            pdf.set_font("Arial", size=12)
            for clase in clases:
                pdf.cell(0, 10, f"Clase con {clase.profesor} el {clase.fecha_hora}", 0, 1)
            pdf.ln(10)


        # Totales
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 10, "Totales (en Euros)", 0, 1)
        pdf.set_font("Arial", size=12)
        pdf.cell(80, 10, "Concepto", 1)
        pdf.cell(80, 10, "Importe", 1)
        pdf.ln(10)
        pdf.cell(80, 10, "Total", 1)
        pdf.cell(80, 10, f"{factura.calcular_total():.2f}", 1)
        pdf.ln(10)
        pdf.cell(80, 10, "IVA (21%)", 1)
        pdf.cell(80, 10, f"{factura.calcular_iva():.2f}", 1)
        pdf.ln(10)
        pdf.cell(80, 10, "Total con IVA", 1)
        pdf.cell(80, 10, f"{factura.calcular_total_con_iva():.2f}", 1)
        pdf.ln(10)
        pdf.cell(80, 10, "Saldo Pendiente", 1)
        pdf.cell(80, 10, f"{factura.calcular_saldo_pendiente():.2f}", 1)
        pdf.ln(10)

        if detalles_pago:
            pdf.set_font("Arial", 'B', 12)
            pdf.cell(0, 10, "Detalles de Pago", 0, 1)
            pdf.set_font("Arial", size=12)
            for clave, valor in detalles_pago.items():
                pdf.cell(0, 10, f"{clave}: {valor}", 0, 1)

        # Guardar el PDF
        ruta_completa = os.path.join(self.directorio, self.nombre_archivo)
        pdf.output(ruta_completa)