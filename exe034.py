salario = float(input("Digite seu salário:"))
if salario > 1250:
    aumento1= salario * 0.10 + salario
    print(f"Houve um aumento de 10% em seu salário, agora você passa a receber R${aumento1}")
elif salario<=1250:
    aumento2= salario * 0.15 + salario
    print(f"Houve um aumento de 15% em seu salário, agora você passa a receber R${aumento2}")