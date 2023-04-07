'''
054: Crie um programa que leia o ano de nascimento de sete
pessoas. No final, mostre quantas pessoas ainda não
atingiram a maioridade (21 anos) e quantas já são maiores.
'''

ano_atual = int(input("Digite o ano atual:"))
maiores = 0
menores = 0
for i in range(1,8):
    ano_nascimento = int(input("Digite o ano de nascimento de sete pessoas:"))
    idade = ano_atual- ano_nascimento
    if idade >= 21:
        maiores+=1
    else:
        menores+=1
print(f"{maiores} Já são maiores de idade")
print(f"{menores} pessoas ainda não atingiram a maioridade")

