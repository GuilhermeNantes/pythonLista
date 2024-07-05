print("Lata de 18L curstam em média R$80,00")
print("Galão de 3,6L curstam em média R$25,00")

ms = float(input("Digite os metros a serem pintados: "))

abs = ms / 6

if abs <= 21:
    print("Compre apenas galões de 3,6L")

elif abs >= 108:
    print("Compre apenas um galão de 18L")

else:
    print("alem de mais de dez porcento no mais de uma lata e galao")
