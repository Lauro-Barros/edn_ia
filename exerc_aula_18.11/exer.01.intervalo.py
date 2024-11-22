"""
Qual o valor entre [0,25], [25,50], [50,75] ou [75,100]
Preciso incluir os números do intervalo com 2 casas decimais
"""
# if elif else (se, senão, então)
# round faz arredondamento

numero = round(float(input("Digite um Nº com 2 casas decimais: ")),2)

if 0 <= numero <= 25:
    print("Ele se encontra no intervalo: [0, 25]")
elif 25 < numero <=50:
    print("Ele se enontra no intervalo: [25, 50]")
elif 50 < numero <=75:
    print("Ele se enontra no intervalo: [50, 75]")
elif 75 < numero <=100:
    print("O nº se encontra no intervalo: [75, 100]")
else:
    print("O nº está fora de qualquer intervalo")