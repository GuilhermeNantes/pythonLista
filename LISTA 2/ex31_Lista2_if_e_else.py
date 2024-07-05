km = float(input("quantos Km você andou?"))
litro = float(input("litros consumidos ?"))
kmrodado = km / litro
if kmrodado < 8:
    print("Venda o carro!")
elif kmrodado > 8 and kmrodado < 11:
    print("Econômico!")
elif kmrodado > 12:
    print("Super econômico!") 