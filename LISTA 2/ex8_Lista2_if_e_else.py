##Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do
##número. Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.
v1 = float(input("Digite um numeiro"))
import math
if(v1 >= 0):
    raiz = math.sqrt(v1)
    print("valor do seu numeiro é ",raiz,)

else:
    print("valor invalido")

