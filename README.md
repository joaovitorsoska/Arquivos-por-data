# Separação de Orçamentos por Ano

Script em Python desenvolvido para separar um arquivo de orçamentos em diferentes arquivos CSV, de acordo com o ano da data de cadastro.

## Funcionamento

O programa:

1. Lê o arquivo CSV de entrada.
2. Converte a coluna `Data de Cad.` para o formato de data.
3. Identifica o ano de cada cadastro.
4. Separa os registros por ano.
5. Agrupa os registros anteriores a 2020 em um único arquivo.
6. Gera os arquivos separados na pasta `output`.

## Arquivos gerados

O programa gera os seguintes arquivos:

- `Orçamentos 2026.csv`
- `Orçamentos 2025.csv`
- `Orçamentos 2024.csv`
- `Orçamentos 2023.csv`
- `Orçamentos 2022.csv`
- `Orçamentos 2021.csv`
- `Orçamentos 2020.csv`
- `Orçamentos abaixo 2020.csv`

## Tecnologias

- Python
- Pandas

## Como executar

Instale as dependências:

```bash
python -m pip install -r requirements.txt