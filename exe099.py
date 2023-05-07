
import random

def sorteia(lista):
    print("Sorteando os 5 valores da lista: ", end="")
    for i in range(5):
        num = random.randint(1,10)
        lista.append(num)
        print(f"{num}", end=" ")


def somaPar(lista):
    soma = 0
    for i in numeros:
        if i % 2 ==0:
            soma +=i
    print(f"\nA soma dos valores pares é {soma}")

numeros = list()
sorteia(numeros)
somaPar(numeros)