try:
    num1 = int(input("Digite o 1º número: "))
    num2 = int(input("Digite o 2º número: "))
    resultado = num1 / num2
    print(f"O resultado é: {resultado}")
except ZeroDivisionError: 
    print("Tá errado, divisão por zero impossível")
except ValueError:
    print("Tá doido rapaz!! Operação não permitida")