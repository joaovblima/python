larg = float(input("Largura da parede:"))
alt = float(input("Altura da parede:"))
area = larg * alt
tinta = area / 2
#cada 2m2 de parede precisa de 1 lt de tinta
print(f"Sua parede tem a dimensão de {larg}X{alt} e sua área é de {area:.3f}m²")
print(f"Para pintar sua parede, você precisará de {tinta:.2}l de tinta")

