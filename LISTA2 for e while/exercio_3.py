def ltxt(mes):
    print("-=" * 30)
    print(mes)
    print("-=" * 30)
def l():
    print("-="*30)


d = list()
p = []
## codigo principal
ltxt("              OI MEU EXERCIÇO ")
for i in range(5):
    p.append(int(input("digite um numeiro: ")))
    
l()
for i in range(len(p)):
    d.append((f"{p[i]} +"))
print(f" {d} = {sum(p)}")
    