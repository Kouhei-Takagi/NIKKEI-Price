from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import os

input = './20220110_NIKKEI/pdf/'

def pdf2text(yearMonth, yearMonthDay):
    input_path = f'./20220110_NIKKEI/pdf/{yearMonth}/{yearMonthDay}-m.pdf'
    output_path = f'./20220110_NIKKEI/pdf/{yearMonth}/{yearMonthDay}-m.txt'

    manager = PDFResourceManager()

    with open(output_path, "wb") as output:
        with open(input_path, 'rb') as input:
            with TextConverter(manager, output, codec='utf-8', laparams=LAParams()) as conv:
                interpreter = PDFPageInterpreter(manager, conv)
                for page in PDFPage.get_pages(input):
                    interpreter.process_page(page)

for i in range(32):
    if i < 10:
        ym = '202110'
        ymd = f'21100{i}'
        input_file = f'{input}{ym}/{ymd}-m.pdf'
        if(os.path.exists(input_file)):
            pdf2text(ym, ymd)
    else:
        ym = '202110'
        ymd = f'2110{i}'
        input_file = f'{input}{ym}/{ymd}-m.pdf'
        if(os.path.exists(input_file)):
            pdf2text(ym, ymd)
else:
    print('FINISH!')