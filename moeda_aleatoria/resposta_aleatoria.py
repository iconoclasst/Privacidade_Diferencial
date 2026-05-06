import random

moeda = ['cara', 'coroa']

resposta = input("Sim ou Nao? ")
print(f"Resposta verdadeira: \'{resposta.capitalize()}\'")

print("Resposta randomizada: ")

primeira_moeda = random.choice(moeda)
if primeira_moeda == 'cara':
    print("Caso 1: deu cara e disse a resposta verdadeira.")
    print(f"\'{resposta.capitalize()}\'")

else:
    segunda_moeda = random.choice(moeda)
    
    if segunda_moeda == 'cara':
        print("Caso 2: Deu coroa seguido de cara e disse \'Sim\' como resposta")
        print("Sim")
    else:
        print("Caso 3: Deu coroa seguido de coroa e disse \'Nao\' como resposta")
        print("Nao")


