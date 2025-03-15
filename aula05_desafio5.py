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
    
        if (notas == []): 
            print('Lisa de Notas Vazia')
        else:
            print(f'A média é {(sum(notas) / len(notas)):.2f}')
    
def exe3() -> None:
    BANIDOS: list = ['pedro', 'josé', 'fernanda']

    if(BANIDOS.count(input('Qual Seu Nome ? ')) != 0 and (int(input('Qual Sua Idade ? ')) >= 18 or input('Está Acompanhado ? ')[0].lower() == 's')):
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
        
        if (len(senha) <= 6) and ((senha == '123456') or (senha == 'senha')):
            print('A Senha tem q ser maior q 6 caracteres e diferente de \'senha\' ou \'123456\' ')

        else:
            print('Cadastrado com Sucesso')
    else:
        print('O Nome tem que possuir mais de 3 caracters.')

def exe6() -> None:
    listaCompra: dict = {}
    cupom: str = input('Se tiver cupom digite o valor ou a porcentagem (use % no final) se não digite 0: ')


    while(True):
        listaCompra[input('Digite o Produto: ')] = float(input('Digite o Valor do Produto: '))

        if(int(input('Para cadastrar um item digite 1 se n 0: ')) == 0):
            break

    resultado: float = sum(listaCompra.values())

    if(sum(listaCompra.values()) >= 100 or len(listaCompra) >= 5):
        if(cupom.count('%') == 1):
            print(f"O valor é: {resultado * (1 - (float(cupom.removesuffix('%')) / 100)):.2f}")
        else:
            print(f"O valor é: {resultado - float(cupom):.2f}")
    else:
        print(resultado)

def exe7() -> None:
    idade: int = int(input('Qual a sua idade ? '))

    if(idade >= 18):
        print('Pode Viajar Sozinho')
    elif((idade < 18 and idade >= 17) and input('Está Autorizado ? <s/n> ')[0].lower() == 's'):
        print('Pode viajar autorizado pelos pais')
    else:
        print('Não pode viajar')

def exe8() -> None:
    if(int(input('Qual sua idade ? ')) >= 18 and input('Tem Carteir ? <s/n> ')[0].lower() == 's'):
        print('Pode Dirigir')
    else:
        print('Não Pode Dirigir')

def exe9() -> None:
    if(input('Digite o Usuário: ') == 'admin' and input('Digite a Senha: ') == '1234'):
        print('Login válido')
    else:
        print('Login Inválido')

def exe10() -> None:
    num: float = float(input('digite um número: '))

    if(num != 0):
        if((num % 2 == 0) and num > 0):
            print('O número é par e positivo')
        elif((num % 2 == 0) and num < 0):
            print('O número é par e negativo')
        elif((num % 2 != 0) and num > 0):
            print('O número é impar e positivo')
        else:
            print('O número é impar e negativo')

    else:
        print('O Número é zero')

def exe11() -> None:
    exe6()

def exe12() -> None:
    ano: int = int(input('Digite o ano: '))

    if((ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)):
        print('O ano é bissexto')
    else:
        print('O ano n e bissexto')

def exe13() -> None:
    idade: int = int(input('Digite a Idade: '))

    if(idade >= 18 or ((idade == 17 or idade == 16) and input('Está Acompanhado ? <s/n>')[0].lower() == 's')):
        print('Pode entrar')
    else:
        print('Não pode entrar')

def exe14() -> None:
    listaUsu: list = ['pedro', 'fabio']
    listaIp: list = ['1','2','3']

    if(listaIp.count(input('Digite o Ip: ')) != 0 or listaUsu.count(input('Digite o Usuário: '))):
        print('Não está Autorizado')
    else:
        print('Está Autorizado')

def exe15() -> None:
    l1: float = float(input('Lado 1: '))
    l2: float = float(input('Lado 2: '))
    l3: float = float(input('Lado 3: '))

    if(l1 == l2 and l2 == l3):
        print('Equilátero')
    elif(l1 == l2 or l2 == l3):
        print('Isósceles')
    else:
        print('Escaleno')
        
def exe16() -> None:
    if(int(input('Idade ? ')) >= 21 and float(input('Qual sua Renda ? ')) >= 2000 and input('Nome Sujo ? <s/n> ')[0].lower() == 'n'):
        print('Pode Empréstimo')
    else:
        print('Não Pode Empréstimo')

def exe17() -> None:
    temp: float = float(input('Qual a Temperatura ? '))

    if(temp > 30):
        print('Clima Quente')
    elif(temp <= 30 and temp >= 10):
        print('Clima Agradável')
    else:
        print('Não está Agradável')

def exe18() -> None:
    print(max([float(input('Num 1: ')), float(input('Num 2: ')), float(input('Num 3: '))]))

def exe19() -> None:
    idade: int = int(input('Idade: '))

    if(idade >= 18 and idade < 70):
        print('Voto Obrigatório')
    elif(idade < 16):
        print('Voto Proibido')
    else:
        print('Voto Opcional')
