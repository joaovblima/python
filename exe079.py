
num = []
while True:
    valores = int(input("Digite um numero:"))
    if valores not in num:
        num.append(valores)
    else:
        print(("Valor duplicado... Tente novamente."))
    seguir = str(input("Deseja acontinuar? [S/N]")).strip().lower()[0]


    if seguir == "n":
        break

for i in range(len(num) -1, -1, -1):
    print(num[i])