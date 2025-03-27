class Aula09:
    vetor: list = []

    def __init__(self, vetor: list = None) -> None:
        self.vetor: list = vetor

    def imprimirLista(self, v: list) -> None:
        print("Vetor:", v)

    def interarLista(self, v: list) -> None:
        for i in v:
            print(i)

    def somaVetor(self, v: list) -> None:
        print(f"Soma de todos os elementos do vetor: {sum(v)}")

    def inverteElementosVetor(self, v: list) -> None:
        print(v[::-1])

    def multiply2vet(self, v: list) -> None:
        print([i * 2 for i in v])

    def countVal3(self, v: list) -> None:
        print(v.count(3))

    def ordemVetor(self, v: list) -> None:
        print(sorted(v))

    def setVetor(self, vetor) -> None:
        self.vetor = vetor
    
    def getVetor(self) -> list:
        return self.vetor

if __name__ == "__main__":
    x = [10, 20, 30, 40, 50]
    a: Aula09 = Aula09(x)
    
    a.imprimirLista(a.getVetor())
    a.interarLista(a.getVetor())
    a.somaVetor(a.getVetor())
    a.inverteElementosVetor(a.getVetor())
    a.multiply2vet(a.getVetor())
    a.countVal3(a.getVetor())
    a.ordemVetor(a.getVetor())
