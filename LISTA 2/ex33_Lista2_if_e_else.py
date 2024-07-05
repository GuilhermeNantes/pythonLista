print("""
Especificação:     | Código |        |Preço|
Hot Dog            |  100   |        |12.00|
X-Salada           |  102   |        |18.50|
X-BACON            |  103   |        |25.50|
X-Burguer          |  104   |        |17.00|
Suco de Laranja    |  105   |        |9.50 | 
Refrigerante       |  106   |        |6.00 | """)
print()
cod = str(input("digite o codigo do produto: "))

nq = int(input("digite o quantidade: "))
if cod == "100":
    m = nq * 12
    print("Hot Dog na quantidade x",nq)
    print("o preco foi",m)
else:
    if cod == "102":
        m = nq * 12
        print("X-Salada na quantidade x",nq)
        print("o preco foi",m)
    else:
        if cod in "103":
            z = nq * 18.5
            print("X-BACON na quantidade x",nq)
            print("o preco foi",z)
        else:
            if cod in "104":
                x = nq * 25.5
                print("X-Burguer  na quantidade x",nq)
                print("o preco foi",x)
            else:
                if cod in "105":
                    c = nq * 17
                    print("Suco de Laranja na quantidade",nq)
                    print("o preco foi",c)
                else:
                    if cod in "106":
                        v = nq * 9.5
                        print("Refrigerante na quantidade ",nq)
                        print("o preco foi",v)
                    else:
                        print("erro: codigo invalido")