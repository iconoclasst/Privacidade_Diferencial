import random

def sensibilidade_global(f, D, U):
    n = len(D)

    if f.lower() == 'media':
        return (max(U) - min(U))//n
    if f.lower() == 'count':
        return 1

def f1(D):
    n = len(D)
    return sum(D)/n

def f2(D):
    return len(D)

U = [i for i in range (101)]

n = int(input("Tamanho do subconjunto: "))

D1 = random.sample(U, n)

sg1 = sensibilidade_global('media', D1, U)
sg2 = sensibilidade_global('count', D1, U)

print(f"A sensibilidade global pra {D1} em média e contagem é {sg1} e {sg2}")



