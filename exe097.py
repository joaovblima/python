
import time
def contador(i, f, p):
    return [i for i in range(i, f+1, p)]

def div():
    return print("-=" * 30)

div()
print("Contagem de 1 até 10 de 1 em 1:")
time.sleep(1)
contagem = contador(i=1, f=10, p=1)
print(*contagem, end=" ")
print("FIM!")
div()

print("Contagem de 10 até 0 de 2 em 2")
time.sleep(1)
contagem= contador(i=10, f=-2, p=-2)
print(*contagem, end=" ")
print("FIM!")
div()


print("Agora é sua vez de personalizar a contagem!")
inicio = int(input("Inicio:"))
fim =  int(input("Fim:"))
passo = int(input("Passo:"))

contagem = contador(i=inicio, f=fim, p=passo)
print(*contagem, " ",  end="")
print("FIM!")

