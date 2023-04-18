soma = 0
qtd = 0
while True:
    num = int(input("Digite um numero inteiro:"))
    if num == 999:
        break
    qtd+= 1
    soma+=num
print(f"Foi digitado {qtd} numeros e a soma entre eles foi {soma}")
