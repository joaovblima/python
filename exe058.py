'''058: Melhore o jogo do DESAFIO 0288 onde o computador vai
''pensar'' em um numero entre 0 e 10. Só que agora o jogador
vai tentar adivinhar até acertar, mostrando no final quantos
palpites foram necessarios para vencer.'''

from random import randint

pc = randint(0,10)
print("Tente adivinhar o numero inteiro de 0 a 10 que estou pensando?")
acertou = False
tentativas = 0
while not acertou:
    num = int(input("Qual seu palpite?"))
    tentativas+=1
    if num == pc:
        acertou = True
print(f"Parabéns, você acertou com {tentativas} tentativas.")