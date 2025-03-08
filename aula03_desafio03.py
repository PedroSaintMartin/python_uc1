import math as m

def calculadoraBasica() -> None:
    x = float(input("Digite o valor do Primeiro Número: "))
    y = float(input("Digite o valor do Primeiro Número: "))

    print(f"O Resultado da Soma é: {(x + y):.2f}")
    print(f"O Resultado da Subtração é: {(x - y):.2f}")
    print(f"O Resultado da Multiplicação é: {(x * y):.2f}")
    print(f"O Resultado da Divisão é: {(x / y):.2f}")
    
def mediaNotas() -> None:
    media: float = (
        (float(input("Qual Valor do Primeiro Número ? ")) + 
        float(input("Qual Valor do Segundo Valor ? ")) +
        float(input("Qual Valor do Terceiro Valor ? ")))/ 3)
    
    print(f"A Média é: {media:.2f}")

def conversorTemperatura() -> None:
    conv: float = float(input("Qual temperatura em C: ")) * 9/5 + 32

    print(f"O Valor da Conversão é: {conv:.2f} F")

def areaCirculo() -> None:
    raio: float = float(input("Qual o Raio ? "))

    print(f"A área do circulo é: {(raio ** 2 * m.pi):.2f} u².m")

def calculadoraImc() -> None:
    peso: float = float(input("Qual o Peso em (Kg) ? "))
    altura: float = float(input("Qual a Altura em (M) ? "))

    print(f"O IMC é: {(peso / altura ** 2):.2f} kg/m²")

def descontoCompras() -> None:
    compra: float = float(input("Qual Total da Compra ? "))

    print(f"A compra com desconto é: R$ {(compra * 0.9):.2f}")

def tempoViagem() -> None:
    distancia: float = float(input("Qual a distâcia ? "))
    velocidade: float = float(input("Qual a Velocidade Média ? "))

    print(f"A duração da viagem é: {(distancia/velocidade):.2f} s")

def jurosSimples() -> None:
    capital: float = float(input("Capital inicial ? "))
    taxa: float = float(input("Taxa de juros ? ")) 
    tempo: float = float(input("Tempo do Investimento ? "))

    print(f"O Valor é: R$ {(capital * (1 + (taxa/100)) * tempo):.2f}")

def bhaskara() -> None:
    a: float = float(input("Digite o valor de A: "))
    b: float = float(input("Digite o valor de B: "))
    c: float = float(input("Digite o valor de C: "))

    delta = (m.pow(b, 2) - 4*a*c)

    print(delta)

    if delta < 0:
        print("Não existe resultado no conjunto dos numeros reais")
    else:
        print(f"O Valor da Primeira Raiz: {((-b + m.sqrt(delta)) / 2 * a):.2f}")
        print(f"O Valor da Segunda Raiz: {((-b - m.sqrt(delta)) / 2 * a):.2f}")

def conversorMoedas() -> None:
    cotacao: float = float(input("Qual a cotação do dólar ? "))
    valor: float = float(input("Qual o Montante de Conversão ? "))

    print(f"O Valor Convertido é: R$ {(valor * cotacao):.2f}")
