
numeros = []
n_five= 5
while True:
    valores = int(input("Digite um numero:"))
    seguir = str(input("Deseja continuar? [S/N]")).strip().lower()
    numeros.append(valores)
    tamanho = len(numeros)
    nova_lista = sorted(numeros)


    if seguir == "n":
        break
print("=-"*30)
print(f"{tamanho} numeros foram digitados\n",f"Aqui está sua lista organizada: {nova_lista}")
if n_five in numeros:
    print("O número 5 está na lista.")
else:
    print("O número 5 não está na lista.")