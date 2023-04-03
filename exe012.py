preco = float(input("Qual é o preço do produto? R$"))
desconto = preco * 0.05
valorNovo = (preco - desconto)
print(f"O produto que custava R${preco:.2f}, na promoção com desconto de 5% vai custar R${valorNovo}")
