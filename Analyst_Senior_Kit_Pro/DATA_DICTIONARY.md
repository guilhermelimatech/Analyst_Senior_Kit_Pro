# Dicionário de Dados

| Coluna        | Tipo     | Descrição                              | Regras/Observações             |
|---------------|----------|----------------------------------------|--------------------------------|
| order_id      | Integer  | Identificador único do pedido          | Não pode ser nulo/duplicado    |
| order_date    | Date     | Data do pedido (YYYY-MM-DD)            | Data válida                    |
| customer_id   | Integer  | Identificador do cliente               | Chave estrangeira              |
| freight_cost  | Float    | Custo de frete em R$                   | >= 0                           |
| region        | String   | Região do cliente                      | Valores padronizados/lookup    |
