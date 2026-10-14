from pathlib import Path
import pandas as pd

ARQUIVO_ENTRADA = Path("dados/newsletter/Newsletter.csv")
PASTA_SAIDA = Path("output/newsletter")


def separar_newsletter():
    # Carrega os cadastros
    df = pd.read_csv(
        ARQUIVO_ENTRADA,
        sep=None,
        engine="python",
        encoding="latin1"
    )

    # Converte os diferentes formatos de data
    datas = pd.to_datetime(
        df["Data de Cad."],
        format="mixed",
        dayfirst=True,
        errors="coerce"
    )

    # Impede a exportação se houver datas inválidas
    if datas.isna().any():
        raise ValueError("Existem datas inválidas no arquivo.")

    # Identifica o ano de cada cadastro
    anos = datas.dt.year

    # Agrupa 2012, 2013 e 2014
    grupos = anos.apply(
        lambda ano: "2012-2014" if ano in [2012, 2013, 2014] else str(ano)
    )

    PASTA_SAIDA.mkdir(parents=True, exist_ok=True)

    # Gera os arquivos CSV
    for grupo, indices in grupos.groupby(grupos).groups.items():
        dados = df.loc[indices]

        caminho = PASTA_SAIDA / f"Newsletter {grupo}.csv"

        dados.to_csv(
            caminho,
            index=False,
            sep=";",
            encoding="latin1"
        )

        print(f"{caminho.name}: {len(dados)} registros")

    print("\nSeparação concluída!")

        # Valida a quantidade total de registros exportados
    total_exportado = 0

    for caminho in PASTA_SAIDA.glob("*.csv"):
        arquivo_validacao = pd.read_csv(
            caminho,
            sep=";",
            encoding="latin1"
        )

        total_exportado += len(arquivo_validacao)

    print(f"\nTotal original: {len(df)}")
    print(f"Total exportado: {total_exportado}")

    if total_exportado == len(df):
        print("VALIDAÇÃO OK: todos os registros foram preservados.")
    else:
        print("ERRO: diferença na quantidade de registros!")


if __name__ == "__main__":
    separar_newsletter()

    print("\nVALIDAÇÃO DOS ANOS:")

    for caminho in sorted(PASTA_SAIDA.glob("*.csv")):
        dados = pd.read_csv(
            caminho,
            sep=";",
            encoding="latin1"
        )

        datas = pd.to_datetime(
            dados["Data de Cad."],
            format="mixed",
            dayfirst=True,
            errors="coerce"
        )

        anos = set(datas.dt.year.dropna().astype(int))

        if caminho.stem == "Newsletter 2012-2014":
            anos_esperados = {2012, 2013, 2014}
        else:
            ano = int(caminho.stem.split()[-1])
            anos_esperados = {ano}

        if datas.isna().any() or anos != anos_esperados:
            print(f"ERRO: {caminho.name} - anos encontrados: {sorted(anos)}")
        else:
            print(f"OK: {caminho.name}")

   