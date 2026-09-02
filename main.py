import os
import pandas as pd


ARQUIVO_ENTRADA = "dados/85120351788264902.csv"
PASTA_SAIDA = "output"


def carregar_dados():
    """Carrega o arquivo CSV e converte a coluna de data."""
    df = pd.read_csv(
        ARQUIVO_ENTRADA,
        encoding="latin1",
        sep=";"
    )

    df["Data de Cad."] = pd.to_datetime(
        df["Data de Cad."],
        errors="coerce"
    )

    return df


def classificar_orcamentos(df):
    """Classifica os registros de acordo com o ano."""
    df["Ano"] = df["Data de Cad."].dt.year

    df["Grupo"] = df["Ano"].apply(
        lambda ano: (
            f"Orçamentos {ano}"
            if ano >= 2020
            else "Orçamentos abaixo 2020"
        )
    )

    return df


def gerar_arquivos(df):
    """Gera um CSV para cada grupo de orçamento."""
    os.makedirs(PASTA_SAIDA, exist_ok=True)

    for grupo, dados in df.groupby("Grupo"):
        nome_arquivo = f"{PASTA_SAIDA}/{grupo}.csv"

        dados = dados.drop(columns=["Ano", "Grupo"])

        dados.to_csv(
            nome_arquivo,
            index=False,
            sep=";",
            encoding="latin1"
        )


def main():
    df = carregar_dados()
    df = classificar_orcamentos(df)
    gerar_arquivos(df)

    print("Arquivos gerados com sucesso!")


if __name__ == "__main__":
    main()