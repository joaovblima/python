from random import randint
numeros = []
for i in range(5):
    numeros.append(randint(1,100))
print(f"Os valores sorteados foram: {numeros}")
print(f"O menor numeros sorteado foi: {min(numeros)}")
print(f"O maior numero sorteado foi: {max(numeros)}")