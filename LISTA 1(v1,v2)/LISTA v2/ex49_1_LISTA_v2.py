print("Tamanhos:  [1]Refigerante de 350m [2]Refigerante de 600ml [3]Refigerante de 2l")

tmn = int(input("Qual opção de refrigerante você quer[escolha a opção numérica]: "))

numR = int(input("Quantas unidades serão compradas: "))

if tmn == 1:
    print(f"{numR} Refigerante de 350ml serão {0.35 * numR}l de refrigerante")
elif tmn == 2:
    print(f"{numR} Refigerante de 600ml serão {0.6 * numR}l de refrigerante")
elif tmn == 3:
    print(f"{numR} Refigerante de 2l sairá serão {2 * numR}l de refrigerante")
else:
    print("Valor não incluso na lista")