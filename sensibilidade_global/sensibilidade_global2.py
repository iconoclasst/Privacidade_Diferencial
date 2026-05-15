import pandas as pd

# f1 = media
# f2 = somatorio

funcoes = ['f1', 'f2']

def sg(f, D, u):
    n = len(D)

    if f == 'f1':
        delta = max(u) - min(u)
        return delta//n
    if f == 'f2':
        delta = max(u) - min(u)
        return delta

def fd(f, D):
    n = len(D)

    if f == 'f1':
        return sum(D)/n
    
    if f == 'f2':
        return sum(D)

D = pd.DataFrame({
    "idade": [18, 22, 25, 31, 40, 52],
    "renda": [1200, 1800, 2200, 3500, 5000, 7200],
    "cidade": ["A", "B", "A", "C", "B", "A"]
})

# Media das idades
media_idades = fd('f1', D['idade'])

print(media_idades)

# Somatorio de renda
somatorio_renda = fd('f2', D['renda'])
print(somatorio_renda)

u_idade = [0, 100]
u_renda = [0, 100000]

print(f"Sensibilidade global para f(D) = media das idades: {sg('f1', D, u_idade)}")

print(f"Sensibilidade global para f(D) = somatorio da renda: {sg('f2', D, u_renda)}")
