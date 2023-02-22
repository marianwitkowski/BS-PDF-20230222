
# parsowanie danych tabelarycznych
import tabula

#df1 = tabula.read_pdf("pdf/tabele.pdf", pages="all") # "2" ; "2,3,5" ; "2-10"
df1 = tabula.read_pdf("http://51.91.120.89/extras/autos.pdf", pages="1")
print(df1)

# konwersja do CSV
tabula.convert_into("pdf/tabele.pdf", "output.csv", output_format="csv", pages="all")
# konwersja do JSON
tabula.convert_into("pdf/tabele.pdf", "output.json", output_format="json", pages="all")

# konwersja batch'owa
tabula.convert_into_by_batch("pdf/", output_format="csv", pages="all")