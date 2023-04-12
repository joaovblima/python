'''057: Faça um programa que leia o sexo de uma pessoa, mas
só aceite os valores 'M' ou 'F'. Caso esteja errado, peça
a digitação novamente até ter o valor correto.
'''

sexo = str(input("Digite seu sexo [M/F]:"))
while sexo != 'M' and sexo !='F':
    sexo = (input("Dados inválidos. Digite seu sexo novamente [M/F]:"))


print(F"Sexo {sexo} registrado com sucesso")