data = int(input("Digite o ano que você nasceu?"))
anoAtual = 2023
idade = 2023 - data
tempo = idade - 18
if idade < 18:
    print(f"Tudo tranquilo, ainda vai chegar seu periodo de alistamento, faltam {tempo} anos.")
elif idade == 18:
    print("Guerreiro, é hora de se alistar.")
elif idade > 18:
    print(f"Já passou do tempo de se alistar. Você está atrasado {tempo} anos")
