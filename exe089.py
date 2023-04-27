nomes = []
notas1 = []
notas2 = []
medias = []
while True:
    nome = str(input("Nome:"))
    nota1 = float(input("Nota 1:"))
    nota2 = float(input("Nota 2:"))
    seguir = str(input("Deseja continuar: [S/N]")).strip().lower()
    nomes.append(nome)
    notas1.append(nota1)
    notas2.append(nota2)


    if seguir == "n":
        break

for i in range(len(nomes)):
        media = (notas1[i] + notas2[i]) / 2
        medias.append(media)

print("-="*30)
print(f'{"No.":<4}{f"NOMES":<10}{"MÉDIA":>8}')
for i, j in enumerate(nomes):
    print(f"{i:<4} {nomes[i]:<10} {medias[i]:>7.1f}")

while True:
    notas_aluno = int(input("Mostrar notas de qual aluno? (999 interrompe)"))
    if notas_aluno == 999:
        print("Finalizando...")
        break
    if notas_aluno <= len(nomes) - 1:
        print(f"Notas de {nomes[notas_aluno]} são {notas1[notas_aluno]:.1f} e {notas2[notas_aluno]:.1f}")


