# Preciso colocar todos os valores juntos, numa variável só, então usa-se a função ".split," 
# que é um separador de variáveis. Toda função de ve vir acompanhada de ()
cod1, qtdade1, vlr1 = (input("Digite o código, quantidade e valor da peça1: ")).split()
cod2, qtdade2, vlr2 = (input("Digite o código, quantidade e valor da peça2: ")).split()

"""preciso colocar 2 valores inteiros e 1 com 2 casas decimais. Pra isso preciso especificar o 
que cada uma delas é, e não preciso especificar o tipo de variável do código pois ele não é 
pedido no retorno do código"""

qtdade1, vlr1 = int(qtdade1), float(vlr1)
qtdade2, vlr2 = int(qtdade2), float(vlr2)

total = (qtdade1 * vlr1) + (qtdade2 * vlr2)

print(f"VALOR A PAGAR PELAS PEÇAS SERÁ DE: R$ {total:.2f} ") 

# o "f" simboliza que existe uma variável dentro da String
