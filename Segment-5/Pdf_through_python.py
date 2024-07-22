from fpdf import FPDF

pdf = FPDF(orientation='P',unit='pt',format='A4')

pdf.add_page()

pdf.image('Segment-5/Certificate.jpg',w=10,h=15)

pdf.output('Output.pdf')

print("Pdf generated")