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
        print("Caso 2: Deu coroa seguido de cara e disse sua resposta falsa")
        mentira = moeda[1-moeda.index('cara')]
        print(mentira)
    else:
        terceira_moeda = random.choice(moeda)

        if terceira_moeda == 'cara':
            print("Caso 3: Deu coroa seguido de coroa seguido de cara e disse \'Sim\' como resposta")
            print("Sim")
        else:
            print("Caso 4: Deu coroa seguido de coroa seguido de coroa e disse \'Não\' como resposta")
            print("Não")


