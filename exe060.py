num = int(input("Digite um número inteiro: "))
fatorial = 1
i = 1

while i <= num:
    fatorial *= i
    i += 1

print(f"O fatorial de {num} é {fatorial}")
