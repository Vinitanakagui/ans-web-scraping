ANS Data Extractor
Projeto para extração, transformação e análise de dados contábeis da ANS (Agência Nacional de Saúde Suplementar).
📋 Descrição
Este projeto automatiza o processo de:

Download de demonstrativos contábeis da ANS
Extração de arquivos ZIP
Filtragem de dados específicos (Eventos/Sinistros)
Consolidação de múltiplos trimestres em um único arquivo

🚀 Funcionalidades

Extração Automática: Baixa demonstrativos contábeis de trimestres específicos
Processamento Inteligente: Identifica automaticamente separadores em arquivos CSV
Filtragem de Dados: Filtra apenas informações relacionadas a "Eventos / Sinistros"
Consolidação: Concatena dados de múltiplos trimestres em um único arquivo

📦 Instalação
Pré-requisitos

Python 3.7 ou superior

Passos de Instalação

Clone ou baixe este repositório
Instale as dependências:

bashpip install -r requirements.txt

💻 Uso
Execute o script principal:
bashpython main.py
O que o script faz:

Busca os últimos 3 trimestres de dados disponíveis
Baixa os arquivos ZIP para a pasta demostrativos_contabeis/
Extrai os arquivos automaticamente
Filtra dados relacionados a "Eventos / Sinistros"
Gera o arquivo consolidado data_concat.csv


Personalização
Para alterar a quantidade de trimestres a serem baixados, edite a linha no arquivo main.py:
pythontrimestres = ans_extract.obter_trimestres(3)  # Altere o número aqui

🔧 Componentes
ANSExtract (ans_extract.py)
Responsável por:

Navegar na estrutura de diretórios da ANS
Identificar trimestres disponíveis
Baixar arquivos ZIP
Extrair arquivos compactados

ANSTransform (ans_transform.py)
Responsável por:

Detectar tipos de arquivo (CSV, TXT, XLSX)
Identificar separadores automaticamente
Filtrar dados específicos
Concatenar múltiplos arquivos

📊 Saída
O arquivo final data_concat.csv contém todos os dados filtrados de "Eventos / Sinistros" dos trimestres processados.
🛠️ Tecnologias Utilizadas

requests: Download de arquivos
BeautifulSoup4: Parsing de HTML
pandas: Manipulação de dados
zipfile: Descompactação de arquivos

⚠️ Observações

Os arquivos são baixados para a pasta demostrativos_contabeis/
O processamento pode levar alguns minutos dependendo do tamanho dos arquivos
Certifique-se de ter espaço em disco suficiente
É necessária conexão com a internet para o download
