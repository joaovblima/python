import random
lista = [0,1,2,3,4,5]
num_aleatorio = random.choice(lista)
num = int(input("Tente descobrir que número inteiro eu escolhi de 0 a 5:"))

if num == num_aleatorio:
    print("Parabéns, você venceu!")
else:
    print("Você perdeu! Tente novamente!")


