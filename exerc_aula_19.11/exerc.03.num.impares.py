# Num. n para se inserir na tela
n = int(input()) # 7 casos de teste
# entre o valor x e o valor y
# some todos os ímpares entre x e y


for _ in range(n): # valor da variável _ (mantém o tipo e descarta a variável)
    x, y = map(int, input().split()) # Aqui na operação o 1º nº é inteiro e o 2º são 2 nº interiros separados
    if x > y:
        x, y = y, x

    # "i" é o índice, que são todos os itens da minha lista
    soma = sum( i for i in range(x + 1, y) if i % 2 != 0) 
    print(soma)

