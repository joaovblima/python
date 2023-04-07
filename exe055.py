''' 055: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior peso e o menor peso lidos.
'''

pesagens = []
for i in range(1,6):
    peso= float(input("Digite o peso de 5 pessoas:"))
    pesagens.append(peso)

maior = max(pesagens)
menor = min(pesagens)

print(f"O maior peso é {maior}KG")
print(f"O menor peso é {menor}KG")

