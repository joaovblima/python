
def area(l,c):
    ar = l * c
    return ar


print("CONTROLE DE TERRENOS")
print("-"*30)
l = float(input("LARGURA (m):"))
c = float(input("COMPRIMENTO(m):"))
a = area(l, c)
print(f"A área de um terreno de {l}x{c} é de {a:.1f} m²")
