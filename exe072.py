contagem = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", "Onze", "Doze", "Treze", "Catorze"
, "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte")

while True:
    num = int(input("Digite um entre 0 e  20:"))
    if 0 <= num <= 20:
        break
    print("Tente novamente. ", end="")
print(f"Você digitou o numero {contagem[num]}")
