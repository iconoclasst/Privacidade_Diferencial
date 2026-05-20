import random
import numpy as np


def media(D):
    return sum(D)/len(D)

# U = [0 - 20]
D = [10, 12, 11, 13, 12, 10]
D1 = random.sample(D, len(D)-1)


print(D)
print(D1)

sensibilidade_global = (20-0)/len(D)

AD = media(D)
AD1 = media(D1)

print("Média de D: {:.2f}".format(AD))
print("Média de D':{:.2f}".format(AD1))
print("Sensibilidade global: {:.2f}".format(sensibilidade_global))

epsilon = 1.0
escala = sensibilidade_global/epsilon

# M(D) = f(D) + Laplace(0, escala)
MD = AD + np.random.laplace(0, escala)
MD1 = AD1 + np.random.laplace(0, escala)

print("\nResultado privado: {:.2f}".format(MD))
print("Resultado privado: {:.2f}".format(MD1))

