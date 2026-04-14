import pandas as pd

dados = [
    [1, 25, "M", "BH", 3000, 720, 5, 2.5, "Sim", 1],
    [2, 34, "F", "SP", 7000, 800, 10, 1.8, "Sim", 0],
    [3, 29, "M", "RJ", 4500, 650, 3, 3.2, "Não", 1],
    [4, 41, "F", "BH", 9000, 820, 15, 2.0, "Sim", 0],
    [5, 22, "M", "POA", 2000, 600, 1, 4.0, "Não", 1]
]

colunas = [
    "id",
    "idade",
    "genero",
    "cidade",
    "renda",
    "score_credito",
    "tempo_emprego",
    "gasto_mensal",
    "possui_cartao",
    "label"
]

df = pd.DataFrame(dados, columns=colunas)

print(dados)
