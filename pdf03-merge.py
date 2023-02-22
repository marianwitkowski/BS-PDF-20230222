
# łączenie plików PDF ze sobą
import glob
from PyPDF2 import PdfReader, PdfMerger

merge = PdfMerger()
files = glob.glob("pdf/*.pdf")
for file in files:
    merge.append( PdfReader(file), pages=(0,1) )

merge.add_outline_item("Test zakładki na stronie nr 1", 0)
merge.write("merged.pdf")
merge.close()

