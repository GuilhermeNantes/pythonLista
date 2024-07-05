nota1 = float(input("Digite um numeiro: "))
nota2 = float(input("Digite um numeiro: "))

if(nota1 >= 0 or nota1 <= 10):
    if (nota2 >= 0 or nota2 <= 10):
        m = (nota1 + nota2) / 2
        print(f"a suas notas foram essas:\n primeira nota:{nota1}\n segunda nota:{nota2}\n vamos ve qual sua media:{m}")
else:
    print("nota ivalida invalido")