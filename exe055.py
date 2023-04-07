pesagens = []
for i in range(1,6):
    peso= float(input("Digite o peso de 5 pessoas:"))
    pesagens.append(peso)

maior = max(pesagens)
menor = min(pesagens)

print(f"O maior peso é {maior}KG")
print(f"O menor peso é {menor}KG")

