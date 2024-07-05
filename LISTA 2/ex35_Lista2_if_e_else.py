m = int(input("digite o quantidade: "))
if  m >= 100000:
    c = (m + 700)/0.16
    print(c)
elif m <= 100000 and m >= 80000:
    g = (m + 650)/0.14
    print(g)
elif m <= 80000 and m >= 60000:
    h = (m + 600)/0.14
    print(h)
elif m <= 60000 and m >= 40000:
    j = (m + 550)/0.14
    print(j)
else:
    k = (m + 500)/0.14
    print(k)