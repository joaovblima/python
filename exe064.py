'''
064: Crie um programa que leia varios umeros inteiros pelo
teclado. O programa so vai parar quando o usuario digitar o
valor 999, que é a condicao de parada. No final, mostre quantos
numeros foram digitados e qual foi a soma entre eles.
(desconsiderando o flag)
'''


num = int(input("Digite um numero [999 para parar]:"))
cont = 0
press = 0
soma = 0
qtd = 0
while num != 999:
    soma += num
    qtd += 1
    num = int(input("Digite um numero [999 para parar]:"))

print(f"Você digitou {qtd} numeros, a soma deles é {soma}")

