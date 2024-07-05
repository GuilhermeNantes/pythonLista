s_h = float(input("Digite o salario ganho por hora. "))
h_t = int(input("Digite a quantidade de horas que trabalhou esse mes: "))

s_b = s_h*h_t

imposto = (s_b*0.11)
inss = s_b*0.08
s = s_b*0.05

s_l = s_b - imposto -inss -s

print(f"Salário Bruto R${s_b:.2f}")
print(f"Imposto de Renda R${imposto:.2f}")
print(f"INSS R${inss:.2f}")
print(f"Sindicato R${s:.2f}")
print(f"Salário Liquido R${s_l:.2f}")