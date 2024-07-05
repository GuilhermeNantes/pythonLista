prc = int(input("digite o valor da compra: "))

if prc >= 0 and prc < 50:
    m = prc * 0.05
    print("o preço é o desconto",m)
else:
    if  prc > 50 and prc < 100:
        m = prc * 0.1
        print("o preço é o desconto",m)
    else:
        z = prc * 0.15
        print("o preço é o desconto",z)
           