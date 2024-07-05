## Se o preço de aquisição de um produto é menor que R$ 50,00, ele deve ser
## vendido por um preço 45% maior, caso contrário o lucro será de 30%. Sabendo disso, Crie um
## algoritmo que leia o valor de aquisição de um produto e mostre o seu valor de venda.
v1 = float(input("Digite um numeiro"))

if(v1 <= 50.0):
    v2 = (v1 * 45) / 100
    print(f"o valor {v1} aquisação e o valor de: {v2}")
else:
    v3 = (v1 * 30) / 100
    print(f"o valor {v1} aquisação e o valor de: {v3}")
 