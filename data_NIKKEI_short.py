import PyPDF2
with open('./20220110_NIKKEI/pdf/220104-me.pdf', 'rb') as f:
    reader = PyPDF2.PdfFileReader(f)
    page = reader.getPage(0)
    print(page.extractText())