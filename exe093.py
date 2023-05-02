dados_jogador = {}
somagols= 0
lista_gols = []

while True:

    dados_jogador["Nome"] = str(input("Nome do jogador:"))
    dados_jogador["N° de partidas"] = int(input("Quantas partidas jogou?"))

    for i in range(dados_jogador["N° de partidas"]):
        gols = int(input(f"Quantos gols na partida {i+1}:"))
        somagols += gols
        dados_jogador["Gols"] = somagols
        lista_gols.append(gols)

    print("-=" * 20)

    for chave, valor in dados_jogador.items():
        print(f"{chave}: {valor}")

    print("-=" *20)

    print(f'O jogador {dados_jogador["Nome"]} jogou {dados_jogador["N° de partidas"]} partidas e marcou {dados_jogador["Gols"]} gols.')

    continuar = str(input("Deseja continuar? [S/N]")).strip().lower()
    if continuar == "n":
        break
