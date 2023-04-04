distancia = int(input("Digite a distancia percorrida em KM:"))

if distancia <=200:
    preco1 = distancia * 0.50
    print(f"Total á pagar é de R${preco1:.2f} ")
else:
    preco2 = distancia * 0.45
    print(f"Total a pagar é de R${preco2:.2f}")

