import random

def main():
# Valor é um nº randômico inteiro entre 1 e 10000, num looping de alcance de 100 números
    valor = [random.randint(1, 10000) for _ in range(100)]

# Aqui ele vai gerar o maior valor dos números randômicos
    maior = (max(valor))
    posicao = valor.index(maior)

    resultado = {
      "Números": valor,
      "Maior Valor": maior,
      "Posição": posicao
    }

    print("\nNúmeros gerados:")
    print(valor)
    print("\n Maior valor",maior)
    print("Posição do maior valor",posicao)

if __name__ == "__main__": 
    main()