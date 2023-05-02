dados = {}
while True:
    dados["Nome"] = str(input("Nome:"))
    dados["Ano De Nascimento"] = int(input("Ano de nascimento:"))
    dados["Carteira de Trabalho"] = int(input("Carteira de Trabalho [Aperte 0 se não tiver]:"))
    if dados["Carteira de Trabalho"] == 0:
        print("-=" * 30)
        for chave, valor in dados.items():
            print(f"{chave}: {valor}")

        break


    else:
        dados["Ano de Contratação"] = int(input("Ano de contratação:"))
        dados["Salário"] = int(input("Salário: R$"))
        aposentadoria = dados["Ano de Contratação"] + 35
        dados["Aposentadoria"] = aposentadoria
        idade = 2023 - dados["Ano De Nascimento"]
        dados["Idade"] = idade


    print("-="*30)
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")
    break