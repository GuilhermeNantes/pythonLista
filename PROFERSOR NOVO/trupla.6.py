matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
l = list()
m = 0

for p in range(0,3):
    for o in range(0,3):
        m += matriz[p][o]
              
print(m)