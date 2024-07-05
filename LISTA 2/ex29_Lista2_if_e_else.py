print("quantos anos de trabalho")
idade = int(input("Qual a sua idade ?: "))
anosd = int(input("Quanto tempo você trabalhou ?: "))
if idade >= 65:
    print("Você pode se aposentar")
elif anosd >= 30:
    print("Você pode se aposentar")
elif idade >= 60 and anosd >= 25:
    print("Você pode se aposentar")
else:
    print("Você não pode se aposentar")