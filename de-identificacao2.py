# mascarar texto identificador

# exemplo 1
dados = [
    {"email": "ana@gmail.com"},
    {"email": "carlos@yahoo.com"}
]

for d in dados:
    d["email"] = '@' + d["email"].split("@")[1]

# exemplo 2

dados1 = [
    {"telefone": "31987654321"},
    {"telefone": "11912345678"}
]

n = len(dados1[0]["telefone"])

for d1 in dados1:
    for i in range(n -1, -1, -1):
        if i < n - 2:
            d1["telefone"][i] = '*'

