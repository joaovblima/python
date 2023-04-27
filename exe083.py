
expressao = str(input("Digite uma expressão:"))
pilha = []
for simb in expressao:
    if simb == "(":
        pilha.append("(")
    elif simb == ")":
        if len(pilha)>0:
            pilha.pop