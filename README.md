# 📊 Sistema de Análise e Automação de Vendas

Sistema desenvolvido em **Python** para validação, análise e automação de relatórios de vendas, utilizando **Pandas, OpenPyXL e Excel**.

O projeto automatiza o processamento de uma base de vendas, valida a qualidade dos dados, calcula indicadores e gera um relatório Excel com **dashboard e gráficos para análise gerencial**.

---

## 🎯 Objetivo

Demonstrar a aplicação de **Python na automação de processos, tratamento de dados e geração de relatórios**, reduzindo tarefas manuais e facilitando a análise de informações comerciais.

---

## 🛠️ Tecnologias

* 🐍 **Python**
* 🐼 **Pandas**
* 📗 **OpenPyXL**
* 📊 **Excel**
* 📁 **Pathlib**
* ⚙️ **Subprocess**

---

## ⚙️ Funcionalidades

* ✅ Validação automática da base de vendas
* ✅ Verificação de campos obrigatórios e dados preenchidos
* ✅ Validação de datas, quantidades e preços
* ✅ Validação do cálculo de faturamento
* ✅ Identificação de pedidos duplicados
* ✅ Validação de status e formas de pagamento
* ✅ Cálculo de indicadores de vendas
* ✅ Análise por produto, região e vendedor
* ✅ Evolução mensal das vendas
* ✅ Geração automática de relatório Excel
* ✅ Criação de dashboard com indicadores e gráficos

---

## 📈 Indicadores

O sistema calcula automaticamente:

* 💰 Faturamento realizado
* 📦 Quantidade vendida
* 🧾 Total de pedidos concluídos
* ❌ Pedidos cancelados
* 🎯 Ticket médio
* 🏆 Produtos com maior faturamento
* 🌎 Faturamento por região
* 👤 Faturamento por vendedor
* 📅 Evolução mensal das vendas

> Para os indicadores de vendas realizadas, são considerados apenas os pedidos com status **Concluído**.

---

## 📊 Resultado

A execução do sistema gera automaticamente um arquivo Excel contendo:

* **Dashboard**
* **Resumo**
* **Análise por Produto**
* **Análise por Região**
* **Análise por Vendedor**
* **Análise por Forma de Pagamento**
* **Gráficos para apoio à análise**

---

## 📁 Estrutura do Projeto

```text
Automacao_Relatorio_Vendas/
│
├── dados/
│   └── vendas.xlsx
│
├── relatorios/
│   └── relatorio_vendas.xlsx
│
├── src/
│   ├── criar_base.py
│   ├── validar_dados.py
│   ├── analisar_vendas.py
│   ├── gerar_relatorio.py
│   └── gerar_excel.py
│
├── .gitignore
└── README.md
```

---

## ▶️ Como Executar

### 1. Instalar as dependências

```bash
pip install pandas openpyxl
```

### 2. Executar o sistema

Na pasta principal do projeto:

```bash
python src/gerar_relatorio.py
```

O sistema executará automaticamente as etapas de:

```text
Validação dos dados
        ↓
Análise das vendas
        ↓
Geração do relatório Excel
        ↓
Atualização do Dashboard
```

O relatório final será salvo em:

```text
relatorios/relatorio_vendas.xlsx
```

---

## 💼 Aplicação Profissional

O projeto simula uma rotina de **análise e automação de processos comerciais**, demonstrando conhecimentos aplicáveis a atividades de:

* Análise de dados
* Automação de processos
* Tratamento e validação de informações
* Geração de relatórios
* Indicadores de desempenho
* Apoio à tomada de decisão

---

## 👨‍💻 Autor

**Fernando Bueno**

🎓 Engenheiro de Computação
💻 Em transição para a área de Tecnologia da Informação
