# ANS Data Extractor

> Extração automatizada de demonstrativos contábeis da ANS (Agência Nacional de Saúde Suplementar)

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## 📋 Sobre o Projeto

Este projeto automatiza o processo de extração, transformação e consolidação de dados contábeis da ANS, focando em informações sobre Eventos e Sinistros.

### Funcionalidades

- ✅ Download automático de demonstrativos contábeis
- ✅ Extração de arquivos ZIP
- ✅ Detecção inteligente de separadores CSV
- ✅ Filtragem de dados específicos (Eventos/Sinistros)
- ✅ Consolidação de múltiplos trimestres

## 🚀 Início Rápido

### Pré-requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

### Instalação

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd ans-data-extractor
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

### Uso

Execute o script principal:

```bash
python main.py
```

O script irá:
1. Buscar os últimos 3 trimestres disponíveis
2. Baixar os arquivos ZIP
3. Extrair automaticamente
4. Filtrar dados de "Eventos / Sinistros"
5. Gerar `data_concat.csv` consolidado

### Configuração

Altere a quantidade de trimestres em `main.py`:

```python
trimestres = ans_extract.obter_trimestres(3)  # Altere o número
```

## 📁 Estrutura do Projeto

```
ans-data-extractor/
│
├── ans_extract.py           # Extração e download
├── ans_transform.py         # Transformação e filtragem
├── main.py                  # Script principal
├── requirements.txt         # Dependências
├── README.md               # Documentação
└── demostrativos_contabeis/ # Dados (gerado automaticamente)
```

## 🔧 Módulos

### `ANSExtract`
- Navegação na estrutura de diretórios da ANS
- Download de arquivos ZIP
- Extração de arquivos compactados

### `ANSTransform`
- Detecção de tipos de arquivo (CSV, TXT, XLSX)
- Identificação automática de separadores
- Filtragem e concatenação de dados

## 🛠️ Tecnologias

- [Python](https://www.python.org/) - Linguagem de programação
- [Requests](https://requests.readthedocs.io/) - HTTP requests
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/) - Web scraping
- [Pandas](https://pandas.pydata.org/) - Análise de dados
- [OpenPyXL](https://openpyxl.readthedocs.io/) - Manipulação de Excel

## 📊 Saída

O arquivo `data_concat.csv` contém todos os dados filtrados de "Eventos / Sinistros" consolidados.

## ⚠️ Observações

- Requer conexão com internet
- Necessário espaço em disco adequado
- Processamento pode levar alguns minutos

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 🤝 Contribuindo

Contribuições são bem-vindas!

1. Fork o projeto
2. Crie sua feature branch (`git checkout -b feature/NovaFuncionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/NovaFuncionalidade`)
5. Abra um Pull Request

## 📧 Contato

Para dúvidas ou sugestões, abra uma [issue](../../issues).

---

⭐ Se este projeto foi útil, considere dar uma estrela!
