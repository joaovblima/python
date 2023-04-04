#018: faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo
import math
ang = float(input("Digite um ângulo:"))
seno = math.sin(ang)
cosseno = math.cos(ang)
tang = math.tan(ang)

print(f"Seu angulo é: {ang}")
print(f"Seno: {seno:.2f}")
print(f"Cosseno: {cosseno:.2f}")
print(f"Tangente:{tang:.2f}")
