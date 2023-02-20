from docx import Document
from openpyxl import load_workbook
from docx.oxml.ns import qn
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx2pdf import convert



convert(r'40 Python works\12. Create a program that automatically generates a certificate by importing information from Excel\수료증양식.docx',
r'40 Python works\12. Create a program that automatically generates a certificate by importing information from Excel\수료증양식.pdf')


