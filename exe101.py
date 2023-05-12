
def fatorial (num, show=False):
    """ Calcula o fatorial de um numero.

    Args:
        num (_type_): Valor inteiro a ser calculado
        show (bool, optional): Irá mostrar toda operação, do valor inicial ao final. Defaults to False.

    Returns:
        _type_: Retorna o valor fatorial de um numero.
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show:
            print(f"{c}", end="")
            if c > 1:
                print(' x ', end="")
            else:
                print(' = ', end="")
    return f 


f1 = int(input("Digite um numero para ver o seu fatorial:"))
print(fatorial(f1, show=False))


    