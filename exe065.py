num = int(input("Digite um numero inteiro:"))
press = str(input("Quer continuar? [S/N]"))
qtd = 1
media = num
menor = num
maior = num
soma = num
while press != "n":
    num = int(input("Digite um numero inteiro:"))
    qtd+=1
    soma += num
    if num < menor:
        menor = num
    if num > maior:
        maior = num
    press = input("Quer continuar? [S/N]").lower()


media = soma / qtd
print("AQUI VÃO OS RESULTADOS EXTRAIDOS:\n" f"MEDIA:{media:.2f}\n" f"MAIOR:{maior}\n" f"MENOR:{menor}")

