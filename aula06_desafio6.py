import math as m

def exe1() -> None:
    for i in range(10):
        print(i + 1)

def exe2() -> None:
    for i in range(10):
        print((i + 1) ** 2)

def exe3() -> None:
    for i in range(20):
        if((i + 1) % 2 == 0):
            print(f"O Número {i + 1} é par")
        else:
            print(f"O Número {i + 1} é impar")

def exe4() -> None:
    i: int = 10

    while(True):
        if(i != 0):
            print(i)
            i -= 1
        else:
            break

def exe5() -> None:
    var: str = ""
    while(var.lower() != 'sair'):
        var: str = input()
        
def exe6() -> None:
    sum: int = 0

    for i in range(100):
        sum += i 
        print(sum)

def exe7() -> None:
    fatorial: int = int(input())
    result: int = 1

    while(fatorial != 1):
        result *= fatorial
        fatorial -= 1
    
    print(result)

def exe8() -> None:
    result: float = 0

    while(True):
        num: float = float(input('Digite um número: '))

        if(num < 0):
            break
        else:
            result += num
    
    print(result)

def exe9() -> None:
    num: int = int(input('Digite um número: '))

    for i in range(10):
        print(f"{i + 1} x { num } = { (i + 1) * num }")

def exe10() -> None:
    while(True):
        senha: str = input('Digite sua senha: ')
        
        if(senha == 'SENHA'):
            break

def exe11() -> None:
    lista: list = ['Pedro', 'José', 'Fernanda']

    for i in lista:
        print(i)

def exe12() -> None:
    num: int = int(input('Digite um Número: '))
    result: int = 0

    for i in range(num):
        result = (i + 1) ** 3
    
    print(result)

def exe13() -> None:
    exe9()

def exe14() -> None:
    print(len(input('Digite um número: ')))

def exe15() -> None:
    for i in range(20):
        if((i + 1) % 3 == 0 and (i + 1) % 5 == 0):
            print(f"o número {(i + 1)} é multiplo de 3 e 5")
        elif((i + 1) % 3 == 0):
            print(f'o numero {(i + 1)} é multiplo de 3')
        elif((i + 1) % 5 == 0):
            print(f'o numero {(i + 1)} é multiplo de 5')

def exe16() -> None:
    for i in [0, 1, 2, 3, 4, 5]:
        for j in [0,1,2,3,4,5,6,7,8,9,10]:
            print(f"{i} x {j} = {i * j}")
