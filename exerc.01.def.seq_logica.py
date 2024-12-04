"""
O que está sendo passado unicialmente é um nº Inteiro 
Natural.
Então se apaga a fção (N = int(input())) pois não precisa 
colocar pois só é preciso colocar na info da fção (n)
Qdo estiver sublinhado de vermelho, é problema de identação,
seleciona-se a pte que quiser identar e aperta o TAB
"""
def seq_logica(n):

    """
    1ª função, imprime a sequencia para o nº inteiro
    """
# N = int(input())
    for i in range(1,n + 1):
        print(i, i**2, i**3)
        print(i, i**2 + 1, i**3 + 1)

def main():
    try:
        entrada = input("Digite a qtdade de testes: ")

        if not entrada.isdigit():
            raise ValueError("Insira um nº positivo!")


        N = int(entrada)
        
        if N < 1 or N >= 1000:
            raise ValueError("Onº deve estar entre 1 e 1000")
        seq_logica(N)
    except ValueError as ve:
        print(f"erro: {ve}")

if __name__ == "__main__":
    main()