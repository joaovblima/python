
def ficha(jogador=None, gols=0):
    
    if jogador is not None:
        print(f"O jogador {player}", end="")
    else:
        print("O jogador <desconhecido>", end=" ")
    
    if gols:
        print(f" Fez {goals} gol(s) no campeonato.")
    else:
        print(" não marcou gols no campeonato")
    return ficha
    
player = input("Nome do jogador:")
if player.strip() == "":
    player = None
goals = input("Numero de gols:")
if goals.strip() == "":
    goals = 0
else: 
    goals = int(goals)

print(ficha(player, goals))
    