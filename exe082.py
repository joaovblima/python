
numeros = []
lista_par = []
lista_impar = []
while True:
    valores = int(input("Digite um numero:"))
    seguir = str(input("Quer continuar? [S/N]")).strip().lower()
    numeros.append(valores)

    if valores % 2 ==0:
        lista_par.append(valores)
    else:
        lista_impar.append(valores)


    if seguir =="n":
        break

print(f"Aqui está a lista digitada: {numeros}")
print(f"Aqui está uma lista de numeros pares: {lista_par}")
print(f"Aqui está uma lista de numeros impares: {lista_impar}")