matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
soma= 0
for o in range(3):
    for d in range(3):
         print(d,o) 
         if o == d:
            soma = soma + matriz[o][d]
print(matriz,soma)