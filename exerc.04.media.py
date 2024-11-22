N1, N2, N3, N4 = map(float, input().split())
p1, p2, p3, p4 = map(float, input().split())

media = (((N1*p1) + (N2*p2) + (N3*p3) + (N4*p4))/((p1+p2+p3+p4)))

if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
elif 5.0 <= media <= 6.9:
    print("Aluno em exame.")
    print(f"Nota do exame: {media}")
elif 5.0 <= media <= 6.9:
    print("")

# media2 = (5.0 <= media <= 6.9 + (media/2))
# print(f"Média: {media:.1f}")





#     print(f"Nota do exame:{media:.1f}")
# else:
#     print("Presentation Error")

# if 5.0 <= media <= 6.9:
#     print(f"sua nova nota é: {media2:.1f}")
