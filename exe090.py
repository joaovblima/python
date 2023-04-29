aluno = dict()

aluno['Nome'] = str(input("Nome:"))
aluno['Média'] = float(input("Média:"))
print("-="*20)
print(f"O nome é igual a {aluno['Nome']}")
print(f"A média do aluno é {aluno['Média']}")
if aluno['Média'] < 7.0:
    print("REPROVADO.")