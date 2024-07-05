ano = int(input("digite um ano para saber se é bisseto"))
cna = ano % 400 and ano % 4
if cna == 0:
    print("é ano bisseto",ano)
else:
    print("nao é bisseto",ano)