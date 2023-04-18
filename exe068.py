
from random import randint

print("Vamos jogar PAR OU IMPAR")
vitorias_consecutivas = 0

while True:
    jogador = int(input("Digite um número: "))
    pc = randint(0, 10)
    total = jogador + pc
    tipo = ' '

    while tipo not in 'PI':
        tipo = str(input("Par ou Impar? [P/I] ")).strip().upper()[0]

    print(f"Você jogou {jogador} e o computador {pc}. Total de {total} ")

    if total % 2 == 0:
        resultado = 'P'
    else:
        resultado = 'I'

    if tipo == resultado:
        print("Você venceu!")
        vitorias_consecutivas += 1
    else:
        print("Você perdeu!")
        break

print(f"Total de vitórias consecutivas: {vitorias_consecutivas}")



