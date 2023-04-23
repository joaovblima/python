
num = []
for i in range(0,5):
    valores = int(input("Digite um valor:"))
    if i == 0 or valores > num[-1]:
        num.append(valores)
        print("Adicionado ao fim da lista")
    else:
        posicao = 0
        while posicao < len(num):
            if valores <= num[posicao]:
                num.insert(posicao, valores)
                print(f"Adicionado a posição {posicao} da lista")
                break
            posicao+=1

print(f"Os valores digitados foram {num}")
