
num1 = int(input("Digite um numero:"))
num2 = int(input("Digite um segundo numero:"))
num3 = int(input("Digite um terceiro numero:"))
num4 = int(input("Digite o quarto e ultimo numero:"))
tupla = (num1, num2, num3, num4)
cont9 = 0
cont_Pares= 0

if 9 in tupla:
    cont9 += 1

for i in tupla:
    if i % 2==0:
        cont_Pares+=1

print(f"Esses foram os numeros digitados: {tupla}")
print(f"O numero 9 apareceu {cont9} vezes")
print(f"Possui {cont_Pares} numeros pares")
if 3 in tupla:
    print(f"O numero 3  apareceu na posição {tupla.index(3)}")
else:
    print("O numero 3 nao foi digitado em nenuma posição")