
def maior( * valores):
    cont = 0
    maior = 0
    print("\nAnalisando os valores passados...")
    for valor in valores:
        print(f'{valor}', end=" ",)
        cont += 1

    if cont == 0:
        maior = valor
    else:
        if valor>maior:
            maior= valor
    print(f"Foram informados {cont} valores ao todo.")
    print(f"O maior valor informado foi {maior}")

maior(9,17,54,43)
maior(55,78,54,92,113)
maior(17,3)
maior(6)