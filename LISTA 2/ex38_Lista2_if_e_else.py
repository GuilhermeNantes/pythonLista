ps = float(input("Digite seu peso: "))
h = float(input("Digite sua altura: "))

flf = ps/(h*h)

if flf < 18.5:
    print("Abaixo do peso ideal!")
elif flf >= 18.6 and flf <= 24.9:
    print("Saudavel!")
elif flf >= 25.0 and flf <= 29.9:
    print("Peso em excesso!")
elif flf >= 30.0 and flf <= 34.9:
   print("Obesidade Grau (D)")
elif flf >= 35.0 and flf <= 39.9:
     print("Obesidade Grau (S)")
else:
    print("Obesidade(SSSS+) ")
