
velocidade = int(input("Digite a velocidade do carro:"))
velocidade_permitida = 80
multa = (velocidade - velocidade_permitida) * 7
if velocidade > velocidade_permitida:
    print(f"Você foi multado por exceder velocidade, terá que pagar multa de R${multa}")
else:
    print("Pode seguir!")
