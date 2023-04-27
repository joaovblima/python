
mat =  [[ 0,0,0], [0,0,0], [0,0,0]]
pares = 0
soma_col = 0
for i in range(0,3):
    for j in range(0,3):
        mat[i][j] = int(input(f"Digite um valor para {[(i), (j)]}:"))

for i in range (0,3):
    for j in range(0,3):
        print(f"[{mat[i][j]}]", end="")
        if mat[i][j] % 2 == 0:
            pares+=mat[i][j]
    print()

print("-=" *30)
print(f"A soma dos valores pares digitados é {pares}")
for i in range(0,3):
    soma_col+=mat[i][2]
print(f"A soma dos valores da terceira coluna é {soma_col}")
print(f"O maior valor da segunda linha é {max(mat[1])}")

