
def voto (ano_nascimento):
    idade = 2023 - ano_nascimento
    print(f"Você tem {idade} anos:", end=" ")

    if idade < 0:
        raise ValueError("Ano de nascimento inválido")
    
    if idade < 18:
        return "VOTO NEGADO!"
    elif idade <65:
        return "VOTO OBRIGATÓRIO!"
    else:
        return  "VOTO OPICIONAL!"
    

print("-" * 25)

ano = int(input("Em que ano você nasceu?"))
print(voto(ano))