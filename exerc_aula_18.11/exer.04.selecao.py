
# Se B > C e D > A e C + D > A + B e C,D > 0,
# com A for par, escreva valores aceitos

A, B, C, D = map(int, input().split())

if (B > C) and (D > A) and (C + D) > (A + B) and C > 0 and D > 0 and A % 2 ==0:
    print("Valores aceitos")
else:
    print("Valores não aceitos")