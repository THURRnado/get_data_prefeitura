from login_prefeitura import login_prefeitura
from process_prefeitura import get_pdf
from csv_extractor import csv_reader

# im_de_teste = 1484176

try:

    im = '1484176'

    #get_pdf(im)

    csv_reader(csv=r'media\csv\Relatório da consulta.csv')

except Exception as e:

    print(f"Houve o seguinte erro: {str(e)}")