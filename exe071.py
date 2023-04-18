
print("=" *20)
print("  " , "NOVENOVE BANK")
print("="*20)

valor = int(input("Qual valor você quer sacar? R$"))
total = valor
ced = 50
contCed = 0

while True:
    if total >= ced:
        total -= ced
        contCed+=1
    else:
        print(f"Total de {contCed} cedulas de R$ {ced}")
        if ced ==50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced ==10:
            ced = 1
        contCed=0
        if total == 0:
            break

