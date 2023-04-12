'''
062: Melhore o desafio 061, perguntando para o usuario
se ele quer mostrar mais alguns termos. O programa encerra
quando ele disser que quer mostrar 0 termos.
'''
print("Vamos calcular sua PA")
a1 = int(input("Digite o primeiro termo:"))
r = int(input("Digite a razao:"))

while True:
    for i in range(10):
        pa = a1 + i*r
        print(pa)

    press = int(input("DESEJA CONTINUAR?\n" "[0]NÃO\n" "[1]SIM\n"))
    if press == 1:
        print("Digite novos numeros:")
        a1 = int(input("Digite o primeiro termo:"))
        r = int(input("Digite a razao:"))
    else:
        print("Programa encerrado.")
        break
