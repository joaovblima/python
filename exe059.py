valor1 = float(input("Primeiro valor:"))
valor2 = float(input("Segundo valor:"))
soma = 0
multi = 0
maior= 0
press = 0
while press != 5:
    press= int(input("MENU:\n" "[1]SOMA\n" "[2]MULTIPLICAR\n" "[3]MAIOR\n" "[4]NOVOS NUMEROS\n" "[5]SAIR DO PROGRAMA\n"))
    if press ==1:
        soma= valor1+valor2
        print(f"A soma de {valor1:.0f} e {valor2:.0f} é igual a {soma:.0f} ")
    elif press ==2:
        multi= valor1 * valor2
        print(f"O valor da multiplicação entre {valor1:.0f} e {valor2:.0f} é de {multi:.0f}")
    elif press ==3:
        if valor1>valor2:
            maior = valor1
            print(f"{maior:.0f} é o maior número")
        else:
            maior = valor2
            print(f"{maior:.0f} é o maior número")
    elif press ==4:
        print("Digite novos numeros:")
        valor1 = float(input("Primeiro valor:"))
        valor2 = float(input("Segundo valor:"))
    elif press == 5:
        print("Programa encerrado")
    else:
        print("Opção inválida. Tente novamente!")



