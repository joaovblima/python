

print("Digite dois numeros inteiros.")
num1 = int(input("Primeiro:"))
num2 = int(input("Segundo:"))
if num1 > num2:
    print(f"{num1} é maior que {num2}")
elif num2 > num1:
    print(f"{num2} é maior que {num1}")
elif num1 == num2:
    print("Não existe valor maior, os dois são iguais.")