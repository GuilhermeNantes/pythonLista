sala = input("digite seu salario")
if sala > 0 and sala <= 500:
    c = (sala + 0) / 0.25
    print(c)
elif sala > 500 and sala <= 1000:
    h = (sala + 100) / 0.20
    print(h)
elif sala > 1000 and sala <= 2000:
    y = (sala + 200) / 0.15
    print(y)
else:
    v = sala + 500
    print(v)