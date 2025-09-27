
---

## 📌 2. `Python.md`
```markdown
# 📌 Cheat Sheet – Python para Análise de Dados

Guia rápido de Python focado em Pandas, Numpy, Matplotlib.

---

## 🚀 Básico
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
📂 Ler Dados
df = pd.read_csv("dados.csv")
df = pd.read_excel("dados.xlsx")
df.head()
df.info()
df.describe()

🔎 Seleção e Filtro
df["coluna"]
df[["col1","col2"]]
df[df["coluna"] > 1000]
df.loc[0]
df.iloc[0:5]

🛠️ Transformações
df["nova_coluna"] = df["col1"] + df["col2"]
df = df.rename(columns={"antigo":"novo"})
df = df.drop(columns=["coluna"])
df["coluna"].fillna(0, inplace=True)
df["coluna"].astype(int)

📊 Agregações
df.groupby("cliente")["valor"].sum()
df.groupby("categoria").agg({
    "valor":["mean","max","min"]
})

📈 Visualização
df["valor"].plot(kind="hist")
df["categoria"].value_counts().plot(kind="bar")
plt.show()

🔗 Integração com SQL
import sqlite3
conn = sqlite3.connect("banco.db")
df = pd.read_sql("SELECT * FROM vendas", conn)

🛠️ Boas práticas sênior

Nomes claros (df_vendas).

Usar notebooks (Jupyter/VS Code).

Requirements.txt para pacotes.

Documentar cada célula com comentários.
