from fpdf import FPDF

class PDFGenerator:
    def __init__(self, filename):
        self.filename = filename

    def generate_pdf(self, content):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, content)
        pdf.output(self.filename)

