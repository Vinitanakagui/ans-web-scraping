from urllib.parse import urljoin
import requests as rq
from bs4 import BeautifulSoup
import os
import re
import zipfile


class ANSExtract:

    def __init__(self, url_base):
        self.url_base = url_base
        self.dir = "demostrativos_contabeis"

    # Obtém todos os links da página
    def obter_links(self, url):

        try:
            response = rq.get(url, timeout=30)

            # Verifica se houve resposta do servidor
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'html.parser')

            # Filtra os links, removendo os que não sejam do diretório atual
            links_filter = []

            for a in soup.find_all('a'):

                if a['href'] not in ['../', '/']:
                    links_filter.append(a['href'])

            return links_filter

        except Exception as e:
            print(f"Erro ao acessar o site {self.url_base}: ", e)
            return []

    # Filtra apenas os links relacionados aos anos
    @staticmethod
    def obter_anos_links(links):
        anos_links = []

        for a in links:

            if re.match(r'^\d{4}/?$', a):
                anos_links.append(a)

        return anos_links

    @staticmethod
    def extrair_info_trim(texto):

        match = re.search(r'(\d)T', texto, re.IGNORECASE)

        if match:
            return int(match.group(1))
        return None

    def obter_trimestres(self, qntd_trimestres):

        # 1. Obtém todos os links da página, a partir da URL base
        links = self.obter_links(self.url_base)

        # 2. Obtém apenas os anos
        anos = sorted(self.obter_anos_links(links), reverse=True)

        trim_encontrados = set()
        trim_baixar = []

        for ano in anos:

            url_ano = urljoin(self.url_base, ano)
            ano_str = ano.replace('/', '')

            # Obtém os conteúdos presentes na "url_ano" e os ordenam em ordem decrescente
            conteudo = sorted(self.obter_links(url_ano), reverse=True)

            for conteudo in conteudo:

                if len(trim_encontrados) == qntd_trimestres:
                    return trim_baixar

                url_trim = urljoin(url_ano, conteudo)
                trim_num = self.extrair_info_trim(conteudo)

                # 1. Cenário: o item já é o ZIP
                if conteudo.lower().endswith(".zip"):

                    if trim_num:
                        key = f"{ano_str}-{trim_num}"

                        if key not in trim_encontrados:
                            trim_encontrados.add(key)
                            trim_baixar.append({
                                'ano': ano_str,
                                'trim': str(trim_num),
                                'url': url_trim,

                            })
                # 2. Cenário: O item é uma subpasta
                elif conteudo.endswith('/'):

                    if trim_num:

                        # Acessa a pasta para obter os conteúdos
                        conteudo_trim = self.obter_links(url_trim)

                        # Retorna apenas os ZIPS
                        zips = [zips for zips in conteudo_trim if zips.lower().endswith(".zip")]

                        if zips:
                            # Obtém o primeiro ZIP encontrado
                            url_zip = urljoin(url_trim, zips[0])
                            key = f"{ano_str}-{trim_num}"

                            if key not in trim_encontrados:
                                trim_encontrados.add(key)
                                trim_baixar.append({
                                    'ano': ano_str,
                                    'trim': str(trim_num),
                                    'url': url_zip
                                })

            if len(trim_encontrados) == qntd_trimestres:
                return trim_baixar

        return trim_baixar

    def baixar_arquivos(self, trimestres):

        # Verifica se o diretório existe, caso não, cria
        os.makedirs(self.dir, exist_ok=True)

        # Baixa os arquivos por chunks
        for trim in trimestres:

            nome_arquivo = f"{trim['ano']}_{trim['trim']}T.zip"
            caminho_completo = os.path.join(self.dir, nome_arquivo)

            print(f"Baixando: {nome_arquivo}...")

            try:

                with rq.get(trim['url'], stream=True, timeout=30) as r:

                    r.raise_for_status()

                    with open(caminho_completo, 'wb') as f:
                        for chunk in r.iter_content(chunk_size=8192):
                            f.write(chunk)

                print(f"Arquivo {nome_arquivo} baixado com sucesso!")

            except Exception as e:

                print(f"Erro ao baixar {trim['url']}: {e}")

    def existe_dir(self):

        pasta = self.dir

        if not os.path.isdir(pasta):
            print("Diretório inexistente, obtenha os arquivos")
            return False

        elif not os.listdir(pasta):
            print("Diretório vazio, não há arquivos")
            return False

        return True

    def extrair_arquivos(self):

        pasta = self.dir

        if not self.existe_dir():
            return

        for arquivo in os.listdir(pasta):
            caminho_zip = os.path.join(pasta, arquivo)

            with zipfile.ZipFile(caminho_zip) as zip_ref:
                zip_ref.extractall(pasta)

            print(f"Arquivo: {arquivo} extraido com sucesso")











