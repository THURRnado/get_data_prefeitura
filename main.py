from login_prefeitura import login_prefeitura
from process_prefeitura import get_pdf

# im_de_teste = 1484176

try:

    im = '1484176'

    get_pdf(im)

except Exception as e:

    print(f"Houve o seguinte erro: {e}")