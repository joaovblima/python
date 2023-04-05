import random
num = int(input("Digite um numero inteiro:"))
print("Escolha as opções a seguir para transformar o seu número:")
escolha = int(input("1 - binario, 2 - octal, 3 - hexadecimal:"))

if escolha == 1:
    binario = bin(num)
    print(binario)
elif escolha ==2:
    octal = oct(num)
    print(octal)
else:
    hexadecimal = hex(num)
    print(hexadecimal)
