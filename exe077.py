tupla = {"Aprender", "Familia", "Igreja", "Paciência",
         "Amor", "Felicidade", "Juntos", "Filhos", "Liberdade"}
vogais = {"a", "e", "i", "o", "u"}

for i in tupla:
    print(f"\nNa palvra {i} há vogais: ", end="")
    for letra in i:
        if letra.lower() in vogais:
            print(letra, end="")