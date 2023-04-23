
numeros = []

for i in range(0,5):
    num = int(input(f"Digite um valor para a posição {i}:"))
    numeros.append(num)

menor = min(numeros)
maior = max(numeros)
print("-="*30)
print(f"Você digitou os valores {numeros}")
print(f"O maior valor digitado foi {maior}, na posição ", end="")
for i, v in enumerate(numeros):
    if v == maior:
        print(f"{i}...")
print(f"O menor valor digitado foi {menor}, na posição ", end="")
for i, v in enumerate(numeros):
    if v == menor:
        print(f"{i}...")