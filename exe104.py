
def notas(*n, situacao= False):
    """Funcao que calcular situação de alunos em relação suas notas.

    Args:
        situacao (bool, optional): Mostra qual situação que o aluno se encontra:(boa, razoável e ruim)

    Returns:
        _type_: retorna o dicionário, com o total de notas, media e maior e menor nota.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    
    if situacao:
        if r['media']>7:
            r['situacao'] = 'BOA'
        elif r['media']>=5:
            r['situacao'] = 'RAZOAVEL'
        else:
            r['situacao'] = 'RUIM'
            
    return r 
   
#Main Program
resposta = notas(2.0, 9.5,5.5, 8.8, 1.4, situacao=True)
print(resposta)