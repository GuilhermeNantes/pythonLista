print("        EXERCIO: Matriz. ex 9 ")
matriz = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]]
c = o = 0

for i in range(len(matriz)):  
    for p in range(len(matriz[0])):        
        if (i,p) == (c,o):
             print(f"     ({i},{p}) = ({c},{o}) iquais") 
             matriz[c][o] = 1 
             c += 1 
             o += 1          
        else:
            if (i,p) != (c,o):
                print(f"     ({i},{p}) é ({c},{o}) diferente")
for p in matriz:
    print(f"        {p}")
