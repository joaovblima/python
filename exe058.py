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
