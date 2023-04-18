'''
70) Crie um programa que leia o nome e o preço de varios produtos. O programa deverá
perguntar se o usuario vai continuar. No final, mostre:
a) Qual é o total gasto na compra.
b) Quantos produtos custam mais de R$1000.
C) qUAL É o nome do produto mais barato.
'''

print("COMPRAS.")
soma = 0
contValores = 0
menor = float("inf")
produtoMenorValor = " "
while True:
    produtos = str(input("Digite o nome do produto:"))
    valor= float(input("Digite o valor do produto:"))
    seguir = str(input("Deseja acontinuar? [S/N]")).strip().lower()[0]
    soma+=valor

    if valor>1000:
        contValores+=1

    if valor < menor:
        menor = valor
        produtoMenorValor = produtos

    if seguir == "n":
        break
print(f"Valor gasto na compra foi de: R${soma:.2f}\n" f"{contValores} produtos custam mais de R$1000\n" 
      f"O produto de menor valor registrado foi {produtoMenorValor}")
