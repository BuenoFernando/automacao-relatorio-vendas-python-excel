# Automação de Relatório de Vendas — Python + Excel

Projeto de automação desenvolvido em Python para geração de relatórios de vendas a partir de uma base de dados em Excel.

O projeto simula um cenário empresarial no qual dados de vendas são processados automaticamente para gerar indicadores, análises e um relatório gerencial em Excel.

## Objetivo

Automatizar o processamento de dados de vendas, reduzindo tarefas manuais e facilitando a análise dos principais indicadores comerciais.

A solução realiza:

* criação de uma base de vendas;
* processamento e filtragem dos dados;
* cálculo de indicadores;
* análise por produto, região, vendedor e forma de pagamento;
* geração automática de um relatório Excel;
* criação de gráficos;
* criação de um Dashboard gerencial.

## Tecnologias utilizadas

* Python
* Pandas
* OpenPyXL
* Excel

## Estrutura do projeto

```text
Automacao_Relatorio_Vendas
│
├── dados
│   └── vendas.xlsx
│
├── relatorios
│   └── relatorio_vendas.xlsx
│
├── src
│   ├── criar_base.py
│   ├── gerar_relatorio.py
│   └── gerar_excel.py
│
└── README.md
```

## Funcionamento

O processo foi dividido em três etapas principais.

### 1. Criação da base

O arquivo `criar_base.py` gera uma base de vendas simulada contendo informações como:

* data da venda;
* produto;
* categoria;
* região;
* vendedor;
* quantidade;
* valor;
* forma de pagamento;
* status do pedido.

A base é salva automaticamente em:

```text
dados/vendas.xlsx
```

### 2. Processamento dos dados

O arquivo `gerar_relatorio.py` utiliza Pandas para processar os dados e calcular indicadores como:

* faturamento total;
* quantidade vendida;
* pedidos concluídos;
* ticket médio;
* produto mais vendido;
* região com maior faturamento;
* vendedor destaque.

### 3. Geração do relatório

O arquivo `gerar_excel.py` cria automaticamente o relatório final em Excel.

O arquivo gerado contém as seguintes abas:

* Dashboard
* Resumo
* Por Produto
* Por Região
* Por Vendedor
* Por Pagamento

Além das tabelas analíticas, o relatório possui gráficos para facilitar a visualização dos resultados.

## Indicadores gerados

O Dashboard apresenta os principais KPIs do período analisado:

* **Faturamento Total:** R$ 276.520,00
* **Quantidade Vendida:** 309
* **Pedidos Concluídos:** 113
* **Ticket Médio:** R$ 2.447,08

## Resultado

A automação transforma uma base de vendas em um relatório gerencial estruturado, permitindo visualizar rapidamente os principais indicadores e análises comerciais.

O projeto demonstra conhecimentos práticos em:

* manipulação e tratamento de dados;
* análise de informações;
* automação de tarefas;
* geração de relatórios;
* Python;
* Pandas;
* Excel;
* OpenPyXL.

## Como executar

Com Python instalado, abra o terminal dentro da pasta:

```text
src
```

Execute os scripts na seguinte ordem:

```bash
python criar_base.py
```

Depois:

```bash
python gerar_relatorio.py
```

E por último:

```bash
python gerar_excel.py
```

O relatório final será criado automaticamente na pasta:

```text
relatorios
```

com o nome:

```text
relatorio_vendas.xlsx
```

## Projeto desenvolvido para portfólio

Este projeto faz parte do portfólio de transição profissional para a área de Tecnologia da Informação, com foco em **Análise de Sistemas, Análise de Dados, Automação e Processos**.
