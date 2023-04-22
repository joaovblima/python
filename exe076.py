lista = ("Lapis", 1.70, "Caderno", 25.00, "Hidratante", 44.00, "Folha de papel A4", 17.00, "Macarrão", 3.50)
print('-'* 30)
print("LISTAGEM DE PREÇOS")
print("-" *30)
for pos in range (0, len(lista)):
    if pos % 2 == 0:
        print(f"{lista[pos]:.<30}", end="")
    else:
        print(f"R${lista[pos]:.>10.2f}")