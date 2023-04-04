nome = str(input("Digite seu nome completo:"))
caps = nome.upper()
minus = nome.lower()
cont = len(nome.replace(" ",""))
print(f"Esse é {nome} em maiusculo: {caps}")
print(f"Esse é {nome} em minusculo: {minus}")
print(f"Seu nome tem {cont} caracteres")

