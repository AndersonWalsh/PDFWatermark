import PyPDF2
import sys

inputs = sys.argv[1:]

files = list()

for file in inputs:
    if file == inputs[len(inputs) - 1]:
        break
    try:
        files.append(open(file, "rb"))
    except FileNotFoundError:
        print(f'File {file} not found')

try:
    wtr_mark = open(inputs[len(inputs) - 1], 'rb')
    wtr_mark = PyPDF2.PdfFileReader(wtr_mark)
    wtr_mark = wtr_mark.getPage(0)
except FileNotFoundError:
    print('Watermark not found')
    raise
print(wtr_mark)
print(inputs[len(inputs) - 1])

for file in files:
    old_pdf = PyPDF2.PdfFileReader(file)
    wtr_pdf = PyPDF2.PdfFileWriter()
    for page_num in range(old_pdf.numPages):
        page = old_pdf.getPage(page_num)
        page.mergePage(wtr_mark)
        wtr_pdf.addPage(page)
    wtr_pdf.write(open(f'wtr_{file.name}.pdf', 'wb'))