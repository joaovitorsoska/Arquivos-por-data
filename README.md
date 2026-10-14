# Separação de Arquivos CSV por Ano

Script desenvolvido em Python para automatizar a organização de registros em arquivos CSV, utilizando a data de cadastro como critério de separação.

## Funcionalidades

O projeto possui duas rotinas de processamento:

**1. Separação de Orçamentos (`main.py`)**
- Organiza os registros de orçamentos por ano.
- Permite agrupar períodos específicos e dividir arquivos em partes.
- Exporta os resultados em arquivos CSV.

**2. Separação de Newsletter (`separar_newsletter.py`)**
- Organiza os cadastros de newsletter por ano.
- Agrupa os registros de 2012, 2013 e 2014 em um único arquivo.
- Gera arquivos individuais para os anos de 2015 em diante.
- Suporta diferentes formatos de data.
- Verifica a quantidade de registros exportados.

## Tecnologias

- Python
- Pandas

## Estrutura do projeto

```text
arquivos-por-data/
├── dados/
│   └── newsletter/
├── output/
│   └── newsletter/
├── main.py
├── separar_newsletter.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Como executar

Instale as dependências:

```bash
python -m pip install -r requirements.txt
```

Para processar os orçamentos:

```bash
python main.py
```

Para processar os cadastros de newsletter:

```bash
python separar_newsletter.py
```

Os arquivos de entrada devem estar nos caminhos definidos nos respectivos scripts.

## Privacidade dos dados

Os arquivos CSV utilizados e gerados durante o processamento não são disponibilizados neste repositório. O `.gitignore` impede que esses dados sejam incluídos no versionamento.