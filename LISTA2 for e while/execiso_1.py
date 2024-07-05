ls1 = []
while True:
    num = int(input("digite numeiro"))
    if(num <= 0):
           break
    ls1.append(num)
print(f"o maior: {max(ls1)} e o menor: {min(ls1)}")