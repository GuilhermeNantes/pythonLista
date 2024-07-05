nota0 = float(input("digite sua nota"))
nota1 = float(input("digite sua nota"))
nota2 = float(input("digite sua nota"))
if nota0 < 10 and nota0 > 0:
    print("essa foi a nota é invalida ",nota0)
elif nota1 < 10 and nota1 > 0:
    print("essa foi a nota é invalida ",nota1)
elif nota2 < 10 and nota2 > 0:
    print("essa foi a nota é invalida ",nota2)
else:
    print("gerando boledin")
           
media= (nota1+nota0+nota2)/3
print(media)
if media > 3.9:
   print("recuperaçao")
elif media > 5.9:
    print("aprovado")
else:
    print("repovado")

  
