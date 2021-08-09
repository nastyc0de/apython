from fpdf import FPDF
from datetime import datetime


class PdfReport:
    def __init__(self, filename):
        self.filename = filename

    def generate(mate1, mate2, bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        data = datetime.now().strftime('%c')
        # adding some text
        pdf.set_font(family='Times', size=20, style='B')
        # insert title
        pdf.cell(w=0, h=80, txt='Flatmates Bill',align='C', ln=1)
        pdf.cell(w=0, h=40, txt=f'Fecha: {data}', border=0, align='C')
        pdf.cell(w=0, h=40, txt=f'Mes a pagar: {bill.period}', border=0, align='C')
        
        return pdf.output(self.filename)
