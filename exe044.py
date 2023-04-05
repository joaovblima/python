precoProduto = float(input("Digite o preco do produto: R$"))
opcao = int(input("Escolha as formas de pagamento: \n1 - a vista/cheque (10% de desconto) \n2 - a vista no cartao: (5% de desconto) \n3- 2x no cartao você paga o preço normal \n4- 3X ou mais no cartao  (20% de juros)\n"))
if opcao == 1:
    valor_a_pagar= precoProduto - (precoProduto * 0.10)
    print(f"Com desconto aplicado você vai pagar R${valor_a_pagar}")
elif opcao ==2:
    valor_a_pagar = precoProduto - (precoProduto * 0.05)
    print(f"Com desconto aplicado você vai pagar R${valor_a_pagar}")
elif opcao ==3:
    print(f"Não há desconto, você irá pagar R$ {precoProduto}")
elif opcao ==4:
    valor_a_pagar = precoProduto + (precoProduto* 0.20)
    print(f"Você irá ter um acrescimo de 20%, esse caso você irá pagar R${valor_a_pagar}")
