#019: um professor quer sortear um dos seus quatro alunos para o quadro. faça um programa que ajude ele, lendo o nome deles
#e escrevendo o nome do escolhido
import random

nome1= str(input("Qual o nome do primeiro aluno:"))
nome2= str(input("Qual o nome do segundo aluno:"))
nome3= str(input("Qual o nome do terceiro aluno:"))
nome4= str(input("Qual o nome do quarto aluno:"))
lista = [nome1, nome2, nome3, nome4]
escolhido = random.choice(lista)
print(f"Quem vai para o quadro é: {escolhido}")