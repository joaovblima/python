notaA= float(input("Qual a primeira nota?"))
notaB = float(input("Qual a seguinda nota?"))

media = (notaA + notaB)/2
if media >= 7.0:
    print("A media: %.1f - APROVADO" % media)
else:
    print("A media: %.1f - REPROVADO " % media)