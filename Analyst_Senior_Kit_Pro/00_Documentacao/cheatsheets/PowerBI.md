## 📌 3. `PowerBI.md`
```markdown
# 📌 Cheat Sheet – Power BI para Análise de Dados

Guia rápido com atalhos, boas práticas e comandos essenciais.

---

## 🚀 Importação de Dados
- Excel, CSV, SQL, Web, API.
- Power Query:
  - Remover colunas.
  - Alterar tipo.
  - Mesclar (JOIN).
  - Acrescentar (UNION).

---

## 🔎 Modelagem
- Relacionamentos (1:N).
- Dimensões: Clientes, Produtos, Tempo.
- Fatos: Vendas.
- Criar tabela calendário.

---

## 📊 Medidas (DAX)
```DAX
Total Vendas = SUM(FatoVendas[Valor])
Qtd Vendas = COUNTROWS(FatoVendas)
Ticket Médio = DIVIDE([Total Vendas], [Qtd Vendas])
Vendas Ano = CALCULATE([Total Vendas], YEAR(DimDate[Data]) = 2025)
Funções: SUM, AVERAGE, COUNTROWS, CALCULATE, FILTER, ALL, RELATED

📈 Visualizações
Colunas/Barras

Linha

Mapa

Cartão

Slicer

Boas práticas:

Máx. 5–6 visuais por página.

Cores consistentes.

1 KPI principal no topo.

🎨 Layout
Página 16:9.

Títulos claros.

Ícones e cores da empresa.

Filtros agrupados.

🛠️ Publicação
Power BI Service.

Atualização automática (gateway).

Workspaces.

🧠 Boas práticas sênior
Sempre tabela calendário.

Medidas DAX (não colunas calculadas).

Documentar.

Versionar PBIX junto com SQL/Python.
