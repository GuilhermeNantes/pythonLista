lista = []
c = 0
while c <= 5:
    lista.append(int(input("num limite: ")))
    c +=1
    print(c-1)
print(f"o maior numeiro digitado foi :{max(lista)}")