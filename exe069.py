
maior_18 = 0
cont_h = 0
mulheres_20 = 0

while True:
    nome = str(input("Digite o nome:"))
    idade = int(input("Digite a idade:"))
    sexo = str(input("Sexo [M/F]:")).strip().upper()[0]
    continuar = str(input("Quer continuar? [S/N]")).strip().lower()[0]

    if idade >= 18:
        maior_18 += 1

    if sexo == "M":
      cont_h += 1

    if sexo == "F" and idade <20:
        mulheres_20 += 1

    if continuar == "n":
        break

print(f"AQUI ESTÃO SEUS DADOS:\n" f"PESSOAS MAIORES DE 18: {maior_18} pessoas\n" 
      f"QUANTIDADE DE HOMENS CADASTRADOS:{cont_h}\n" f"QUANTIDADE DE MULHERES MENORES DE 20 ANOS: {mulheres_20} ")

