from PyPDF2 import PdfWriter

merger = PdfWriter()
pdfs = []

n = int(input("Số file muốn ghép: \n"))

for i in range(0, n):
    name = input(f"Nhập file số {i+1}: ")
    pdfs.append(f"Project/{name}")

for pdf in pdfs:
    merger.append(pdf)

merger.write("Project/merge-pdf.pdf")

merger.close()
