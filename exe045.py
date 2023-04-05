import random

print("Vamos jogar pedra, papel e tesoura hihihi")
jogador = str(input("Escolha Pedra, Papel ou Tesoura?"))
lista = ['Pedra', 'Papel', 'Tesoura']
escolha_computador = random.choice(lista)
print(f"O computador escolheu {escolha_computador}")
if jogador == 'Pedra' and escolha_computador == 'Papel':
    print("HAHA, o computador venceu")
elif jogador == 'Papel' and escolha_computador == 'Pedra':
    print("VOCÊ VENCEU =(")
elif jogador == 'Pedra' and escolha_computador == 'Tesoura':
    print("VOCÊ VENCEU =(")
elif jogador == 'Tesoura' and escolha_computador =='Pedra':
    print("HAHA, o computador venceu")
elif jogador == 'Tesoura' and escolha_computador == 'Papel':
    print("VOCÊ VENCEU =(")
elif jogador == 'Papel' and escolha_computador == 'Tesoura':
    print("HAHAHA, o computador venceu")
elif jogador == 'Papel' and escolha_computador == 'Papel':
    print("Ninguem venceu")
elif jogador == 'Pedra' and escolha_computador == 'Pedra':
    print("Ninguem venceu")
elif jogador == 'Papel' and escolha_computador == 'Papel':
    print("Ninguem venceu")
