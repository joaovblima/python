nomeCompleto = str(input("Digite seu nome completo:"))
palavras = nomeCompleto.split()
primeiro_nome = palavras[0]
segundo_nome = palavras[-1]
print(f"Primeiro nome: {primeiro_nome}")
print(f"Ultimo nome: {segundo_nome}")