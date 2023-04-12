
somaidade=0
mediaidade=0
nome_velho = ''
maior_idade_homem = 0
idade_mulher = 0

for i in range(1,5):
    print(f"----- {i}ªPESSOA ----- " )
    nome = str(input("Nome:"))
    idade = float(input("Idade:"))
    sexo = input("SEXO [M/F]:").strip().upper()
    somaidade+=idade
    if i ==1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Ff'and idade<20:
        idade_mulher+=1
mediaidade = somaidade/4
print(f"A media de idade do grupo é {mediaidade} anos")
print(f"O homem mais velho tem {maior_idade_homem} anos e se chama {nome_velho}.")
print(f"{idade_mulher} mulheres tem menos de 20 anos")




