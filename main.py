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

    def definir_grupo(ano):
        if ano in [2025, 2026]:
            return "Orçamentos 2025-2026"
        return f"Orçamentos {ano}"

    df["Grupo"] = df["Ano"].apply(definir_grupo)

    return df


def gerar_arquivos(df):
    """Gera os arquivos CSV separados por ano."""
    os.makedirs(PASTA_SAIDA, exist_ok=True)

    for grupo, dados in df.groupby("Grupo"):
        
        # Divide 2025 e 2026 em duas partes
        if grupo == "Orçamentos 2025-2026":
            metade = len(dados) // 2

            parte_1 = dados.iloc[:metade]
            parte_2 = dados.iloc[metade:]

            partes = {
                "Orçamentos 2025-2026 Parte 1": parte_1,
                "Orçamentos 2025-2026 Parte 2": parte_2
            }

            for nome, parte in partes.items():
                parte = parte.drop(columns=["Ano", "Grupo"])

                parte.to_csv(
                    f"{PASTA_SAIDA}/{nome}.csv",
                    index=False,
                    sep=";",
                    encoding="latin1"
                )

        else:
            dados = dados.drop(columns=["Ano", "Grupo"])

            dados.to_csv(
                f"{PASTA_SAIDA}/{grupo}.csv",
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