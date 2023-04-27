
pessoas = []
dados = []
maior = -float("inf")
menor = float("inf")
while True:
    pessoas.append(str(input("Nome:")))
    pessoas.append(float(input("Peso:")))

    if len(pessoas) == 0:
        maior = menor = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        if pessoas[1] < menor:
            menor = pessoas[1]

    dados.append(pessoas[:])
    pessoas.clear()
    continuar = str(input("Deseja continuar? [S/N]")).strip().lower()
    if continuar == "n":
        break

print("-="*30)
print(f"{len(dados)} pessoas foram cadastradas")
print(f"O maior peso foi de {maior}KG de ", end="")
for p in dados:
    if p[1] == maior:
        print(f"[{p[0]}]", end="")
print()
print(f"O menor peso foi de {menor}KG de ", end="")
for p in dados:
    if p[1] == menor:
        print(f"[{p[0]}]")
