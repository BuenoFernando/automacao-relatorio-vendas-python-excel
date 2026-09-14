
import pandas as pd
import random
from datetime import datetime, timedelta

produtos = [
    ("Notebook", "Informática", 3500),
    ("Monitor", "Informática", 1200),
    ("Teclado", "Periféricos", 150),
    ("Mouse", "Periféricos", 80),
    ("Headset", "Periféricos", 220),
    ("Impressora", "Informática", 900),
    ("Webcam", "Periféricos", 180),
    ("SSD 480GB", "Informática", 350)
]

regioes = [
    "Sudeste",
    "Sul",
    "Centro-Oeste",
    "Nordeste",
    "Norte"
]

vendedores = [
    "Ana",
    "Carlos",
    "Fernanda",
    "João",
    "Marcos"
]

pagamentos = [
    "Pix",
    "Cartão de Crédito",
    "Cartão de Débito",
    "Boleto"
]

status = [
    "Concluído",
    "Concluído",
    "Concluído",
    "Cancelado"
]

data_inicial = datetime(2026, 1, 1)

dados = []

for i in range(1, 151):

    produto, categoria, preco = random.choice(produtos)

    quantidade = random.randint(1, 5)

    data_venda = data_inicial + timedelta(
        days=random.randint(0, 242)
    )

    dados.append({
        "Data": data_venda,
        "Pedido": f"PED{i:05d}",
        "Produto": produto,
        "Categoria": categoria,
        "Região": random.choice(regioes),
        "Vendedor": random.choice(vendedores),
        "Quantidade": quantidade,
        "Preço Unitário": preco,
        "Faturamento": quantidade * preco,
        "Forma de Pagamento": random.choice(pagamentos),
        "Status": random.choice(status)
    })

df = pd.DataFrame(dados)

df = df.sort_values("Data")

df["Data"] = df["Data"].dt.strftime("%d/%m/%Y")

caminho = "../dados/vendas.xlsx"

df.to_excel(caminho, index=False)

print("Base de vendas criada com sucesso!")
print(f"Quantidade de registros: {len(df)}")
print(f"Arquivo criado em: {caminho}")
