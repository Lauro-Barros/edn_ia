# classificando de acordo da idade

idade = int(input("Digite uma idade: "))

if idade >= 18:
    print("Você já é adulto")
elif 12 <= idade < 18 :
    print("Você já é adolescente")
else:
    print("Parabéns, você é uma criança!!")
