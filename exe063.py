'''
063: Escreva um programa que leia um numero n inteiro qualquer
e mostre na tela os n primeiros elementos de uma Sequencia de
Fibonacci.
'''

'''
Sequencia Fibonacci é uma sequencia matematica em que cada termo é a soma dos dois termos anteriores, começando com 
0 e 1.
'''
print("SEQUENCIA FIBONACCI")
n = int(input("Quantos termos da sequência de Fibonacci você quer gerar? "))
t1 = 0
t2 = 1
print(f"{t1} ↦ {t2}", end="")
cont = 3
while cont <=n:
    t3 = t1 + t2
    print(f"  ↦ {t3}", end="" )
    t1 = t2
    t2 = t3
    cont+=1
print("  ↦ FIM")





