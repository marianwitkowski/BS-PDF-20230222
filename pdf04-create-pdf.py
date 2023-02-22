
# Tworzenie plików PDF
from io import BytesIO
from PyPDF2 import PdfWriter, PdfReader

from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfgen import canvas

from reportlab.platypus import Frame, Paragraph, SimpleDocTemplate, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch, cm

# utworzenie obiektu PdfWriter
output_pdf = PdfWriter()

# Tworzenie nową stronę A4
c = canvas.Canvas("tmp.pdf", pagesize=A4 )

# Dodawanie tekstu do strony
c.drawString(10, 800, "Hello, Google!")

textobject = c.beginText()
textobject.setTextOrigin(100, 750)

textobject.setFont("Helvetica", 14)
textobject.textLine("Tekst linia 1 ")

textobject.setFont("Helvetica-Bold", 14)
textobject.textLine("Tekst linia 2")

textobject.setFont("Helvetica", 14)
textobject.textLine("Tekst linia 3")

c.drawText(textobject)

# Przykładowy długi tekst
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae metus sed velit malesuada molestie eu eu orci. Nam ac metus eget nisi congue porttitor. Morbi vestibulum diam nec metus consequat, vel bibendum lectus efficitur. Nulla quis fringilla augue. Duis ullamcorper suscipit sapien, eget suscipit turpis luctus vel."

# Tworzenie obiektu Canvas i dodawanie tekstu
styles = getSampleStyleSheet()
style = styles["Normal"]
style.textColor = HexColor("#00FF00")
style.fontSize = 20
style.leading = 22
style.alignment = 1  # 0 = lewo, 1 = środek, 2 = prawo

frame = Frame(inch, inch, 6*inch, 4*inch, showBoundary=1)
paragraph = Paragraph(text, style)
frame.addFromList([paragraph], c)

c.save()

# Zapisywanie strony do obiektu PdfWriter
pdf_data = BytesIO(c.getpdfdata())
pdf_reader = PdfReader(pdf_data)
page_object = pdf_reader.pages[0]
output_pdf.add_page(page_object)

# dodanie pustej strony
output_pdf.add_blank_page()

#####################################################
# dodanie grafiki
c = canvas.Canvas("tmp.pdf", pagesize=A4)
c.drawImage("cat.jpg", 100, 400, width=400, height=300)

pdf_data = BytesIO(c.getpdfdata())
pdf_reader = PdfReader(pdf_data)
page_object = pdf_reader.pages[0]
output_pdf.add_page(page_object)

#####################################################
# dodanie kształtów
c = canvas.Canvas("tmp.pdf", pagesize=letter)

# Dodawanie prostokąta
c.setFillColor(colors.blue)
c.rect(1*inch, 5*inch, 2*inch, 1*inch, fill=True)

# Dodawanie elipsy
c.setFillColor(colors.red)
c.ellipse(4*inch, 5*inch, 3*inch, 2*inch, fill=True)

# Dodawanie okregu
c.setFillColor(colors.gray)
c.circle(7*inch, 7*inch, 1*inch, fill=True)

pdf_data = BytesIO(c.getpdfdata())
pdf_reader = PdfReader(pdf_data)
page_object = pdf_reader.pages[0]
output_pdf.add_page(page_object)

#####################################################
# dodanie grida
c = canvas.Canvas("tmp.pdf", pagesize=A4)
w, h = A4
xlist = [10, 60, 110, 160]
ylist = [h - 10, h - 60, h - 110, h - 160]
c.grid(xlist, ylist)

pdf_data = BytesIO(c.getpdfdata())
pdf_reader = PdfReader(pdf_data)
page_object = pdf_reader.pages[0]
output_pdf.add_page(page_object)

#################################
# dodanie tabeli z wartościami

doc = SimpleDocTemplate("tmp.pdf", pagesize=letter)
elements = []

data= [['00', '01', '02', '03', '04'],
['10', '11', '12', '13', '14'],
['20', '21', '22', '23', '24'],
['30', '31', '32', '33', '34']]

t=Table(data,5*[0.4*inch], 4*[0.4*inch])
t.setStyle(TableStyle([('ALIGN',(1,1),(-2,-2),'RIGHT'),
('TEXTCOLOR',(1,1),(-2,-2),colors.red),
('VALIGN',(0,0),(0,-1),'TOP'),
('TEXTCOLOR',(0,0),(0,-1),colors.blue),
('ALIGN',(0,-1),(-1,-1),'CENTER'),
('VALIGN',(0,-1),(-1,-1),'MIDDLE'),
('TEXTCOLOR',(0,-1),(-1,-1),colors.green),
('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
('BOX', (0,0), (-1,-1), 0.25, colors.black),
]))
elements.append(t)
doc.build(elements)

pdf_data = BytesIO(doc.canv.getpdfdata())
pdf_reader = PdfReader(pdf_data)
page_object = pdf_reader.pages[0]
output_pdf.add_page(page_object)

#####################################################
output_pdf.encrypt(user_password="xyz", owner_pwd=None, use_128bit=True)
# zapis na koncu wszystkiego do wynikowego pliku PDF
with open("output.pdf", "wb") as out_file:
    output_pdf.write(out_file)
