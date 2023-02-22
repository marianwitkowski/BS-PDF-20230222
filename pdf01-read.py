
# Odczyt zawartości PDF

from PyPDF2 import PdfReader

reader = PdfReader("pdf/programista.pdf")

print(f"Liczba stron: {len(reader.pages)}")
print(reader.metadata) # metadane pliku
print(reader.page_mode) # układ strony
print(reader.outline) # zakładki

# ekstrakcja tekstu
print("="*100)
print(reader.pages[1].extract_text())

# ekstrakcja obrazu
print("="*100)
page = reader.pages[0]
print(f"Znalezionych grafik: {len(page.images)}")
for img in page.images:
    with open(img.name, "wb") as fd:
        fd.write(img.data)

