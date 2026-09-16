from pathlib import Path
import pandas as pd


# ============================================================
# CONFIGURAÇÕES
# ============================================================

PASTA_PROJETO = Path(__file__).resolve().parent.parent
ARQUIVO_VENDAS = PASTA_PROJETO / "dados" / "vendas.xlsx"

COLUNAS_OBRIGATORIAS = [
    "Data",
    "Pedido",
    "Produto",
    "Categoria",
    "Região",
    "Vendedor",
    "Quantidade",
    "Preço Unitário",
    "Faturamento",
    "Forma de Pagamento",
    "Status"
]

STATUS_VALIDOS = {
    "Concluído",
    "Cancelado",
    "Pendente"
}

PAGAMENTOS_VALIDOS = {
    "Pix",
    "Cartão de Crédito",
    "Cartão de Débito",
    "Boleto",
    "Transferência"
}


# ============================================================
# FUNÇÕES DE VALIDAÇÃO
# ============================================================

def carregar_dados():
    """Carrega a base de vendas."""

    if not ARQUIVO_VENDAS.exists():
        raise FileNotFoundError(
            f"Arquivo não encontrado:\n{ARQUIVO_VENDAS}"
        )

    return pd.read_excel(ARQUIVO_VENDAS)


def validar_colunas(df):
    """Verifica se todas as colunas obrigatórias existem."""

    colunas_faltantes = [
        coluna
        for coluna in COLUNAS_OBRIGATORIAS
        if coluna not in df.columns
    ]

    return colunas_faltantes


def validar_campos_obrigatorios(df):
    """Verifica campos vazios."""

    campos = [
        "Pedido",
        "Produto",
        "Categoria",
        "Região",
        "Vendedor",
        "Forma de Pagamento",
        "Status"
    ]

    registros_vazios = 0

    for coluna in campos:
        registros_vazios += df[coluna].isna().sum()

    return registros_vazios


def validar_datas(df):
    """Verifica se as datas são válidas."""

    datas = pd.to_datetime(
        df["Data"],
        errors="coerce",
        dayfirst=True
    )

    return datas.isna().sum()


def validar_quantidades(df):
    """Verifica se as quantidades são maiores que zero."""

    quantidade = pd.to_numeric(
        df["Quantidade"],
        errors="coerce"
    )

    return ((quantidade.isna()) | (quantidade <= 0)).sum()


def validar_precos(df):
    """Verifica se os preços unitários são maiores que zero."""

    preco = pd.to_numeric(
        df["Preço Unitário"],
        errors="coerce"
    )

    return ((preco.isna()) | (preco <= 0)).sum()


def validar_faturamento(df):
    """Verifica se faturamento = quantidade x preço unitário."""

    quantidade = pd.to_numeric(
        df["Quantidade"],
        errors="coerce"
    )

    preco = pd.to_numeric(
        df["Preço Unitário"],
        errors="coerce"
    )

    faturamento = pd.to_numeric(
        df["Faturamento"],
        errors="coerce"
    )

    esperado = quantidade * preco

    diferenca = (faturamento - esperado).abs()

    return (
        faturamento.isna() |
        (diferenca > 0.01)
    ).sum()


def validar_pedidos_duplicados(df):
    """Verifica pedidos duplicados."""

    return df["Pedido"].duplicated().sum()


def validar_status(df):
    """Verifica status fora do padrão esperado."""

    valores = (
        df["Status"]
        .dropna()
        .astype(str)
        .str.strip()
    )

    invalidos = ~valores.isin(STATUS_VALIDOS)

    return invalidos.sum(), sorted(valores[invalidos].unique())


def validar_pagamentos(df):
    """Verifica formas de pagamento fora do padrão."""

    valores = (
        df["Forma de Pagamento"]
        .dropna()
        .astype(str)
        .str.strip()
    )

    invalidos = ~valores.isin(PAGAMENTOS_VALIDOS)

    return invalidos.sum(), sorted(valores[invalidos].unique())


# ============================================================
# EXECUÇÃO PRINCIPAL
# ============================================================

def main():

    print("=" * 50)
    print("VALIDAÇÃO DA BASE DE VENDAS")
    print("=" * 50)

    try:
        df = carregar_dados()
    except Exception as erro:
        print(f"\nERRO: {erro}")
        return

    print(f"\nRegistros analisados: {len(df)}\n")

    # --------------------------------------------------------
    # Colunas
    # --------------------------------------------------------

    colunas_faltantes = validar_colunas(df)

    if colunas_faltantes:
        print("✗ Campos obrigatórios..... ERRO")
        print(f"  Colunas ausentes: {colunas_faltantes}")
        return
    else:
        print("✓ Campos obrigatórios..... OK")

    # --------------------------------------------------------
    # Campos vazios
    # --------------------------------------------------------

    vazios = validar_campos_obrigatorios(df)

    if vazios == 0:
        print("✓ Campos preenchidos...... OK")
    else:
        print(f"✗ Campos preenchidos...... {vazios} problema(s)")

    # --------------------------------------------------------
    # Datas
    # --------------------------------------------------------

    datas_invalidas = validar_datas(df)

    if datas_invalidas == 0:
        print("✓ Datas................... OK")
    else:
        print(f"✗ Datas................... {datas_invalidas} inválida(s)")

    # --------------------------------------------------------
    # Quantidades
    # --------------------------------------------------------

    quantidades_invalidas = validar_quantidades(df)

    if quantidades_invalidas == 0:
        print("✓ Quantidades............. OK")
    else:
        print(
            f"✗ Quantidades............. "
            f"{quantidades_invalidas} inválida(s)"
        )

    # --------------------------------------------------------
    # Preços
    # --------------------------------------------------------

    precos_invalidos = validar_precos(df)

    if precos_invalidos == 0:
        print("✓ Preços.................. OK")
    else:
        print(f"✗ Preços.................. {precos_invalidos} inválido(s)")

    # --------------------------------------------------------
    # Faturamento
    # --------------------------------------------------------

    faturamentos_invalidos = validar_faturamento(df)

    if faturamentos_invalidos == 0:
        print("✓ Faturamento............. OK")
    else:
        print(
            f"✗ Faturamento............. "
            f"{faturamentos_invalidos} divergência(s)"
        )

    # --------------------------------------------------------
    # Pedidos duplicados
    # --------------------------------------------------------

    duplicados = validar_pedidos_duplicados(df)

    if duplicados == 0:
        print("✓ Pedidos duplicados...... 0")
    else:
        print(f"✗ Pedidos duplicados...... {duplicados}")

    # --------------------------------------------------------
    # Status
    # --------------------------------------------------------

    status_invalidos, valores_status = validar_status(df)

    if status_invalidos == 0:
        print("✓ Status.................. OK")
    else:
        print(
            f"✗ Status.................. "
            f"{status_invalidos} inválido(s)"
        )
        print(f"  Valores encontrados: {valores_status}")

    # --------------------------------------------------------
    # Formas de pagamento
    # --------------------------------------------------------

    pagamentos_invalidos, valores_pagamento = validar_pagamentos(df)

    if pagamentos_invalidos == 0:
        print("✓ Formas de pagamento.... OK")
    else:
        print(
            f"✗ Formas de pagamento.... "
            f"{pagamentos_invalidos} inválida(s)"
        )
        print(f"  Valores encontrados: {valores_pagamento}")

    # --------------------------------------------------------
    # Resultado final
    # --------------------------------------------------------

    problemas = (
        vazios
        + datas_invalidas
        + quantidades_invalidas
        + precos_invalidos
        + faturamentos_invalidos
        + duplicados
        + status_invalidos
        + pagamentos_invalidos
    )

    print("\n" + "=" * 50)

    if problemas == 0:
        print("BASE VALIDADA COM SUCESSO")
    else:
        print(f"BASE COM {problemas} PROBLEMA(S) ENCONTRADO(S)")

    print("=" * 50)


if __name__ == "__main__":
    main()