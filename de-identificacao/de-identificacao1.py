
# Tirar os PII a seguir
dados = [
    {"nome": "Ana", "cpf": "123.456.789-00", "idade": 28},
    {"nome": "Carlos", "cpf": "987.654.321-00", "idade": 35}
]
pii = []

for d in dados:
    pii.append({"nome": d["nome"]})
    pii.append({"cpf": d["cpf"]})

    d.pop("nome")
    d.pop("cpf")
