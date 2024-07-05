print("digite a , b , c para midir a area do triangulo.....\n")

a = int(input("digite um numeiro"))
b = int(input("digite um numeiro"))
c = int(input("digite um numeiro"))
if a == b == c and b == c == a:
        print("um triangulo equilatro")
elif a == b  or  b == c or a == c:
        print('um triangulo isosceleo')
elif a < (b+c) and b <(c+a) and c <(a+b):
        print("é um escalono")

