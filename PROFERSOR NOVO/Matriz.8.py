matriz = [
     [1,2,11,13],
     [4,15,16,60],
     [7,8,19,200],
     [20,100,5,3]
     ]

for i in range(len(matriz)):
     for o in range(len(matriz[0])):
         tudo = matriz[i][o]
         if tudo > 10:
            print("valor maior de dez:",tudo)