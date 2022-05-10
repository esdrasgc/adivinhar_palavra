import string
from funcoes import resumoDaRodada ,verRegras ,printTituloDoJogo, formatarAnagrama, recebeEValidaEntrada, retornaPalavraSorteada, formatarAnagrama, retornaNovoEstadoLetras, retornaNovoEstadoPalpite, printAlfabeto, printPalpite

#### Projeto individual Adivinha Palavra ##########
#### Discente: Esdras Gomes Carvalho  #############

naoTerminouOjogo = True
printTituloDoJogo()
verRegras()
quantidadeDeTentativas = []
while naoTerminouOjogo:

    ## laço para as rodadas
    partidaNaoTerminou = True
    rodada = 1
    palavraSorteada = retornaPalavraSorteada()
    palavraSortFormat = formatarAnagrama(palavraSorteada)

    lista = []
    alfabeto = list(string.ascii_lowercase)
    for i in range(26):
        buffer = [alfabeto[i], 'Preto']
        lista.append(buffer)  ## Fundo preto significa que a letra ainda não apareceu nos palpites
        buffer = 0  ## limpar o buffer
    estadoDasLetras = lista

    estadoDaSorteada = []
    for i in range(len(palavraSorteada)):
        buffer = [palavraSorteada[i], 'Oculto']
        estadoDaSorteada.append(buffer)
        buffer = 0  ## limpar o buffer


    while partidaNaoTerminou and rodada < 7:
        
        palpite = recebeEValidaEntrada()
        estadoDoPalpite = []
        for i in range(len(palpite)):
            buffer = [palpite[i], 'Preto']
            estadoDoPalpite.append(buffer)
            buffer = 0  ## limpar o buffer
        estadoDoPalpite = retornaNovoEstadoPalpite(estadoDoPalpite ,palpite, 'lindo')
        printPalpite(estadoDoPalpite)
        estadoDasLetras = retornaNovoEstadoLetras(estadoDasLetras, estadoDoPalpite)
        printAlfabeto(estadoDasLetras)

        jogoContinua = False
        for letraPalpite in estadoDoPalpite:
            if letraPalpite[1] != 'Verde':
                jogoContinua = True

        if not jogoContinua:
            partidaNaoTerminou = False
            print(f'Parabéns, você descobriu a palavra correta "{palavraSorteada}" em {rodada} tentativas.\n')
            quantidadeDeTentativas.append(rodada)
            rodada -= 1
        rodada += 1

    if rodada >= 7 :
        print(f'Infelizmente você não descobriu a palavra correta.\nA palavra era "{palavraSorteada}".\n')
        quantidadeDeTentativas.append(rodada)
    mantem_while = True
    while mantem_while:
        mantem_while = False
        recomecarJogo = input('Deseja recomeçar o jogo? [s] sim ou [n] não\n')
        if recomecarJogo == 's':
            pass
        elif recomecarJogo == 'n':
            naoTerminouOjogo = False
            print('Resumo das rodadas.\n')
            resumoDaRodada(quantidadeDeTentativas)
            # for i in range(len(quantidadeDeTentativas)):
            #     if quantidadeDeTentativas[i] < 7:
            #         print(f'Na partida {i+1} o jogador finalizou com {quantidadeDeTentativas[i]} tentativas.\n')
            #     elif quantidadeDeTentativas[i] >= 7:
            #         print(f'Na partida {i+1} o jogador não acertou a palavra.')
        else:
            print('Entrada inválida, favor escolher uma das opções citadas (digite "s" para sim e "n" para não).\n')
            mantem_while = True
    




