
dados = {}
lista_dados = []
contador = 0
soma_idade = 0
media_idade = 0
lista_mulheres = []
pessoas_acima_media = []

while True:
    dados["nome"] = str(input("Nome:"))
    while True:
        dados["sexo"] = str(input("Sexo:")).strip().lower()
        if dados["sexo"] == "m" or dados["sexo"] == "f":
            break
        else:
            print("ERRO, digite apenas M ou F.")
    dados["idade"] = int(input("Idade:"))
    contador += 1
    lista_dados.append(dados.copy())
    soma_idade += dados["idade"]
    media_idade = soma_idade / contador
    if dados["sexo"] == "f":
        lista_mulheres.append(dados["nome"])

    continuar = str(input("Deseja continuar? [S/N]")).strip().lower()
    if continuar == "n":
        break

for pessoa in lista_dados:
    if pessoa["idade"] > media_idade:
        pessoas_acima_media.append(pessoa)

print(f"Quantidade de pessoas cadastradas: {contador}")
print(f"A média de idade do grupo é de: {media_idade:.1f} anos")
print(f"Lista das mulheres registradas: {lista_mulheres}")
print(f"Pessoas com idade acima da média: {pessoas_acima_media}")
