
nome = input("Digite o nome do vendedor: ")
sal_fixo = float(input("Digite o seu salário base: R$ "))
vendas_mês = float(input("Digite o valor vendido no mês: R$ "))
comissao = float(input("Digite o valor da comissão: "))

sal_final = sal_fixo + (vendas_mês * comissao)

print(f"O valor final à receber por {nome} será de: R$ {sal_final:.2f}")



