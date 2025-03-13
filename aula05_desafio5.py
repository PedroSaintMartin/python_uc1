from random import randint

def exe1() -> None:
    SENHA_BANCO: str = 'senha'

    if(float(input('Qual Sua Idade ? ')) >= 18 and input('Qual a Senha ? ') == SENHA_BANCO):
        print('Acesso Permitido')
    else:
        print('Acesso Negado')

def exe2() -> None:
    notas: list = []

    while(True):
        temp: float = float(input('Digite Uma Nota, Se n Tiver Mais Notas Digite Uma Número Inválido (Maior q 10 ou Menor q 0): '))

        if(temp >= 0 and temp <= 10):
            notas.append(temp)
            print(notas)
        else:
            break
    
    (print('Lisa de Notas Vazia')) if (notas == []) else print(f'A média é {(sum(notas) / len(notas)):.2f}')
    
def exe3() -> None:
    BANIDOS: list = ['pedro', 'josé', 'fernanda']

    nome: str = input('Qual Seu Nome ? ')
    idade: int = int(input('Qual Sua Idade ? '))
    isAcompanhado: bool = bool(input('Está Acompanhado ? '))

    if(BANIDOS.count(nome) != 0 and (idade >= 18 or isAcompanhado == True)):
        print('Não Pode Entrar')
    else:
        print('Pode Entrar')

def exe4() -> None:
    num: int = randint(1, 10)
    print(num)

    for i in range(3):
        if(int(input('Digite um Número. ')) == num):
            print('Você Ganhou !')
            break
        
        if(i == 2):
            print('Você Perdeu')
            break
        
        print('Tente Novamente')

def exe5() -> None:
    nome: str = input('Digite Seu Nome. ')

    if(len(nome) >= 3):
        senha: str = input('Digite sua Senha. ')
        print(type(senha))
        if (len(senha) <= 6) and ((senha == '123456') or (senha == 'senha')):
            print('A Senha tem q ser maior q 6 caracteres e diferente de \'senha\' ou \'123456\' ')

        else:
            print('Cadastrado com Sucesso')
    else:
        print('O Nome tem que possuir mais de 3 caracters.')

'''
def exe6() -> None:
def exe7() -> None:
def exe8() -> None:
def exe9() -> None:
def exe10() -> None:
def exe11() -> None:
def exe12() -> None:
def exe13() -> None:
def exe14() -> None:
def exe15() -> None:
def exe16() -> None:
def exe17() -> None:
def exe18() -> None:
def exe19() -> None:
def exe20() -> None:
'''

exe3()
