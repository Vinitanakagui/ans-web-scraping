from ans_extract import ANSExtract
from ans_transform import ANSTransform

ans_url = "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/"

if __name__ == '__main__':

    ans_extract = ANSExtract(ans_url)
    ans_transform = ANSTransform()

    #1. Extrai os trimestres da base de dados
    trimestres = ans_extract.obter_trimestres(3)

    #2. Baixa os arquivos dos trimestres encontrados
    ans_extract.baixar_arquivos(trimestres)

    #3. Descompacta os arquivos .zip
    ans_extract.extrair_arquivos()

    #4. Filtra os arquivos extraídos e os concatena
    ans_transform.concatenar_arquivos()



