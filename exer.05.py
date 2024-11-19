
matricula = int(input("Digite a matricula do colaborador: "))
h_trabalhadas = int(input("Digite quantas horas trabalhadas: "))
vl_hora = float(input("Digite o valor que o colaborador recebe por hora: "))

salario = h_trabalhadas * vl_hora

print(f"NUMBER = {matricula}")
print(f"SALARY = {salario:.2f}")
