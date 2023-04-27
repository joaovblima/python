
lista1 = []
impar = []
par = []
for i in range (0,7):
    num = int(input(f"Digite o {i+1}° numero: "))
    lista1.append(num)
for i in lista1:
    if i % 2 == 1:
        impar.append(i)
    else:
        par.append(i)
print("=-"*30)
print(lista1)
print(f"Os valores pares digitados foram: {sorted(par)}")
print(f"Os valores impares digitados foram: {sorted(impar)}")