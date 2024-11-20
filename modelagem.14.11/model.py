from sklearn.linear_model import LinearRegression

import numpy as np

# 'h_estudo' é a atribuição para transformar 
#  esse array numa matriz
h_estudo = np.array([1,2,3,4,5]).reshape(-1,1) # valor referência
notas = np.array([40,50,60,70,80])

# com essas duas linhas estamos dizendo para 
# o modelo: usa isso pra aprender

modelo = LinearRegression()
modelo.fit(h_estudo, notas) # o modelo está treinando

horas = float(input("Digite o nº de horas estudadas: "))

# previsão # os 2 [] colocam nossa matriz em duas dimensões
nota_prev = modelo.predict([[horas]]) 

print(f"Com {horas} de estudo, a nota prevista será: {nota_prev[0]:.2f}") 

