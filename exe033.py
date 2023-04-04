num1 = int(input("Digite um numero:"))
num2 = int(input("Digite um segundo numero:"))
num3 = int(input("Digite um terceiro numero:"))

if num1 > num2 and num1 > num3:
    print(f"{num1} é maior que os outros.")
elif num2 > num1 and num2 > num3:
    print(f"{num2} é maior que os outros.")
else:
    print(f"{num3} é maior que os outros.")