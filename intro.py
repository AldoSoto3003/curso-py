"""Introduccion a python"""

from PyPDF2 import PdfReader

def convertir_pdf_a_texto(pdf_file):
    with open(pdf_file, 'rb') as file:
        reader = PdfReader(file)
        text = ''
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            page.add_transformation()
            text += page.extract_text()
    return text

def guardar_en_txt(pdf_text,txt_path):
    with open(txt_path, 'w', encoding='utf-8') as txt_file:
        txt_file.write(pdf_text)

pdf_path = 'prueba.pdf'
txt_path = 'prueba.txt'

texto = convertir_pdf_a_texto(pdf_path)
guardar_en_txt(texto,txt_path)