# Preciso colocar todos os valores juntos, numa variável só, então usa-se a função ".split," 
# que é um separador de variáveis. Toda função de ve vir acompanhada de ()
# fórmula Distância: sqrt ((x2 - x1)**2 + (y2 - y1)**2))

import math

# x1, y1 = (input("Digite os pontos 01: ")).split()
# x2, y2 = (input("Digite os pontos 02: ")).split()

x1, y1 = map(float, input("Digite as coordenadas de x1 e x2: ")).split()
x2, y2 = map(float, input("Digite as coordenadas de y1 e y2: ")).split()

# x1, x2, y1, y2 = float(x1), float(x2), float(y1), float(y2)

Dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Dist = (((x2 - x1)**2 + (y2 - y1)**2))**0.5 - Tbm funciona

print(f"A distância entre os pontos é de: {Dist:.4f} ") 

# o "f" simboliza que existe uma variável dentro da String
