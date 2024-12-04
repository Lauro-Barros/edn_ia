def fibonacci(n):
    a, b = 0 , 1  
    resultado = [a]

    
    for _ in range(1, n):
        resultado.append(b)
    a, b = b, a + b
    print(f"Resultado sem tratamento: {resultado}")
    return resultado

    
    """ (Linhas 1, 2 e 3)
     1. **for _ in range(n):** Esse loop `for` irá executar o bloco de código interno `n` vezes. 
     O caractere `_` é usado como uma variável temporária que não será usada dentro do loop. 
     É uma convenção comum em Python para indicar que a variável do loop não importa.

     2. **print(x, end=" "):** Este comando `print` exibe o valor de `x` na tela, 
     seguido de um espaço (`end=" "`). O parâmetro `end` especifica o que será impresso no final do valor, 
     substituindo a quebra de linha padrão por um espaço.

     3. **x, y = y, x + y:** Esta linha faz a troca dos valores de `x` e `y`. `x` recebe o valor de `y`, e `y`
     recebe a soma dos valores antigos de `x` e `y`. Isso é essencial para gerar a sequência de Fibonacci,
     onde cada número é a soma dos dois números anteriores.
    """
    
    
    """ (Linhas 6, 7, 8, 9 e 10)
    1. **for _ in range(1, n):** Esse loop `for` começa em `1` e vai até `n-1` (o valor de `n` não é incluído no loop).
    Novamente, o caractere `_` é usado como uma variável temporária que não será utilizada dentro do loop.

    2. **resultado.append(b):** Dentro do loop, este comando adiciona o valor de `b` à lista `resultado`. `append` é 
    um método de lista que adiciona um item ao final da lista.

    3. **a, b = b, a + b:** Esta linha de código, fora do loop, atualiza os valores de `a` e `b`. `a` 
    recebe o valor de `b`, e `b` recebe a soma dos valores antigos de `a` e `b`. Esta atualização é fundamental 
    para gerar a sequência de Fibonacci, onde cada número é a soma dos dois números anteriores.
    """

def main():
    try:
        N = int(input())

        if N <= 0 or N >= 46:
            raise ValueError("O nº precisa estar ente 1 e 45")
        
        fibonacci_seq = fibonacci(N)

        print(" ".join(map(str, fibonacci_seq)))


    except ValueError as ve:
        print(f"Erro {ve}")

if __name__ == "__name__":
    main()

    # """ (Linha 40 em diante)
    # 1. **def main():** Define uma função chamada `main`.
    # 2. **try:** Inicia um bloco `try` para capturar exceções que possam ocorrer no código.
    # 3. **N = int(input()):** Solicita um número ao usuário, lê a entrada do usuário como string,
    # e a converte para um número inteiro.
    # 4. **if N <= 0 or N >= 46:** Verifica se o número `N` está fora do intervalo permitido 
    # (menor ou igual a 0, ou maior ou igual a 46).
    # 5. **raise ValueError("O nº precisa estar ente 1 e 45"):** Levanta uma exceção `ValueError` com uma 
    # mensagem personalizada se `N` não estiver no intervalo permitido.
    # 6. **fibonacci_seq = fibonacci(N):** Chama a função `fibonacci` (não definida aqui, mas presumivelmente 
    # definida em outro lugar do código) para gerar a sequência de Fibonacci com `N` termos.
    # 7. **print(" ".join(map(str, fibonacci_seq))):**
    # Converte os números na sequência de Fibonacci para strings, junta-os em uma única string com espaços 
    # entre os números, e imprime a string resultante.
    # 8. **except ValueError as ve:** Captura a exceção `ValueError` se ela for levantada no bloco `try`.
    # 9. **print(f"Erro {ve}"):** Imprime a mensagem de erro capturada.
    # 10. **if __name__ == "__main__": ** Verifica se o script está sendo executado diretamente (não importado como 
    # um módulo). Se for o caso, chama a função `main`.
    # """
