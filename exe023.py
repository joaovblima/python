numero = int(input("Digite um número de 0 a 9999: "))

unidade = numero % 10
numero = numero // 10

dezena = numero % 10
numero = numero // 10

centena = numero % 10
numero = numero // 10

milhar = numero % 10

print(f"Milhar:{milhar}")
print(f"Centena:{centena}")
print(f"Dezena:{dezena}")
print(f"Unidade:{unidade}")
