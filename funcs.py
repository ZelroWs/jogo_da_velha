import random 
from gen import *



def jogo(lugar, valor, dicjogo, jogador_agr, jogador_dps):
    dicjogo = dicjogo
    valor = valor
    jogador_agr = jogador_agr
    jogador_dps = jogador_dps
    
    if lugar == 'a1':
        dicjogo['a1'] = valor
    elif lugar == 'a2':
        dicjogo['a2'] = valor
    elif lugar == 'a3':
        dicjogo['a3'] = valor
    elif lugar == 'b1':
        dicjogo['b1'] = valor
    elif lugar == 'b2':
        dicjogo['b2'] = valor
    elif lugar == 'b3':
        dicjogo['b3'] = valor
    elif lugar == 'c1':
        dicjogo['c1'] = valor
    elif lugar == 'c2':
        dicjogo['c2'] = valor
    elif lugar == 'c3':
        dicjogo['c3'] = valor
    else:
        print('Essa casa não existe')
        if valor == 'o':
            valor = 'x'
        elif valor == 'x':
            valor = 'o'
        jogopergunta(dicjogo, valor, dicp)
        
    print(dicjogo['a1'],'|', dicjogo['b1'],'|', dicjogo['c1'], '     a1|b1|c1' )
    print('---------     ---------')
    print(dicjogo['a2'],'|', dicjogo['b2'],'|', dicjogo['c2'], '     a2|b2|c2' )
    print('---------     ---------')
    print(dicjogo['a3'],'|', dicjogo['b3'],'|', dicjogo['c3'], '     a3|b3|c3' )
    jogoanalise(dicjogo, valor, jogador_agr, jogador_dps)


def jogoanalise(dicjogo, valor, jogador_agr, jogador_dps):
    dicjogo = dicjogo
    valor = valor
    jogador_agr = jogador_agr
    jogador_dps = jogador_dps
    if dicjogo['a1'] != ' ': 
        if dicjogo['a2'] != ' ': 
            if dicjogo['a3'] != ' ': 
                if dicjogo['b1'] != ' ':
                    if dicjogo['b2'] != ' ':
                        if dicjogo['b3'] != ' ':
                            if dicjogo['c1'] != ' ':
                                if dicjogo['c2'] != ' ':
                                    if dicjogo['c3'] != ' ':
                                        print('Fim de jogo!')
                                        print('Velha!!')
                                        continuar = input('Deseja jogar novamente? ')
                                        finalizar(continuar)
    if dicjogo['a1'] == dicjogo['a2'] and ['a2'] == ['a3'] and ['a1'] != ' ':
        print('Fim de jogo!')
        print(f'{jogador_agr} venceu!!')
        continuar = input('Deseja jogar novamente? ')
        finalizar(continuar)

    elif dicjogo['b1'] == dicjogo['b2'] and dicjogo['b2'] == dicjogo['b3'] and dicjogo['b1'] != ' ':
        print('Fim de jogo!')
        print(f'{jogador_agr} venceu!!')
        continuar = input('Deseja jogar novamente? ')
        finalizar(continuar)
    elif dicjogo['c1'] == dicjogo['c2'] and dicjogo['c2'] == dicjogo['c3'] and dicjogo['c1'] != ' ':
        print('Fim de jogo!')
        print(f'{jogador_agr} venceu!!')
        continuar = input('Deseja jogar novamente? ')
        finalizar(continuar)
    elif dicjogo['a1'] == dicjogo['b1'] and dicjogo['b1'] == dicjogo['c1'] and dicjogo['a1'] != ' ':
        print('Fim de jogo!')
        print(f'{jogador_agr} venceu!!')
        continuar = input('Deseja jogar novamente? ')
        finalizar(continuar)
    elif dicjogo['a2'] == dicjogo['b2'] and dicjogo['b2'] == dicjogo['c2'] and dicjogo['a2'] != ' ':
        print('Fim de jogo!')
        print(f'{jogador_agr} venceu!!')
        continuar = input('Deseja jogar novamente? ')
        finalizar(continuar)
    elif dicjogo['a3'] == dicjogo['b3'] and dicjogo['b3'] == dicjogo['c3'] and dicjogo['a3'] != ' ':
        print('Fim de jogo!')
        print(f'{jogador_agr} venceu!!')
        continuar = input('Deseja jogar novamente? ')
        finalizar(continuar)
    elif dicjogo['a3'] == dicjogo['b2'] and dicjogo['b2'] == dicjogo['c1'] and dicjogo['a3'] != ' ':
        print('Fim de jogo!')
        print(f'{jogador_agr} venceu!!')
        continuar = input('Deseja jogar novamente? ')
        finalizar(continuar)
    elif dicjogo['a1'] == dicjogo['b2'] and dicjogo['b2'] == dicjogo['c3'] and dicjogo['a1'] != ' ':
        print('Fim de jogo!')
        print(f'{jogador_agr} venceu!!')
        continuar = input('Deseja jogar novamente? ')
        finalizar(continuar)
        
    else:
        jogopergunta(dicjogo, valor, jogador_agr, jogador_dps)                                       


def jogopergunta(dicjogo, valor, jogador_agr, jogador_dps):
    dicjogo = dicjogo
    jogador_agr, jogador_dps = jogador_dps, jogador_agr
    if valor == 'o':
        valor = 'x'
    elif valor == 'x':
        valor = 'o'
    else:
        valor = input('Valor invalido, digite (o ou x)')
        if valor != 'o' or valor != 'x':
            jogopergunta(dicjogo, valor, jogador_agr, jogador_dps)
    frase = gen(jogador_agr)
    print(frase)
    lugar = input('Casa desejada: ')
    valor = valor
    jogo(lugar, valor, dicjogo, jogador_agr, jogador_dps)

        

def começar():
    print('Jogo da velha do Kurtzinho.')
    input('COMEÇAR')
    modo = str(input('Digite 1 para pvp e 2 para pve:'))
    if modo != '1' and modo != '2':
        print(f'{modo} não é uma resposta valida.')
        começar()
    dicjogo = {'a1': ' ', 'a2' : ' ', 'a3' : ' ', 'b1' : ' ', 'b2' : ' ', 'b3': ' ', 'c1' : ' ', 'c2' : ' ', 'c3' : ' '}
    print(dicjogo['a1'],'|', dicjogo['b1'],'|', dicjogo['c1'], '     a1|b1|c1' )
    print('---------     ---------')
    print(dicjogo['a2'],'|', dicjogo['b2'],'|', dicjogo['c2'], '     a2|b2|c2' )
    print('---------     ---------')
    print(dicjogo['a3'],'|', dicjogo['b3'],'|', dicjogo['c3'], '     a3|b3|c3' )
    if modo == '1':
        jogador_agr = str(input('Nome do Jogador 1: '))
        jogador_dps = str(input('Nome do Jogador 2: '))
        frase = gen(jogador_agr)
        print(frase)
        lugar = input('Casa desejada: ')
        valor = input('x ou o: ')
        jogo(lugar, valor, dicjogo, jogador_agr, jogador_dps)
   
    elif modo == '2':
        jogador = str(input('Nome: '))
        print(f'Vez de {jogador}')
        print('Você é o x')
        valor = 'x'
        lugar = input('Casa desejada: ')
        jogomaquina(lugar, valor, dicjogo, jogador)
    
def finalizar(continuar):
    listas = ['s', 'sim', 'y', 'yes', '1']
    listan = ['n', 'não', 'nao', 'no', '0']
    if continuar in listas:
        começar()
    elif continuar in listan:
        input('Obrigado por jogar!!\
                Ass: Kurtzinho')
    else:
        print('Essa resposta não é valida.')
        continuar = input('Deseja jogar novamente? ')
        finalizar(continuar)








def maquina(dicjogo, valor):
    import random
    dicjogo = dicjogo
    valor = valor
    if valor == 'o':
        valor = 'x'
    elif valor == 'x':
        valor = 'o'
    listap =['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
    a1 = dicjogo.get('a1')
    a2 = dicjogo.get('a2')
    a3 = dicjogo.get('a3')
    b1 = dicjogo.get('b1')
    b2 = dicjogo.get('b2')
    b3 = dicjogo.get('b3')
    c1 = dicjogo.get('c1')
    c2 = dicjogo.get('c2')
    c3 = dicjogo.get('c3')
    if a1 != ' ':
        listap.remove('a1')
    if a2 != ' ':
        listap.remove('a2')
    if a3 != ' ':
        listap.remove('a3')
    if b1 != ' ':
        listap.remove('b1')
    if b2 != ' ':
        listap.remove('b2')
    if b3 != ' ':
        listap.remove('b3')
    if c1 != ' ':
        listap.remove('c1')
    if c2 != ' ':
        listap.remove('c2')
    if c3 != ' ':
        listap.remove('c3')

    lugar = random.choice(listap)
    jogopessoa(lugar, valor, dicjogo)


    
def jogomaquina(lugar, valor, dicjogo, jogador):
    dicjogo = dicjogo
    valor = valor
    jogador = jogador
    if lugar == 'a1':
        dicjogo['a1'] = valor
    elif lugar == 'a2':
        dicjogo['a2'] = valor
    elif lugar == 'a3':
        dicjogo['a3'] = valor
    elif lugar == 'b1':
        dicjogo['b1'] = valor
    elif lugar == 'b2':
        dicjogo['b2'] = valor
    elif lugar == 'b3':
        dicjogo['b3'] = valor
    elif lugar == 'c1':
        dicjogo['c1'] = valor
    elif lugar == 'c2':
        dicjogo['c2'] = valor
    elif lugar == 'c3':
        dicjogo['c3'] = valor
    else:
        print('Essa casa não existe')
        if valor == 'o':
            valor = 'x'
        elif valor == 'x':
            valor = 'o'
        jogoperguntapessoa(dicjogo, valor)
        
    print(dicjogo['a1'],'|', dicjogo['b1'],'|', dicjogo['c1'], '     a1|b1|c1' )
    print('---------     ---------')
    print(dicjogo['a2'],'|', dicjogo['b2'],'|', dicjogo['c2'], '     a2|b2|c2' )
    print('---------     ---------')
    print(dicjogo['a3'],'|', dicjogo['b3'],'|', dicjogo['c3'], '     a3|b3|c3' )
    jogoanalisemaquina(dicjogo, valor)

def jogoanalisemaquina(dicjogo, valor):
    dicjogo = dicjogo
    valor = valor
    if dicjogo['a1'] != ' ': 
        if dicjogo['a2'] != ' ': 
            if dicjogo['a3'] != ' ': 
                if dicjogo['b1'] != ' ':
                    if dicjogo['b2'] != ' ':
                        if dicjogo['b3'] != ' ':
                            if dicjogo['c1'] != ' ':
                                if dicjogo['c2'] != ' ':
                                    if dicjogo['c3'] != ' ':
                                        print('Fim de jogo!')
                                        print('Velha!!')
                                        continuar = input('Deseja jogar novamente? ')
                                        finalizar(continuar)
    if dicjogo['a1'] == dicjogo['a2'] and ['a2'] == ['a3'] and ['a1'] != ' ':
        print('Fim de jogo!')
        print(f'{jogador} venceu!!')
        continuar = input('Deseja jogar novamente? ')
        finalizar(continuar)

    elif dicjogo['b1'] == dicjogo['b2'] and dicjogo['b2'] == dicjogo['b3'] and dicjogo['b1'] != ' ':
        print('Fim de jogo!')
        print(f'{jogador} venceu!!')
        continuar = input('Deseja jogar novamente? ')
        finalizar(continuar)
    elif dicjogo['c1'] == dicjogo['c2'] and dicjogo['c2'] == dicjogo['c3'] and dicjogo['c1'] != ' ':
        print('Fim de jogo!')
        print(f'{jogador} venceu!!')
        continuar = input('Deseja jogar novamente? ')
        finalizar(continuar)
    elif dicjogo['a1'] == dicjogo['b1'] and dicjogo['b1'] == dicjogo['c1'] and dicjogo['a1'] != ' ':
        print('Fim de jogo!')
        print(f'{jogador} venceu!!')
        continuar = input('Deseja jogar novamente? ')
        finalizar(continuar)
    elif dicjogo['a2'] == dicjogo['b2'] and dicjogo['b2'] == dicjogo['c2'] and dicjogo['a2'] != ' ':
        print('Fim de jogo!')
        print(f'{jogador} venceu!!')
        continuar = input('Deseja jogar novamente? ')
        finalizar(continuar)
    elif dicjogo['a3'] == dicjogo['b3'] and dicjogo['b3'] == dicjogo['c3'] and dicjogo['a3'] != ' ':
        print('Fim de jogo!')
        print(f'{jogador} venceu!!')
        continuar = input('Deseja jogar novamente? ')
        finalizar(continuar)
    elif dicjogo['a3'] == dicjogo['b2'] and dicjogo['b2'] == dicjogo['c1'] and dicjogo['a3'] != ' ':
        print('Fim de jogo!')
        print(f'{jogador} venceu!!')
        continuar = input('Deseja jogar novamente? ')
        finalizar(continuar)
    elif dicjogo['a1'] == dicjogo['b2'] and dicjogo['b2'] == dicjogo['c3'] and dicjogo['a1'] != ' ':
        print('Fim de jogo!')
        print(f'{jogador} venceu!!')
        continuar = input('Deseja jogar novamente? ')
        finalizar(continuar)
        
    else:
        maquina(dicjogo, valor)

def jogopessoa(lugar, valor, dicjogo):
    dicjogo = dicjogo
    valor = valor
    if lugar == 'a1':
        dicjogo['a1'] = valor
    elif lugar == 'a2':
        dicjogo['a2'] = valor
    elif lugar == 'a3':
        dicjogo['a3'] = valor
    elif lugar == 'b1':
        dicjogo['b1'] = valor
    elif lugar == 'b2':
        dicjogo['b2'] = valor
    elif lugar == 'b3':
        dicjogo['b3'] = valor
    elif lugar == 'c1':
        dicjogo['c1'] = valor
    elif lugar == 'c2':
        dicjogo['c2'] = valor
    elif lugar == 'c3':
        dicjogo['c3'] = valor
    else:
        print('Essa casa não existe')
        if valor == 'o':
            valor = 'x'
        elif valor == 'x':
            valor = 'o'
        jogopergunta(dicjogo, valor)
        
    print(dicjogo['a1'],'|', dicjogo['b1'],'|', dicjogo['c1'], '     a1|b1|c1' )
    print('---------     ---------')
    print(dicjogo['a2'],'|', dicjogo['b2'],'|', dicjogo['c2'], '     a2|b2|c2' )
    print('---------     ---------')
    print(dicjogo['a3'],'|', dicjogo['b3'],'|', dicjogo['c3'], '     a3|b3|c3' )
    jogoanalisepessoa(dicjogo, valor)

def jogoanalisepessoa(dicjogo, valor):
    dicjogo = dicjogo
    valor = valor
    if dicjogo['a1'] != ' ': 
        if dicjogo['a2'] != ' ': 
            if dicjogo['a3'] != ' ': 
                if dicjogo['b1'] != ' ':
                    if dicjogo['b2'] != ' ':
                        if dicjogo['b3'] != ' ':
                            if dicjogo['c1'] != ' ':
                                if dicjogo['c2'] != ' ':
                                    if dicjogo['c3'] != ' ':
                                        print('Fim de jogo!')
                                        print('Velha!!')
                                        continuar = input('Deseja jogar novamente? ')
                                        finalizar(continuar)
    if dicjogo['a1'] == dicjogo['a2'] and ['a2'] == ['a3'] and ['a1'] != ' ':
        print('Fim de jogo!')
        print(f'{valor} venceu!!')
        continuar = input('Deseja jogar novamente? ')
        finalizar(continuar)

    elif dicjogo['b1'] == dicjogo['b2'] and dicjogo['b2'] == dicjogo['b3'] and dicjogo['b1'] != ' ':
        print('Fim de jogo!')
        print(f'{valor} venceu!!')
        continuar = input('Deseja jogar novamente? ')
        finalizar(continuar)
    elif dicjogo['c1'] == dicjogo['c2'] and dicjogo['c2'] == dicjogo['c3'] and dicjogo['c1'] != ' ':
        print('Fim de jogo!')
        print(f'{valor} venceu!!')
        continuar = input('Deseja jogar novamente? ')
        finalizar(continuar)
    elif dicjogo['a1'] == dicjogo['b1'] and dicjogo['b1'] == dicjogo['c1'] and dicjogo['a1'] != ' ':
        print('Fim de jogo!')
        print(f'{valor} venceu!!')
        continuar = input('Deseja jogar novamente? ')
        finalizar(continuar)
    elif dicjogo['a2'] == dicjogo['b2'] and dicjogo['b2'] == dicjogo['c2'] and dicjogo['a2'] != ' ':
        print('Fim de jogo!')
        print(f'{valor} venceu!!')
        continuar = input('Deseja jogar novamente? ')
        finalizar(continuar)
    elif dicjogo['a3'] == dicjogo['b3'] and dicjogo['b3'] == dicjogo['c3'] and dicjogo['a3'] != ' ':
        print('Fim de jogo!')
        print(f'{valor} venceu!!')
        continuar = input('Deseja jogar novamente? ')
        finalizar(continuar)
    elif dicjogo['a3'] == dicjogo['b2'] and dicjogo['b2'] == dicjogo['c1'] and dicjogo['a3'] != ' ':
        print('Fim de jogo!')
        print(f'{valor} venceu!!')
        continuar = input('Deseja jogar novamente? ')
        finalizar(continuar)
    elif dicjogo['a1'] == dicjogo['b2'] and dicjogo['b2'] == dicjogo['c3'] and dicjogo['a1'] != ' ':
        print('Fim de jogo!')
        print(f'{valor} venceu!!')
        continuar = input('Deseja jogar novamente? ')
        finalizar(continuar)
        
    else:
        jogoperguntapessoa(dicjogo, valor)

def jogoperguntapessoa(dicjogo, valor):
    dicjogo = dicjogo
    if valor == 'o':
        valor = 'x'
    elif valor == 'x':
        valor = 'o'
    else:
        valor = input('Valor invalido, digite (o ou x)')
        if valor != 'o' or valor != 'x':
            jogopergunta(dicjogo, valor)
    print(f'Vez do {jogador}')
    lugar = input('Casa desejada: ')
    valor = valor
    jogomaquina(lugar, valor, dicjogo)
