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

