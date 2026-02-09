import pandas as pd
from pathlib import Path
import os

class ANSTransform :

    def __init__(self):
        self.dir = "demostrativos_contabeis"
        self.chunk_size = 5000



    def existe_dir(self):

        pasta = self.dir

        if not os.path.isdir(pasta):
            print("Diretório inexistente, obtenha os arquivos")
            return False

        elif not os.listdir(pasta):
            print("Diretório vazio, não há arquivos")
            return False

        return True

    def filtrar_arquivos(self):

        # Armazena os arquivos processados antes de uní-los
        arquivos_filtrados = []

        pasta = self.dir

        if not self.existe_dir():
            return None

        print("Filtrando arquivos extraídos...")

        for arquivo in os.listdir(pasta) :

            caminho = os.path.join(pasta, arquivo)

            extensao = Path(arquivo).suffix


            try:

                if extensao in [".csv", ".txt"] :


                    #Identifica qual separador está sendo utilizado
                    try:
                        with open(caminho, 'r', encoding='utf-8') as f:

                            primeira_linha = f.readline()

                            if ';' in primeira_linha:
                                sep = ';'
                            elif ',' in primeira_linha:
                                sep = ','
                            elif '\t' in primeira_linha:
                                sep = '\t'
                            else:
                                sep = ','
                    except:
                        sep = ';'

                    with pd.read_csv(caminho, sep=sep, encoding="utf-8", chunksize=self.chunk_size) as r:

                        for i, chunk in enumerate(r):

                            #Remove espaços e garante que as colunas sejam maiúsculas
                            chunk.columns = [c.strip().upper() for c in chunk.columns]

                            if 'DESCRICAO' in chunk.columns :

                                dado_filtrado = chunk[
                                    chunk['DESCRICAO'].astype(str).str.contains("Eventos / Sinistros", case=False, na=False)]

                                #Se retornou algo, adiciona na lista
                                arquivos_filtrados.append(dado_filtrado)

                                print(f"Arquivo: {arquivo} Filtrado!")

                elif extensao == ".xlsx":

                    df = pd.read_excel(caminho)
                    df.columns = [c.strip().upper() for c in df.columns]

                    if "DESCRICAO" in df.columns:

                        dado_filtrado = df[
                            df["DESCRICAO"].astype(str).str.contains("Eventos / Sinistros", case=False, na=False)]

                        if not dado_filtrado.empty:
                            arquivos_filtrados.append(dado_filtrado)

            except Exception as e:
                print(f"Erro ao filtra o arquivo {arquivo}: {e}")
                continue

        return arquivos_filtrados

    def concatenar_arquivos(self):

        arquivos_filtrados = self.filtrar_arquivos()

        df = pd.concat(arquivos_filtrados, ignore_index=True)

        df.to_csv("data_concat", index=False, encoding="utf-8")
