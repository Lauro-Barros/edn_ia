import math #Cálculo da área do círculo = pi * R²

raio = float(input("Digite o valor do raio: "))

area = math.pi * (raio ** 2) 
""" # O valor deve apresentar 4 casas decimais no máximo no resultado"""

   
print (f"A área do círculo com raio {raio} é {area:.4f}")
 