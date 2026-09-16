from pathlib import Path
import pandas as pd


# ============================================================
# CONFIGURAÇÕES
# ============================================================

PASTA_PROJETO = Path(__file__).resolve().parent.parent
ARQUIVO_VENDAS = PASTA_PROJETO / "dados" / "vendas.xlsx"


# ============================================================
# CARREGAMENTO E PREPARAÇÃO
# ============================================================

def carregar_dados():
    """Carrega e prepara a base de vendas."""

    df = pd.read_excel(ARQUIVO_VENDAS)

    df["Data"] = pd.to_datetime(
        df["Data"],
        errors="coerce",
        dayfirst=True
    )

    df["Quantidade"] = pd.to_numeric(
        df["Quantidade"],
        errors="coerce"
    )

    df["Preço Unitário"] = pd.to_numeric(
        df["Preço Unitário"],
        errors="coerce"
    )

    df["Faturamento"] = pd.to_numeric(
        df["Faturamento"],
        errors="coerce"
    )

    return df


# ============================================================
# INDICADORES GERAIS
# ============================================================

def calcular_indicadores(df):
    """Calcula os principais indicadores da operação."""

    # Considera apenas pedidos concluídos como vendas realizadas
    df_concluido = df[df["Status"] == "Concluído"].copy()

    faturamento_total = df_concluido["Faturamento"].sum()

    quantidade_vendida = df_concluido["Quantidade"].sum()

    total_pedidos = df_concluido["Pedido"].nunique()

    pedidos_concluidos = df_concluido["Pedido"].nunique()

    pedidos_cancelados = (
        df[df["Status"] == "Cancelado"]["Pedido"]
        .nunique()
    )

    ticket_medio = (
        faturamento_total / total_pedidos
        if total_pedidos > 0
        else 0
    )

    return {
        "Faturamento Total": faturamento_total,
        "Quantidade Vendida": quantidade_vendida,
        "Total de Pedidos": total_pedidos,
        "Pedidos Concluídos": pedidos_concluidos,
        "Pedidos Cancelados": pedidos_cancelados,
        "Ticket Médio": ticket_medio
    }

# ============================================================
# ANÁLISES POR PRODUTO
# ============================================================

def analisar_produtos(df):

    analise = (
        df.groupby("Produto")
        .agg(
            Faturamento=("Faturamento", "sum"),
            Quantidade=("Quantidade", "sum"),
            Pedidos=("Pedido", "nunique")
        )
        .sort_values(
            "Faturamento",
            ascending=False
        )
        .reset_index()
    )

    return analise


# ============================================================
# ANÁLISES POR REGIÃO
# ============================================================

def analisar_regioes(df):

    analise = (
        df.groupby("Região")
        .agg(
            Faturamento=("Faturamento", "sum"),
            Quantidade=("Quantidade", "sum"),
            Pedidos=("Pedido", "nunique")
        )
        .sort_values(
            "Faturamento",
            ascending=False
        )
        .reset_index()
    )

    return analise


# ============================================================
# ANÁLISES POR VENDEDOR
# ============================================================

def analisar_vendedores(df):

    analise = (
        df.groupby("Vendedor")
        .agg(
            Faturamento=("Faturamento", "sum"),
            Quantidade=("Quantidade", "sum"),
            Pedidos=("Pedido", "nunique")
        )
        .sort_values(
            "Faturamento",
            ascending=False
        )
        .reset_index()
    )

    return analise


# ============================================================
# EVOLUÇÃO MENSAL
# ============================================================

def analisar_evolucao_mensal(df):

    df = df.copy()

    df["Mês"] = df["Data"].dt.to_period("M")

    analise = (
        df.groupby("Mês")
        .agg(
            Faturamento=("Faturamento", "sum"),
            Quantidade=("Quantidade", "sum"),
            Pedidos=("Pedido", "nunique")
        )
        .reset_index()
    )

    analise["Mês"] = analise["Mês"].astype(str)

    return analise


# ============================================================
# PRODUTOS COM BAIXO VOLUME
# ============================================================

def identificar_baixo_volume(df, limite=10):

    analise = (
        df.groupby("Produto")
        .agg(
            Quantidade=("Quantidade", "sum"),
            Faturamento=("Faturamento", "sum")
        )
        .reset_index()
    )

    baixo_volume = analise[
        analise["Quantidade"] < limite
    ].sort_values(
        "Quantidade"
    )

    return baixo_volume


# ============================================================
# EXECUÇÃO
# ============================================================

def main():

    print("=" * 55)
    print("ANÁLISE DA BASE DE VENDAS")
    print("=" * 55)

    df = carregar_dados()

    indicadores = calcular_indicadores(df)
    produtos = analisar_produtos(df)
    regioes = analisar_regioes(df)
    vendedores = analisar_vendedores(df)
    evolucao = analisar_evolucao_mensal(df)
    baixo_volume = identificar_baixo_volume(df)

    print("\nINDICADORES GERAIS")
    print("-" * 55)

    print(
        f"Faturamento total: "
        f"R$ {indicadores['Faturamento Total']:,.2f}"
    )

    print(
        f"Quantidade vendida: "
        f"{indicadores['Quantidade Vendida']}"
    )

    print(
        f"Total de pedidos: "
        f"{indicadores['Total de Pedidos']}"
    )

    print(
        f"Pedidos concluídos: "
        f"{indicadores['Pedidos Concluídos']}"
    )

    print(
        f"Pedidos cancelados: "
        f"{indicadores['Pedidos Cancelados']}"
    )

    print(
        f"Ticket médio: "
        f"R$ {indicadores['Ticket Médio']:,.2f}"
    )

    print("\nTOP 5 PRODUTOS POR FATURAMENTO")
    print("-" * 55)
    print(
        produtos[
            ["Produto", "Faturamento"]
        ].head(5).to_string(index=False)
    )

    print("\nFATURAMENTO POR REGIÃO")
    print("-" * 55)
    print(
        regioes[
            ["Região", "Faturamento"]
        ].to_string(index=False)
    )

    print("\nFATURAMENTO POR VENDEDOR")
    print("-" * 55)
    print(
        vendedores[
            ["Vendedor", "Faturamento"]
        ].to_string(index=False)
    )

    print("\nEVOLUÇÃO MENSAL")
    print("-" * 55)
    print(evolucao.to_string(index=False))

    print("\nPRODUTOS COM BAIXO VOLUME")
    print("-" * 55)

    if baixo_volume.empty:
        print("Nenhum produto identificado.")
    else:
        print(
            baixo_volume.to_string(index=False)
        )

    print("\n" + "=" * 55)
    print("ANÁLISE CONCLUÍDA")
    print("=" * 55)


if __name__ == "__main__":
    main()