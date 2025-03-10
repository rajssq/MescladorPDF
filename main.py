import PyPDF2
import os

merger = PyPDF2.PdfMerger()

lista_pdfs = os.listdir("pdfs")
lista_pdfs.sort() # organiza a ordem caso precise

for pdf in lista_pdfs:
    if ".pdf" in pdf:
        merger.append(f"pdfs/{pdf}")

merger.write("PDF Mesclado.pdf")