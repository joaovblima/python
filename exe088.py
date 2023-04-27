import random
print("-="*30)
print(" " * 18, "LOTERIA NOVENOVE\n", "-=" * 30)
num_jogos = int(input("Quantos jogos você quer que eu sorteie?"))

jogos = []

for i in range(num_jogos):
    jogos.append([])

for jogo in jogos:
    for j in range(6):
        sorteio = random.randint(1, 60)
        jogo.append(sorteio)

for i, jogo in enumerate(jogos):
    print(f"Jogo {i+1}: {jogo}")
