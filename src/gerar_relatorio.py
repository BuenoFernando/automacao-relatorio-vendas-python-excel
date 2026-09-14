import pandas as pd

# Caminho da base
caminho = "../dados/vendas.xlsx"

# Ler a base
df = pd.read_excel(caminho)

# Considerar apenas vendas concluídas
df_concluido = df[df["Status"] == "Concluído"].copy()

# Indicadores
faturamento_total = df_concluido["Faturamento"].sum()
quantidade_vendida = df_concluido["Quantidade"].sum()
total_pedidos = len(df_concluido)

ticket_medio = faturamento_total / total_pedidos

# Produto mais vendido
produto_mais_vendido = (
    df_concluido.groupby("Produto")["Quantidade"]
    .sum()
    .sort_values(ascending=False)
    .index[0]
)

# Região com maior faturamento
regiao_maior_faturamento = (
    df_concluido.groupby("Região")["Faturamento"]
    .sum()
    .sort_values(ascending=False)
    .index[0]
)

# Vendedor com maior faturamento
vendedor_destaque = (
    df_concluido.groupby("Vendedor")["Faturamento"]
    .sum()
    .sort_values(ascending=False)
    .index[0]
)

# Exibir resultados
print("\n===== RELATÓRIO DE VENDAS =====")

print(f"Faturamento total: R$ {faturamento_total:,.2f}")
print(f"Quantidade vendida: {quantidade_vendida}")
print(f"Pedidos concluídos: {total_pedidos}")
print(f"Ticket médio: R$ {ticket_medio:,.2f}")
print(f"Produto mais vendido: {produto_mais_vendido}")
print(f"Região com maior faturamento: {regiao_maior_faturamento}")
print(f"Vendedor destaque: {vendedor_destaque}")

print("\nRelatório calculado com sucesso!")