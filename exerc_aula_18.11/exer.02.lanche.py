
item, qtdade = map(int, input("Informe o nº do item e a Qtdade a ser comprada por favor: ").split())
preços = {1: 4.00,
          2: 4.50,
          3: 5.00,
          4: 2.00,
          5: 1.50
        }
   
total = preços[item] * qtdade
print(f"O valor total da sua compra será de: R$ {total:.2f}")



