#017: faça um programa que leia o comprimento do cateto oposto e o cateto adjacente de um triangulo retangulo, calcule
#e mostre o comprimento da hipotenusa
import math
cateto1 = int(input("Digite o cateto oposto:"))
cateto2 = int(input("Digite o cateto adjacente:"))
hipot = math.hypot(cateto1, cateto2)
print(f"A hipotenusa é: {hipot:.2f}")
