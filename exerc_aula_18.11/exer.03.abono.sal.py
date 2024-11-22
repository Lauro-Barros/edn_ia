
salario = float(input("Digite o valor do salário base: R$ "))

if  salario <= 400.00:
    percentual = 15
elif salario <= 800.00:
    percentual = 12
elif salario <= 1200.00:
    percentual = 10
elif salario <= 2000.00:
    percentual = 7
else:
    percentual = 4

reajuste = salario * (percentual/100)
sal_novo = salario + reajuste


print(f"Novo Salário: R$ {sal_novo:.2f}")
print(f"Reajuste ganho: R$ {reajuste:.2f}")
print(f"Valor do percentual foi de: {percentual}%")






