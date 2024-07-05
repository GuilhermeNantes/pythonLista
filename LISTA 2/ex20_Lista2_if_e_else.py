nota1 = float(input('digite seu nota'))
nota2 = float(input('digite seu nota'))
nota3 = float(input('digite seu nota'))
print('=' * 35)
nota3 = nota3 * 2
boletin = nota1,nota2,nota3
if nota3 <= 60:
    print(nota3)
else:
    print('nota invalida')
if nota2 <= 25:
    print(nota2)
else:
    print('nota invalida')
if nota1 <= 25:
    print(nota1)
else:
    print('nota invalida')

if boletin >= 60:
    print("aprovado")
else:
    print("reprovado")