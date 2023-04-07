
num = int(input("Digite um numero inteiro:"))

for i in range(2, num):
    if num % i==0:
        print(f"{num}Não é numero primo")
        break
else:
    print(f" {num}   É número primo")