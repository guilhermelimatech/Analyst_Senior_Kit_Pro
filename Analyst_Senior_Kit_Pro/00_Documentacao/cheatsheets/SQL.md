# 📌 Cheat Sheet – SQL Básico para Analistas

Guia rápido dos comandos mais usados em SQL para análise de dados.
(Atualize conforme aprender novos padrões!)

---

## 🔎 Seleção de Dados
- `SELECT * FROM tabela;`
- `SELECT coluna1, coluna2 FROM tabela;`
- `SELECT DISTINCT coluna FROM tabela;`

---

## 🎯 Filtros (WHERE)
- `SELECT * FROM vendas WHERE valor > 1000;`
- `SELECT * FROM clientes WHERE cidade = 'São Paulo';`
- `SELECT * FROM produtos WHERE estoque BETWEEN 10 AND 50;`
- `SELECT * FROM vendas WHERE data >= '2025-01-01';`

---

## 🔢 Ordenação e Limite
- `ORDER BY coluna ASC`
- `ORDER BY coluna DESC`
- `LIMIT 10`

---

## 📊 Agregações
- `COUNT(*)`
- `SUM(valor)`
- `AVG(valor)`
- `MIN(valor)` / `MAX(valor)`

Exemplo:
```sql
SELECT cliente_id, SUM(valor) AS total_gasto
FROM vendas
GROUP BY cliente_id
ORDER BY total_gasto DESC;
🔗 Junções (JOINS)
SELECT c.nome, v.valor
FROM clientes c
INNER JOIN vendas v ON c.id = v.cliente_id;


INNER JOIN

LEFT JOIN

RIGHT JOIN

FULL JOIN

📝 Criação e Alteração

CREATE TABLE tabela (...);

ALTER TABLE tabela ADD coluna tipo;

DROP TABLE tabela;

🛠️ Boas práticas sênior

Usar alias curtos (c, v).

Nomear colunas derivadas (AS total_gasto).

Separar blocos de query em várias linhas.

Testar com LIMIT.
