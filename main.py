from emoji import emojize
from time import sleep

def leiaInt(txt):
    ok = True
    op = ''
    while ok:
        try:
            print('\033[1;97m')
            op = int(input(txt))
        except:
            print('\033[1;31mERRO!\033[mPor favor, Digite uma opção válida.')
        else:
            if op >= 2 and op <= 4:
                ok = False
                return op
            else:
                print('\033[1;31mERRO!\033[mPor favor, Digite um número entre 2 e 4.')


def lerOpcao(txt):
    ok = True
    while ok:
        try:
            opcao = int(input(txt))
        except:
            print('\033[1;31mERRO!\033[mPor favor, Digite uma opção válida.')
        else:
            if opcao >= 1 and opcao <= 3:
                ok = False
                return opcao
            else:
                print('\033[1;31mERRO!\033[mPor favor, Digite uma opção válida.')


def jogarDado():
    from random import randint
    dado = [1, 2, 3, 4, 5, 6]
    print('JOGANDO DADO ', end='')
    sleep(0.5)
    print(emojize(':game_die: ', use_aliases=True), end='')
    sleep(0.5)
    print(emojize(':game_die: ', use_aliases=True), end='')
    sleep(0.5)
    print(emojize(':game_die:', use_aliases=True))
    sleep(0.8)

    resultado = dado[randint(0, 5)]

    print(f'TIROU: {resultado}!')
    sleep(1.5)
    return resultado


def layout(txt):
    print("-="*30)
    print(f'{txt:^60}')
    print('-='*30)


#JOGO
layout('MINI RPG')

#CASAS DO TABULEIRO
lista_de_casas = ['Início', emojize('Centro de Cura :heavy_plus_sign:', use_aliases=True),
                  2, emojize('GATO AMIGO :cat:', use_aliases=True), 4, emojize('NEBLINA :cloud:', use_aliases=True),
                  emojize('Ferreiro :older_man:', use_aliases=True), emojize('Trincheiras :bomb:', use_aliases=True),
                  emojize('MERCADOR SOMBRIO :smiling_imp:', use_aliases=True), emojize('TEMPESTADE :umbrella:', use_aliases=True), emojize('Samurai Mestre :man_with_gua_pi_mao:', use_aliases=True),
                  emojize('Trincheiras :bomb:', use_aliases=True), emojize('Ferreiro :older_man:', use_aliases=True), emojize('TERREMOTO :earth_africa:', use_aliases=True),
                  emojize('ESCALIBUR :hocho:', use_aliases=True), emojize('Centro de Cura :heavy_plus_sign:', use_aliases=True), emojize('GATO AMIGO :cat:', use_aliases=True),
                  emojize('MERCADOR SOMBRIO :smiling_imp:', use_aliases=True), emojize('Ferreiro :older_man:', use_aliases=True), emojize('Ciclope Amargurado :eyes:', use_aliases=True), 20, emojize('Centro de Cura :heavy_plus_sign:', use_aliases=True),
                  emojize('Trincheiras :bomb:', use_aliases=True), 23, emojize('AVALANCHE :ocean:', use_aliases=True), emojize('MERCADOR SOMBRIO :smiling_imp:', use_aliases=True),
                  26, emojize('AMIGO DA ONÇA :leopard:', use_aliases=True), emojize('NEBLINA :cloud:', use_aliases=True),
                  emojize('GUIA MISTERIOSO :skull:', use_aliases=True), emojize('Coração de Cravo :heart:', use_aliases=True)]

#JOGADORES
jogadores = [{'\033[1;35mjogador 1\033[m': 'roxo', '\033[1;31mvida\033[m': 4, '\033[1;37marmadura\033[m': 0, '\033[1;34mitem\033[m': '', '\033[1;32mpontuação\033[m': 0},
             {'\033[1;31mjogador 2\033[m': 'vermelho', '\033[1;31mvida\033[m': 4, '\033[1;37marmadura\033[m': 0, '\033[1;34mitem\033[m': '', '\033[1;32mpontuação\033[m': 0},
             {'\033[1;36mjogador 3\033[m': 'azul', '\033[1;31mvida\033[m': 4, '\033[1;37marmadura\033[m': 0, '\033[1;34mitem\033[m': '', '\033[1;32mpontuação\033[m': 0},
             {'\033[1;32mjogador 4\033[m': 'verde', '\033[1;31mvida\033[m': 4, '\033[1;37marmadura\033[m': 0, '\033[1;34mitem\033[m': '', '\033[1;32mpontuação\033[m': 0}]

listaJogadores = ['\033[1;35mJOGADOR 1\033[m', '\033[1;31mJOGADOR 2\033[m', '\033[1;36mJOGADOR 3\033[m', '\033[1;32mJOGADOR 4\033[m']

#MENU
print("""MENU DE AÇÕES DO JOGO
1 - ARREMESSAR DADOS
2 - VERIFICAR INVETÁRIO
3 - DESISTIR (ATENÇÂO: Nâo pode desistir mais de 1 jogador por rodada)""")
print('-='*30)

#DEFINIR QUANTIDADE DE PLAYERS
quant_players = leiaInt('Digite quantos playes irão jogar: ')
print('\033[m')
if quant_players == 3:
    jogadores.pop(3)
    listaJogadores.pop(3)
elif quant_players == 2:
    jogadores.pop(3)
    listaJogadores.pop(3)
    jogadores.pop(2)
    listaJogadores.pop(2)

#LOOP GAME
desistiu = False
morreu = False
quant_players = len(jogadores)
cont = 0
gameover = True
print('-*' * 30)
while gameover:
    vez = listaJogadores[cont]

    print(f'SUA VEZ: {vez}')
    pontos = jogadores[cont]['\033[1;32mpontuação\033[m']
    print(f'\033[1;97mCASA ATUAL: {lista_de_casas[pontos]}\033[m')
    opcao = lerOpcao('DIGITE SUA OPÇÃO: ')

    #OPÇÕES
    if opcao == 1:#JOGAR DADO
        jogadores[cont]['\033[1;32mpontuação\033[m'] += jogarDado()
        pontos = jogadores[cont]['\033[1;32mpontuação\033[m']
        if pontos > 30:
            msg = emojize(f'\033[1;32mPARABÉNS {listaJogadores[cont]} :tada: :tada: :tada:', use_aliases=True)
            print(f'{msg:^60}')
            print(f'{"!!!VOCÊ VENCEU!!!":^60}')
            gameover = False
        else:
            print(f'\033[1;97mCASA ATUAL: {lista_de_casas[pontos]}\033[m')
            sleep(1)

        #AÇÕES DO MEIO DO JOGO
        if lista_de_casas[pontos] == emojize('Centro de Cura :heavy_plus_sign:', use_aliases=True):#CENTRO DE CURA
            print(emojize('PRECISA DAR UMA PAUSA, PEGUE ISSO PRA REFRESCAR!: \033[1;32m+1 :heart:\033[m', use_aliases=True))
            jogadores[cont]['\033[1;31mvida\033[m'] += 1
            sleep(1.2)
        elif lista_de_casas[pontos] == emojize('GATO AMIGO :cat:', use_aliases=True):#GATO AMIGO
            print(emojize('NÃO FAZ MUITO CARINHO, ELE MORDE!: \033[1;32m+1 :house:\033[m', use_aliases=True))
            jogadores[cont]['\033[1;32mpontuação\033[m'] += 1
            sleep(1.2)
        elif lista_de_casas[pontos] == emojize('NEBLINA :cloud:', use_aliases=True):#DESASTRES
            print(emojize('O CAMINHO NÃO É POR AÍ, DEVE ESTAR CEGO: \033[1;31m-3 :house:\033[m', use_aliases=True))
            jogadores[cont]['\033[1;32mpontuação\033[m'] -= 3
            sleep(1.2)
        elif lista_de_casas[pontos] == emojize('TEMPESTADE :umbrella:', use_aliases=True):
            print(emojize('FALEI PRA TRAZER O GUARDA-CHUVA!: \033[1;31m-3 :house:\033[m', use_aliases=True))
            jogadores[cont]['\033[1;32mpontuação\033[m'] -= 3
            sleep(1.2)
        elif lista_de_casas[pontos] == emojize('TERREMOTO :earth_africa:', use_aliases=True):
            print(emojize('SEGURE-SE QUEM PUDER, NÃO ESTAMOS NO JAPÃO: \033[1;31m-3 :house:\033[m', use_aliases=True))
            jogadores[cont]['\033[1;32mpontuação\033[m'] -= 3
            sleep(1.2)
        elif lista_de_casas[pontos] == emojize('AVALANCHE :ocean:', use_aliases=True):
            print(emojize('OPS! VOCÊ ACABOU FALANDO ALTO DEMAIS: \033[1;31m-3 :house:\033[m', use_aliases=True))
            jogadores[cont]['\033[1;32mpontuação\033[m'] -= 3
            sleep(1.2)
        elif lista_de_casas[pontos] == emojize('AMIGO DA ONÇA :leopard:', use_aliases=True):
            print(emojize('ESCOLHA MELHOR SEUS "AMIGOS"!: \033[1;31m-5 :house:\033[m', use_aliases=True))
            jogadores[cont]['\033[1;32mpontuação\033[m'] -= 5
            sleep(1.2)
        elif lista_de_casas[pontos] == emojize('GUIA MISTERIOSO :skull:', use_aliases=True):
            print(emojize('ELE ACABOU ERRANDO O CAMINHO, NUNCA ACEITE AJUDA DE ESTRANHOS!: \033[1;31m-8 :house:\033[m', use_aliases=True))
            jogadores[cont]['\033[1;32mpontuação\033[m'] -= 8
            sleep(1.2)
        elif lista_de_casas[pontos] == emojize('Ferreiro :older_man:', use_aliases=True):#FERREIRO
            print(emojize('BOM VELHINHO A ARMADURA TORNA!: \033[1;97m+1 :lock:\033[m', use_aliases=True))
            jogadores[cont]['\033[1;37marmadura\033[m'] += 1
            sleep(1.2)
        elif lista_de_casas[pontos] == emojize('Trincheiras :bomb:', use_aliases=True):#TRINCHEIRAS
            print(emojize('CUIDADO ONDE PISA! MAS PODE LEVAR ISSO PRA BRINCAR: \033[1;34m bomba :bomb:\033[m', use_aliases=True))
            jogadores[cont]['\033[1;34mitem\033[m'] = emojize('\033[1;34m bomba :bomb:\033[m', use_aliases=True)
            sleep(1.2)
        elif lista_de_casas[pontos] == emojize('MERCADOR SOMBRIO :smiling_imp:', use_aliases=True):#MERCADOR SOMBRIO
            print(emojize('NÃO ACEITE DOCE DA MÃO DE ESTRANHOS!, NÃO TE DISSERAM ISSO?: \033[1;35m anel de almas :ring:\033[m | \033[1;31m-1 :heart:\033[m ', use_aliases=True))
            jogadores[cont]['\033[1;34mitem\033[m'] = emojize('\033[1;35m anel de almas :ring:\033[m', use_aliases=True)
            jogadores[cont]['\033[1;31mvida\033[m'] -= 1
            if jogadores[cont]['\033[1;31mvida\033[m'] <= 0:
                print(emojize('\033[1;31mVOCÊ MORREU! \033[1;97m:skull:\033[m', use_aliases=True))
                morreu = True
                jogadorMorto = cont
            sleep(1.2)
        elif lista_de_casas[pontos] == emojize('ESCALIBUR :hocho:', use_aliases=True):#ESCALIBUR
            print(emojize('VOCÊ EMPUNHOU A LENDÁRIA ESCALIBUR, RECEBA SUAS GRAÇAS!: \033[1;33m escalibur :hocho:\033[m | \033[1;97m+1 :lock:\033[m', use_aliases=True))
            jogadores[cont]['\033[1;34mitem\033[m'] = emojize('\033[1;33m escalibur :hocho:\033[m', use_aliases=True)
            jogadores[cont]['\033[1;37marmadura\033[m'] += 1
            sleep(1.2)
        elif lista_de_casas[pontos] == emojize('Samurai Mestre :man_with_gua_pi_mao:', use_aliases=True):#SAMURAI MESTRE
            print('\033[1;31mO SAMURAI MESTRE')
            sleep(1.8)
            print('\033[1;97mabandonado por seus pais precisou sobreviver e aprender artes macias sozinho, para fazer comida.')
            sleep(3)
            print('.')
            sleep(0.6)
            print('.')
            sleep(0.6)
            print('.')
            sleep(1.5)
            pontos_de_vida = jogadores[cont]['\033[1;31mvida\033[m'] + jogadores[cont]['\033[1;37marmadura\033[m']
            item = jogadores[cont]['\033[1;34mitem\033[m']
            if jogadores[cont]['\033[1;34mitem\033[m'] == '':
                print(f"VOCÊ POSSUI NENHUM ITEM PARA DERROTA-LO!")
                if pontos_de_vida > 2:
                    print(emojize('ELE É O MESTRE NAS FACAS, TE FEZ DE PEIXE!: \033[1;31m-2 :heart:\033[m ', use_aliases=True))
                    jogadores[cont]['\033[1;31mvida\033[m'] = pontos_de_vida - 2
                    jogadores[cont]['\033[1;37marmadura\033[m'] = 0
                else:
                    print(emojize('ELE RESOLVEU FAZER SUSHI HOJE!: \033[1;31m-2 :heart:\033[m ', use_aliases=True))
                    print(emojize('\033[1;31mVOCÊ MORREU! \033[1;97m:skull:\033[m', use_aliases=True))
                    morreu = True
                    jogadorMorto = cont
            elif jogadores[cont]['\033[1;34mitem\033[m'] == emojize('\033[1;34m bomba :bomb:\033[m', use_aliases=True):
                print(emojize('VOCÊ EXPLODIU ELE COM UMA BOMBA, PORÉM ISSO TBM O MACHUCOU!: \033[1;31m-1 :heart:\033[m ', use_aliases=True))
                jogadores[cont]['\033[1;31mvida\033[m'] = pontos_de_vida - 1
                jogadores[cont]['\033[1;34mitem\033[m'] = ''
                jogadores[cont]['\033[1;37marmadura\033[m'] = 0
                if jogadores[cont]['\033[1;31mvida\033[m'] <= 0:
                    print(emojize('\033[1;31mVOCÊ MORREU! \033[1;97m:skull:\033[m', use_aliases=True))
                    morreu = True
                    jogadorMorto = cont
            elif jogadores[cont]['\033[1;34mitem\033[m'] == emojize('\033[1;33m escalibur :hocho:\033[m', use_aliases=True):
                print(emojize('COM A ESCALIBUR QUALQUER UM FAZ ESTRAGO, ELE FICOU COM INVEJA DA ESPADA!', use_aliases=True))
                jogadores[cont]['\033[1;34mitem\033[m'] = ''
            elif jogadores[cont]['\033[1;34mitem\033[m'] == emojize('\033[1;35m anel de almas :ring:\033[m', use_aliases=True):
                print(emojize('ELE ARRANCOU DE VOCÊ O ANEL DA ALMA, E ISSO O DEIXOU MAIS FORTE!: \033[1;31m-3 :heart:\033[m ', use_aliases=True))
                jogadores[cont]['\033[1;31mvida\033[m'] = pontos_de_vida - 3
                jogadores[cont]['\033[1;34mitem\033[m'] = ''
                jogadores[cont]['\033[1;37marmadura\033[m'] = 0
                if jogadores[cont]['\033[1;31mvida\033[m'] <= 0:
                    print(emojize('\033[1;31mVOCÊ MORREU! \033[1;97m:skull:\033[m', use_aliases=True))
                    morreu = True
                    jogadorMorto = cont
        elif lista_de_casas[pontos] == emojize('Ciclope Amargurado :eyes:', use_aliases=True):#CICLOPE AMARGURADO
            print('\033[1;31mO CICLOPE AMARGURADO')
            sleep(1.8)
            print('\033[1;97mum gigante ciclope de coração ferido, após sua amada o dizer que ele não tinha olhos para os dois.')
            sleep(3)
            print('.')
            sleep(0.6)
            print('.')
            sleep(0.6)
            print('.')
            sleep(1.5)
            pontos_de_vida = jogadores[cont]['\033[1;31mvida\033[m'] + jogadores[cont]['\033[1;37marmadura\033[m']
            item = jogadores[cont]['\033[1;34mitem\033[m']
            if jogadores[cont]['\033[1;34mitem\033[m'] == '':
                print(f"VOCÊ POSSUI NENHUM ITEM PARA DERROTA-LO!")
                if pontos_de_vida > 3:
                    print(emojize('ELE POSSUI SÓ UM OLHO, MAS MUITA VONTADE DE ESMAGAR!: \033[1;31m-3 :heart:\033[m ', use_aliases=True))
                    jogadores[cont]['\033[1;31mvida\033[m'] = pontos_de_vida - 3
                    jogadores[cont]['\033[1;37marmadura\033[m'] = 0
                else:
                    print(emojize('ELE NÃO DEIXOU BARATO PARA VOCÊ, ACHO QUE IMAGINOU A SUA AMADA COMO VOCÊ!: \033[1;31m-3 :heart:\033[m ', use_aliases=True))
                    print(emojize('\033[1;31mVOCÊ MORREU! \033[1;97m:skull:\033[m', use_aliases=True))
                    morreu = True
                    jogadorMorto = cont
            elif jogadores[cont]['\033[1;34mitem\033[m'] == emojize('\033[1;34m bomba :bomb:\033[m', use_aliases=True):
                print(emojize('VOCÊ EXPLODIU ELE COM UMA BOMBA, PORÉM ISSO TBM O MACHUCOU!: \033[1;31m-1 :heart:\033[m ', use_aliases=True))
                jogadores[cont]['\033[1;31mvida\033[m'] = pontos_de_vida - 1
                jogadores[cont]['\033[1;34mitem\033[m'] = ''
                jogadores[cont]['\033[1;37marmadura\033[m'] = 0
                if jogadores[cont]['\033[1;31mvida\033[m'] <= 0:
                    print(emojize('\033[1;31mVOCÊ MORREU! \033[1;97m:skull:\033[m', use_aliases=True))
                    morreu = True
                    jogadorMorto = cont
            elif jogadores[cont]['\033[1;34mitem\033[m'] == emojize('\033[1;33m escalibur :hocho:\033[m', use_aliases=True):
                print(emojize('ELE SE RENDEU AO BRILHO DA ESPADA, MAS TE PEDIU PRA IR EMBORA!: | \033[1;31m-1 :house:\033[m', use_aliases=True))
                jogadores[cont]['\033[1;34mitem\033[m'] = ''
                jogadores[cont]['\033[1;32mpontuação\033[m'] -= 1
            elif jogadores[cont]['\033[1;34mitem\033[m'] == emojize('\033[1;35m anel de almas :ring:\033[m', use_aliases=True):
                print(emojize('ELE ARRANCOU DE VOCÊ O ANEL DA ALMA, E ISSO O DEIXOU MAIS FORTE!: \033[1;31m-4 :heart:\033[m ', use_aliases=True))
                jogadores[cont]['\033[1;31mvida\033[m'] = pontos_de_vida - 4
                jogadores[cont]['\033[1;34mitem\033[m'] = ''
                jogadores[cont]['\033[1;37marmadura\033[m'] = 0
                if jogadores[cont]['\033[1;31mvida\033[m'] <= 0:
                    print(emojize('\033[1;31mVOCÊ MORREU! \033[1;97m:skull:\033[m', use_aliases=True))
                    morreu = True
                    jogadorMorto = cont
        elif lista_de_casas[pontos] == emojize('Coração de Cravo :heart:', use_aliases=True):#CORAÇÃO DE CRAVO
            print('\033[1;31mCORAÇÃO DE CRAVO')
            sleep(1.8)
            print('\033[1;97mpronto para descontar suas mágoas com a dona rosa em qualquer um na sua frente.')
            sleep(3)
            print('.')
            sleep(0.6)
            print('.')
            sleep(0.6)
            print('.')
            sleep(1.5)
            pontos_de_vida = jogadores[cont]['\033[1;31mvida\033[m'] + jogadores[cont]['\033[1;37marmadura\033[m']
            item = jogadores[cont]['\033[1;34mitem\033[m']
            if jogadores[cont]['\033[1;34mitem\033[m'] == '':
                print(f"VOCÊ POSSUI NENHUM ITEM PARA DERROTA-LO!")
                if pontos_de_vida > 4:
                    print(emojize('DESCULPE POR TE EXPULSAR DE MEU JARDIM, FLORES NÃO COSTUMAM SER DELICADAS!: \033[1;31m-4 :heart:\033[m | \033[1;31m-6 :house:\033[m', use_aliases=True))
                    jogadores[cont]['\033[1;31mvida\033[m'] = pontos_de_vida - 4
                    jogadores[cont]['\033[1;32mpontuação\033[m'] -= 6
                    jogadores[cont]['\033[1;37marmadura\033[m'] = 0
                else:
                    print(emojize('ELE SENTE MUITO POR ISSO, SE TALVEZ VOCÊ FOSSE UMA ABELINHA!: \033[1;31m-4 :heart:\033[m ', use_aliases=True))
                    print(emojize('\033[1;31mVOCÊ MORREU! \033[1;97m:skull:\033[m', use_aliases=True))
                    morreu = True
                    jogadorMorto = cont
            elif jogadores[cont]['\033[1;34mitem\033[m'] == emojize('\033[1;34m bomba :bomb:\033[m', use_aliases=True):
                print(emojize('VOCÊ O EXPLODIU COM A BOMBA, MAS VOCÊ VOOU PRA LONGE!: \033[1;31m-1 :heart:\033[m | \033[1;31m-2 :house:\033[m', use_aliases=True))
                jogadores[cont]['\033[1;31mvida\033[m'] = pontos_de_vida - 2
                jogadores[cont]['\033[1;34mitem\033[m'] = ''
                jogadores[cont]['\033[1;32mpontuação\033[m'] -= 2
                jogadores[cont]['\033[1;37marmadura\033[m'] = 0
                if jogadores[cont]['\033[1;31mvida\033[m'] <= 0:
                    print(emojize('\033[1;31mVOCÊ MORREU! \033[1;97m:skull:\033[m', use_aliases=True))
                    morreu = True
                    jogadorMorto = cont
            elif jogadores[cont]['\033[1;34mitem\033[m'] == emojize('\033[1;33m escalibur :hocho:\033[m', use_aliases=True):
                print(emojize('TE EXPULSOU DO JARDIM ANTES QUE O CORTASSE COM A ESPADA!: | \033[1;31m-2 :house:\033[m', use_aliases=True))
                jogadores[cont]['\033[1;34mitem\033[m'] = ''
                jogadores[cont]['\033[1;32mpontuação\033[m'] -= 2
            elif jogadores[cont]['\033[1;34mitem\033[m'] == emojize('\033[1;35m anel de almas :ring:\033[m', use_aliases=True):
                print(emojize('O ANEL O DEIXOU ENCANTADO, POR ISSO TE DEU UM PRESENTE!: \033[1;31m-4 :heart:\033[m | \033[1;31m-8 :house:\033[m | \033[1;34m bomba :bomb:\033[m', use_aliases=True))
                jogadores[cont]['\033[1;31mvida\033[m'] = pontos_de_vida - 5
                jogadores[cont]['\033[1;34mitem\033[m'] = emojize('\033[1;34m bomba :bomb:\033[m', use_aliases=True)
                jogadores[cont]['\033[1;32mpontuação\033[m'] -= 8
                jogadores[cont]['\033[1;37marmadura\033[m'] = 0
                if jogadores[cont]['\033[1;31mvida\033[m'] <= 0:
                    print(emojize('\033[1;31mVOCÊ MORREU! \033[1;97m:skull:\033[m', use_aliases=True))
                    morreu = True
                    jogadorMorto = cont


    elif opcao == 2:#VER INVENTÁRIO
        pontos = 0
        print(f'{"INVENTÁRIO":-^73}')
        for key, value in jogadores[cont].items():
            if value == '':
                value = 'Nenhum Item'
            print(f'|{key:^30}|{value:^50}|')
        print('-'*73)
        cont -= 1

    else:  #DESITÊNCIA
        print(f'{vez} DESISTIU DO JOGO =(')
        desistiu = True
        jogadorDesistor = cont


    # CONDIÇÃO DE GAME OVER OU VITÓRIA
    if jogadores[cont]['\033[1;32mpontuação\033[m'] > 30:
        msg = emojize(f'\033[1;32mPARABÉNS {listaJogadores[cont]} :tada: :tada: :tada:', use_aliases=True)
        print(f'{msg:^60}')
        print(f'{"!!!VOCÊ VENCEU!!!":^60}')
        gameover = False
        break;

    #CONTAGEM DE VEZ
    if cont == quant_players - 1:
        cont = 0
        if desistiu:
            jogadores.pop(jogadorDesistor)
            listaJogadores.pop(jogadorDesistor)
            quant_players -= 1
            desistiu = False
        elif morreu:
            jogadores.pop(jogadorMorto)
            listaJogadores.pop(jogadorMorto)
            quant_players -= 1
            morreu = False
    else:
        cont += 1
    if quant_players == 1:
        msg = emojize(f'\033[1;32mPARABÉNS {listaJogadores[0]} :tada: :tada: :tada:', use_aliases=True)
        print(f'{msg:^60}')
        print(f'{"!!!VOCÊ VENCEU!!!":^60}')
        gameover = False

    print('-*'*30)

print('-'*60)
print(f"\033[1;31m{'GAME OVER':^60}\033[m")
print('-'*60)