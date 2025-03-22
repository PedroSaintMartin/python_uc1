import sys

def calculadoraSimples(a: float, b: float, c: chr) -> float:
    if(c == '+'):
        return a + b
    if(c == '-'):
        return a - b
    if(c == '*'):
        return a * b
    if(c == '/'):
        return a / b

def contadorPalavras(lista: tuple) -> int:
    return len(lista)

def palindromo(palavra: str) -> None:
    if(palavra == palavra[::-1]):
        print("É Palindromo")
    else:
        print("Não é Palindromo")

def seqFibo(i: int) -> None:
    lista: list = [0, 1]
    
    for j in range(i - 2):
        lista.append(lista[j] + lista[j + 1])
    
    print(lista)

def conversorTemperatura(temp: int) -> float:
        return temp * 1.8 + 32
    
def main(a: tuple):
    #print(f"O Resultado é: {calculadoraSimples(float(a[0]), float(a[1]), a[2]):.2f}")
    #print(f"A Quantidade de palavras é {contadorPalavras(a)}")
    #palindromo(a[0])
    #seqFibo(int(a[0]))
    conversorTemperatura()

if __name__ == "__main__":
    main(sys.argv[1::])
