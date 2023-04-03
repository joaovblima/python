dias = float(input("Quantos dias alugados?"))
kmRodados = float(input("Quantos km rodados?"))
valorDia = dias * 60
valorKm = kmRodados * 0.15
valorTotal = valorDia+valorKm
#R$60,00 por dia e R$0.15 por km rodados
print(f"O total a pagar é R${valorTotal:.2f}")