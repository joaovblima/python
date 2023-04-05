casaValor = float(input("Digite o valor da casa? R$"))
salario = float(input("Qual é o seu salário? R$"))
meses = int(input("Em quantos meses você pretende pagar?"))
prestacao = casaValor/meses
porcentagem = salario * 0.30
if prestacao > porcentagem:
    print("Desculpe, seu emprestimo não pode ser realizado.")
else:
    print("Parabéns, seu emprestimo foi aprovado.")
    print(f"Você irá pagar {meses} parcelas de R${prestacao}.")