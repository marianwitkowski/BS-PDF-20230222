
# Odczytanie pól formularza
from PyPDF2 import PdfReader

reader = PdfReader("pdf/forms.pdf")
fields = reader.get_form_text_fields()
for field in fields:
    print(field)

print("="*100)
fields = reader.get_fields()
for field in fields:
    print(field)