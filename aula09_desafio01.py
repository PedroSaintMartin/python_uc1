from random import randint

class Desafio09:
    def __init__(self, opcao: int = 1):
        self.opcao = opcao

    def somaElementos(self) -> int:
        return sum([int(input("Digite um Número: ")) for i in range(5)])

    def numerosImparesIntervalo(self) -> list:
        return [(i + 1) for i in range(50) if (i + 1) % 2 != 0]

    def insercaoOrdenada(self) -> list:
        return sorted([int(input("Digite um número: ")) for i in range(5)])

    def contagemOcorrencias(self, opcao: int = 1) -> int:
        return [randint(1, 5) for i in range(10)].count(opcao)

    def getOpcao(self) -> int:
        return self.opcao
    def setOpcao(self, opcao) -> None:
        self.opcao = opcao


if __name__ == "__main__":
    obj: Desafio09 = Desafio09()

    #print(obj.insercaoOrdenada())
    print(obj.contagemOcorrencias())
