alunos = [("João", 8.0) , ("maria",9.5) , ("pedro",7.5) , ("ana",8.5)]
c = 0
v = 0

for i in alunos:
    if  i[1] > c:
        c = i[1]
        v = i
print(v)