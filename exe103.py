def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok=True
        else:
            print("Erro, digite valor válido!")
        if ok:
            break
    return valor 

n = leiaInt("Digite um numero:")
print(f"Você digitou o valor {n}")