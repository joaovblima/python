
mat= []
for i in range (0,3):
    linha = []
    for j in range(0,3):
        num = int(input(f"Digite um valor para {[(i),(j)]}:"))
        linha.append(num)
    mat.append(linha)

for linha in mat:
    for elemento in linha:
        print("{:4d}" .format(elemento), end="")
    print()
'''
mat = [[ 0,0,0], [0,0,0], [0,0,0]]

for i in range(0,3):
    for j in range(0,3):
        mat[i][j] = int(input(f"Digite um valor para {[(i), (j)]}:"))

for i in range (0,3):
    for j in range(0,3):
        print(f"[{mat[i][j]}]", end="")
    print()
'''