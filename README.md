# 📊 Automação de Relatório de Vendas — Python + Excel

Projeto de automação desenvolvido em **Python** para validação, análise e geração de relatórios de vendas a partir de uma base de dados em Excel.

O projeto simula um cenário empresarial no qual dados de vendas são processados automaticamente, passando por **validação, análise de indicadores e geração de um relatório gerencial em Excel com Dashboard e gráficos**.

## 🎯 Objetivo

Automatizar o processamento de dados de vendas, reduzindo tarefas manuais e facilitando a análise dos principais indicadores comerciais.

A solução realiza:

* criação de uma base de vendas;
* validação da qualidade dos dados;
* verificação de campos obrigatórios e informações preenchidas;
* validação de datas, quantidades, preços e faturamento;
* identificação de pedidos duplicados;
* processamento e filtragem dos dados;
* análise dos principais indicadores;
* análise por produto, região, vendedor e forma de pagamento;
* evolução mensal das vendas;
* identificação de produtos com baixo volume;
* geração automática de um relatório Excel;
* criação de gráficos;
* criação de um Dashboard gerencial.

## 🛠️ Tecnologias utilizadas

* 🐍 Python
* 🐼 Pandas
* 📗 OpenPyXL
* 📊 Excel
* 📁 Pathlib
* ⚙️ Subprocess

## 📁 Estrutura do projeto

```text
Automacao_Relatorio_Vendas
│
├── dados
│   └── vendas.xlsx
│
├── imagens
│   ├── dashboard_vendas.png
│   └── relatorio_vendas.png
│
├── relatorios
│   └── relatorio_vendas.xlsx
│
├── src
│   ├── criar_base.py
│   ├── validar_dados.py
│   ├── analisar_vendas.py
│   ├── gerar_relatorio.py
│   └── gerar_excel.py
│
├── .gitignore
└── README.md
```

## ⚙️ Funcionamento

O processo foi estruturado em etapas para automatizar todo o fluxo de análise.

### 1. Criação da base

O arquivo `criar_base.py` gera uma base de vendas simulada contendo informações como:

* data da venda;
* pedido;
* produto;
* categoria;
* região;
* vendedor;
* quantidade;
* preço unitário;
* faturamento;
* forma de pagamento;
* status do pedido.

A base é salva automaticamente em:

```text
dados/vendas.xlsx
```

### 2. Validação dos dados

O arquivo `validar_dados.py` realiza verificações automáticas na base antes da análise.

São validados:

* campos obrigatórios;
* campos preenchidos;
* datas;
* quantidades;
* preços;
* cálculo do faturamento;
* pedidos duplicados;
* status dos pedidos;
* formas de pagamento.

Dessa forma, o processo verifica a consistência da base antes de gerar os indicadores e o relatório.

### 3. Análise das vendas

O arquivo `analisar_vendas.py` realiza a análise dos dados e calcula indicadores como:

* faturamento total;
* quantidade vendida;
* total de pedidos;
* pedidos concluídos;
* pedidos cancelados;
* ticket médio;
* faturamento por produto;
* faturamento por região;
* faturamento por vendedor;
* evolução mensal das vendas;
* produtos com baixo volume.

Para os indicadores de vendas realizadas, são considerados apenas os pedidos com status **Concluído**.

### 4. Geração do relatório

O arquivo `gerar_excel.py` cria automaticamente o relatório final em Excel.

O relatório contém as seguintes abas:

* Dashboard
* Resumo
* Por Produto
* Por Região
* Por Vendedor
* Por Pagamento

Além das tabelas analíticas, o relatório possui gráficos para facilitar a visualização dos resultados.

### 5. Automação do processo

O arquivo `gerar_relatorio.py` funciona como o **orquestrador do projeto**.

Ao executar esse arquivo, o sistema realiza automaticamente:

```text
Validação dos dados
        ↓
Análise das vendas
        ↓
Geração do relatório Excel
        ↓
Atualização do Dashboard
```

Assim, não é necessário executar cada etapa manualmente.

## 📈 Indicadores gerados

O Dashboard apresenta os principais KPIs do período analisado:

* **Faturamento Total:** R$ 276.520,00
* **Quantidade Vendida:** 309
* **Pedidos Concluídos:** 113
* **Pedidos Cancelados:** 37
* **Ticket Médio:** R$ 2.447,08

Além dos indicadores principais, o sistema permite analisar:

* produtos com maior faturamento;
* faturamento por região;
* faturamento por vendedor;
* formas de pagamento;
* evolução mensal das vendas.

## 📊 Resultado

A automação transforma uma base de vendas em um **relatório gerencial estruturado**, permitindo visualizar rapidamente os principais indicadores e análises comerciais.

O projeto demonstra conhecimentos práticos em:

* manipulação e tratamento de dados;
* validação de informações;
* análise de dados;
* automação de processos;
* geração de relatórios;
* indicadores de desempenho;
* Python;
* Pandas;
* OpenPyXL;
* Excel.

## ▶️ Como executar

Com Python instalado, abra o terminal na **pasta principal do projeto**:

```text
Automacao_Relatorio_Vendas
```

Instale as dependências:

```bash
pip install pandas openpyxl
```

Depois execute:

```bash
python src/gerar_relatorio.py
```

O sistema executará automaticamente todas as etapas:

```text
1. Validação dos dados
2. Análise das vendas
3. Geração do relatório Excel
4. Atualização do Dashboard
```

O relatório final será criado automaticamente em:

```text
relatorios/relatorio_vendas.xlsx
```

## 🖼️ Visualização do Projeto

### 📊 Dashboard de Vendas

![Dashboard de Vendas](imagens/dashboard_vendas.png)

### 📋 Relatório de Vendas

![Relatório de Vendas](imagens/relatorio_vendas.png)

## 💼 Aplicação profissional

O projeto simula uma rotina de **análise e automação de processos comerciais**, demonstrando conhecimentos aplicáveis a atividades de:

* Análise de Dados;
* Automação de Processos;
* Análise de Sistemas;
* Tratamento e validação de informações;
* Geração de relatórios;
* Indicadores de desempenho;
* Apoio à tomada de decisão.

## 👨‍💻 Projeto desenvolvido para portfólio

Este projeto faz parte do portfólio de transição profissional para a área de **Tecnologia da Informação**, com foco em **Análise de Sistemas, Análise de Dados, Automação e Processos**.

**Fernando Bueno**

🎓 Engenheiro de Computação
💻 Em transição para a área de Tecnologia da Informação
