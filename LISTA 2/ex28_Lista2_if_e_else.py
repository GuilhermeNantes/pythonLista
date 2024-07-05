confique = input("digite sua forma de conta  \n ex: 'mai' maior ou menor dos dois numeiro \n     'div' divisão dos dois numeiro \n     'soa' soma dos dois numeiro\n")
n1 = int(input("digite n1 "))
n2 = int(input("digite n2 "))

if confique in "div":
    c = n1 / n2
    print("a divisão foi a ",n1,"/",n2,"=",c)
if confique in "soa": 
    d = n1 + n2
    print("a soma foi a ",n1,"+",n2,"=",d)
if confique in "mai":
    if n1 > n2:
        print(n1," é maior do que ",n2)
    else: 
        print(n2," é maior do que ",n1)