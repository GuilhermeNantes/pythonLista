palito = str(input("DIGITE UM NUMERO"))
priT = int(palito[0])
sedT = int(palito[1])
treT = int(palito[2])
patinho = priT+sedT+treT

if patinho >= 0 :
    if patinho % 100 == 0:
        priT = int(palito[0])
        soma = priT
        print(priT," =",soma)
    elif patinho % 10 == 0:
        priT = int(palito[0])
        sedT = int(palito[1])
        soma = priT + sedT
        print(priT,"+ ",sedT," =",soma) 
    elif patinho % 1 == 0:
        priT = int(palito[0])
        sedT = int(palito[1])
        treT = int(palito[2])
        soma = priT+ sedT + treT
        print(priT,"+ ",sedT,"+ ",treT," =",soma)
    else:
        print('tem o limite de três termos')
else:
    print("invalido")

