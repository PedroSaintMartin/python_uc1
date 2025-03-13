def exec1() -> None:
    num: float = float(input('Insira um número ! '))
    if(num == 0):
        print('O Número é Zero. ')
    elif(num > 0):
        print('O Número é Positivo.')
    else:
        print('O Número é Negativo.')

def exec2() -> None:
    if(int(input('Digite sua Idade ? ')) >= 16):
        print('Pode Votar.')
    else:
        print('Não Pode Votar.')

def exec3() -> None:
    num1: float = float(input('Digite Primeiro Número. '))
    num2: float = float(input('Digite Segundo Número. '))

    if num1 > num2:
        print(f'{num1:.2f}')
    else:
        print(f'{num2:.2f}')

def exec4() -> None:
    if(float(input('Digite um Número ! ')) % 2 == 0):
        print('O Número é Par.')
    else:
        print('O Número é Ímpar.')

def exec5() -> None:
    if(input('Digite o Usuário. ') == 'admin' and input('Digite a Senha. ') == '1234'):
        print('Acesso Permitido')
    else:
        print('Acesso Negado')

def exec6() -> None:
    num: float = float(input('Digite um Número. '))

    if(num >= 10 and num <= 50):
        print('O Número Está Entre 10 e 50')
    else:
        print('O Número não Está Entre 10 e 50')

def exec7() -> None:
    imc: float = float(input('Qual seu peso ? ')) / float(input('Qual sua Altura ? ')) ** 2

    if(imc <= 18.5):
        print('Abaixo do Peso')
    elif(imc > 18.5 and imc <= 24.9):
        print('Peso Ideal')
    elif(imc > 24.9 and imc <= 29.9):
        print('Sobrepeso')
    elif(imc > 29.9):
        print('Obesidade')

def exec8() -> None:
    l1: float = float(input('Digite o Primeiro Número. '))
    l2: float = float(input('Digite o Segundo Número. '))
    l3: float = float(input('Digite o Terceiro Número. '))

    if(((l1 + l2) > l3) and ((l2 + l3) > l1) and ((l3 + l1) > l2)):
        print('É um triângulo')
    else:
        print('Não é um Triângulo')

def exec9() -> None:
    temp: float = float(input('Qual a Temperatura ? '))

    if(temp <= 0):
        print('Muito Frio !')
    elif(temp > 0 and temp <= 20):
        print('Clima Agradável !')
    else:
        print('Calorão !')

def exec10() -> None:
    compra: float = float(input('Qual o Valor da Compra ? '))

    if(compra >= 500):
        print(compra * (1 - (15/100)))
    elif(compra < 500 and compra >= 200):
        print(compra * (1 - (10/100)))
    else:
        print(compra * (1 - (5/100)))
