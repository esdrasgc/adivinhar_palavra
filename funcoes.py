import sys
from colorama import Fore, Back, Style
import colorama
import string
from random import randint
import unidecode
from palavrasPTBR import retornaAsPalavrasPTBR


### Recebe a entrada e valida se ela tem 5 caracteres, se é um anagrama válido e por fim se é uma palavra válida
def recebeEValidaEntrada():
    mantem_while = True
    while mantem_while:
        mantem_while = False
        entrada = input('Digite seu palpite: ')
        if verificaAnagrama(entrada):
            if len(entrada) == 5:
                if verificaPalavraPTBR(entrada):
                    return entrada
                else:
                    mantem_while = True
                    print('O anagrama escolhido não é uma palavra, favor tentar novamente.')
            else:
                print('O anagrama escolhido não tem 5 letras, tente novamente.')
                mantem_while = True
        else:
            print('Entrada contém caracteres inválidos, favor tentar novamente.')
            mantem_while = True

### Função para verificar se é um anagrama, ou seja, se é formado somente por caracteres que pertencem ao alfabeto PT-BR
def verificaAnagrama(entrada):
    alfabeto = list(string.ascii_lowercase)
    EhAnagrama = True
    for caracter in entrada:
        caracterInvalido = True
        for letra in alfabeto:
            if letra == caracter:
                caracterInvalido = False
        if caracterInvalido:
            EhAnagrama = False
            break

    return EhAnagrama

### Função para verficar se a palavra pertence ao dicionario brasileiro.
### As palavras foram filtradas da lista presente em: https://www.ime.usp.br/~pf/dicios/br-utf8.txt
def verificaPalavraPTBR(anagrama):
    anagrama = formatarAnagrama(anagrama)

    listaPalavrasPTBR = filtraPalavrasValidas()
    listaFormatadaPalavras = formatarListaPalavras(listaPalavrasPTBR)

    palavraInvalida = True
    for palavra in listaFormatadaPalavras:
        if anagrama == palavra:
            palavraInvalida = False
            break

    return (not palavraInvalida)

### Funcao que retorna a lista de palavras existentes no dicionario brasileiro que tenham 5 letras.
def filtraPalavrasValidas():
    lista_de_palavras = retornaAsPalavrasPTBR().split()
    lista_de_palavras_validas = []
    for palavra in lista_de_palavras:
        if len(palavra) == 5:
            lista_de_palavras_validas.append(palavra)

    return lista_de_palavras_validas

### Função para formatar o anagrama, deixando todas as letras minusculas e retirando acentos.
def formatarAnagrama(anagrama):
    anagrama = anagrama.lower()
    anagrama = unidecode.unidecode(anagrama)
    return anagrama

### retorna uma lista de palavras formatadas (sem acento e lowcase).
def formatarListaPalavras(lista):

    for i in range(len(lista)):
        palavra = lista[i]
        palavra = formatarAnagrama(palavra)
        lista[i] = palavra 

    return lista
        
### retorna a Palavra sorteada dentre as possiveis em listaPalavras
def retornaPalavraSorteada():
    listaPalavras = ['Amapá', 'André', 'Argel', 'Argos', 'Artur', 'Aécio', 'Babel', 'Bagdá', 'Bangu', 'Belém', 'Bento', 'Berna', 'Berta', 'Bielo', 'Borba', 'Bruno', 'Carla', 'Ceará', 'Chica', 'Chico', 'Chile', 'China']
    listaPalavras += ['Filho', 'Fábio', 'Gales', 'Gauss', 'Goiás', 'Golfo', 'Hegel', 'Intel']
    listaPalavras += ['Japão', 'Jesus', 'Jobim', 'Jorge', 'Nobel', 'Norte', 'Paris', 'Paula', 'Paulo']
    listaPalavras += ['ajudá', 'alada', 'alado', 'alaga', 'anime']
    listaPalavras += ['seduz', 'segue', 'segui', 'seios', 'seita', 'seiva', 'seixo', 'sejam', 'sejas', 'selai']
    listaPalavras += [ 'raies', 'raios', 'raiou', 'raiva']
    listaPalavras += ['opção', 'opõem', 'opões', 'orado', 'orais', 'oramo', 'orara', 'orará', 'orava', 'orcas', 'orcei', 'orcem', 'orces', 'ordem', 'oreis', 'oremo', 'orgem', 'orges', 'orgia']
    listaPalavras += ['médio', 'mídia', 'míope', 'móvel', 'múmia', 'mútua', 'mútuo']
    listaPalavras += [ 'grato', 'graus', 'grava', 'grave', 'gravo', 'graxa', 'graxo', 'graça', 'grega', 'grego', 'greve', 'grifa', 'grife', 'grifo', 'grifá', 'grila', 'grile', 'grilo', 'grilá', 'gripe', 'grita', 'grite', 'grito', 'gritá', 'gruda', 'grude', 'grudo', 'grudá', 'grupo', 'gruta', 'grãos', 'gueto', 'guiai', 'guiam', 'guiar',]
    listaPalavras += ['durou', 'dutos', 'dália', 'débil', 'dólar', 'dúbia', 'dúbio', 'dúzia', 'ecoai', 'ecoam', 'ecoar']
    listaPalavras += ['temor', 'temos', 'tempo', 'tenaz', 'tenda', 'tende', 'tendi']
    listaPalavras += [ 'vogal', 'volta', 'volte', 'volto', 'voltá', 'volva', 'volve', 'volvi', 'volvo', 'volvê', 'voraz', 'vossa', 'vosso', 'votai', 'votam', 'votar', 'votas', 'votei', 'votem']
    listaPalavras += ['ósseo', 'ótica', 'ótico', 'ótima', 'ótimo', 'óvulo', 'óxido', 'úmida', 'úmido', 'única', 'único', 'úrico', 'úteis', 'útero', 'toshi', 'grazi']
    numeroSorteado = randint(0, (len(listaPalavras)-1))
    palavraSorteada = listaPalavras[numeroSorteado]
    return palavraSorteada

### Função para alterar "estado da letra"
### Trata-se de uma função que busca um dado elemento na lista de palavras e altera o estado (string com a cor que a letra terá no print)
def alteraEstadoDasLetras(estadoDasLetras, letraObjetivo, novoEstado):
    for i in range(len(estadoDasLetras)):
        lista = estadoDasLetras[i]
        letra = lista[0]
        if letra == letraObjetivo:
            estadoDasLetras[i][1] = novoEstado
            break
    return estadoDasLetras

### Função que realiza uma busca e retorna o indice do elemento
def retornaIndiceDeEstadoDeLetras(estadoDasLetras, letraObjetivo):
    for i in range(len(estadoDasLetras)):
        lista = estadoDasLetras[i]
        letra = lista[0]
        if letra == letraObjetivo:
            return i

### Função que faz a verificação e altera o estado das letras no palpite (o estado é a cor da letra)
def retornaNovoEstadoPalpite(estadoDoPalpite, palpite, palavraSortFormat):
    
    for i in range(len(palpite)):
        if palpite[i] == palavraSortFormat[i]:
            estadoDoPalpite[i][1] = 'Verde'
    
    listaQuantidadeDeRepeticoes = []

    for i in range(len(palpite)):
        quantidadeDeRepeticoesDaLetra = 0
        if (estadoDoPalpite[i][1] != 'Verde') and (estadoDoPalpite[i][1] != 'Amarelo') and (estadoDoPalpite[i][1] != 'Cinza'):
            for letraSort in palavraSortFormat:
                if palpite[i] == letraSort:
                    quantidadeDeRepeticoesDaLetra += 1
        listaQuantidadeDeRepeticoes.append(quantidadeDeRepeticoesDaLetra)


    for i in range(len(listaQuantidadeDeRepeticoes)):
        if (estadoDoPalpite[i] != 'Amarelo') and (estadoDoPalpite[i] != 'Verde'):
            for j in range(i ,len(listaQuantidadeDeRepeticoes)):
                
                if (palpite[i] == palpite[j]) and (listaQuantidadeDeRepeticoes[i] > 0):
                    listaQuantidadeDeRepeticoes[i] -= 1
                    estadoDoPalpite[j][1] = 'Amarelo'

    for i in range(len(palpite)):
        if estadoDoPalpite[i][1] == 'Preto':
            estadoDoPalpite[i][1] = 'Cinza'

    return estadoDoPalpite
    
### Função que realiza a verificação e altera o estado das letras no alfabeto.
def retornaNovoEstadoLetras(estadoDasLetras, estadoDoPalpite):
    for lista in estadoDoPalpite:
        if (lista[1] == 'Verde'):
            estadoDasLetras = alteraEstadoDasLetras(estadoDasLetras, lista[0], 'Verde')
    
    for lista in estadoDoPalpite:
        indice = retornaIndiceDeEstadoDeLetras(estadoDasLetras, lista[0])
        if (lista[1] == 'Verde'):
            pass

        elif (lista[1] == 'Amarelo'):
            
            if (estadoDasLetras[indice][1] != 'Verde') and (estadoDasLetras[indice][1] != 'Cinza'): ## Verifica se a letra em questão já recebeu status de presente ou ausente, elas não precisam ser verificadas novamente.
                estadoDasLetras[indice][1] = 'Amarelo'

        elif (lista[1] == 'Cinza'):
            if (estadoDasLetras[indice][1] != 'Verde') and (estadoDasLetras[indice][1] != 'Amarelo'):
                estadoDasLetras[indice][1] = 'Cinza'

        else:
            raise('Erro na função retornaNovoEstadoLetras.')

    return estadoDasLetras

### Função para printar o palpite de forma correspondente ao seu estado (string com a cor do elemento).
def printPalpite(estadoDoPalpite):
    colorama.init()

    dic = {
        'Verde' : Back.GREEN,
        'Amarelo' : Back.YELLOW,
        'Cinza' : Back.LIGHTBLACK_EX,
        'Preto' : ''
    }

    for letraPalpite in estadoDoPalpite:
        # print('['+ '\033[4m' + f' {letraPalpite[0]} ' + Style.RESET_ALL + ']')
        sys.stdout.write('['+ dic[letraPalpite[1]] + f' {letraPalpite[0]} ' + Style.RESET_ALL + '] ')
    print('\n')

### Função para printar o alfabeto de forma correspondente ao seu estado.
def printAlfabeto(estadoDasLetras):
    colorama.init()

    
    dic = {
        'Verde' : Back.GREEN,
        'Amarelo' : Back.YELLOW,
        'Cinza' : Back.LIGHTBLACK_EX,
        'Preto' : ''
    }

    i =0
    for letra in estadoDasLetras:
        i+=1
        sys.stdout.write('|'+ dic[letra[1]] + f' {letra[0]} ' + Style.RESET_ALL + '| ')
        if i%8 == 0:
            print('')
    print('')


def printTituloDoJogo():
    titulo = """
       
       
      _____                    _____                    _____                    _____                   _______         
     /\    \                  /\    \                  /\    \                  /\    \                 /::\    \        
    /::\    \                /::\    \                /::\    \                /::\____\               /::::\    \       
    \:::\    \              /::::\    \              /::::\    \              /::::|   |              /::::::\    \      
     \:::\    \            /::::::\    \            /::::::\    \            /:::::|   |             /::::::::\    \     
      \:::\    \          /:::/\:::\    \          /:::/\:::\    \          /::::::|   |            /:::/~~\:::\    \    
       \:::\    \        /:::/__\:::\    \        /:::/__\:::\    \        /:::/|::|   |           /:::/    \:::\    \   
       /::::\    \      /::::\   \:::\    \      /::::\   \:::\    \      /:::/ |::|   |          /:::/    / \:::\    \  
      /::::::\    \    /::::::\   \:::\    \    /::::::\   \:::\    \    /:::/  |::|___|______   /:::/____/   \:::\____\ 
     /:::/\:::\    \  /:::/\:::\   \:::\    \  /:::/\:::\   \:::\____\  /:::/   |::::::::\    \ |:::|    |     |:::|    |
    /:::/  \:::\____\/:::/__\:::\   \:::\____\/:::/  \:::\   \:::|    |/:::/    |:::::::::\____\|:::|____|     |:::|    |
   /:::/    \::/    /\:::\   \:::\   \::/    /\::/   |::::\  /:::|____|\::/    / ~~~~~/:::/    / \:::\    \   /:::/    / 
  /:::/    / \/____/  \:::\   \:::\   \/____/  \/____|:::::\/:::/    /  \/____/      /:::/    /   \:::\    \ /:::/    /  
 /:::/    /            \:::\   \:::\    \            |:::::::::/    /               /:::/    /     \:::\    /:::/    /   
/:::/    /              \:::\   \:::\____\           |::|\::::/    /               /:::/    /       \:::\__/:::/    /    
\::/    /                \:::\   \::/    /           |::| \::/____/               /:::/    /         \::::::::/    /     
 \/____/                  \:::\   \/____/            |::|  ~|                    /:::/    /           \::::::/    /      
                           \:::\    \                |::|   |                   /:::/    /             \::::/    /       
                            \:::\____\               \::|   |                  /:::/    /               \::/____/        
                             \::/    /                \:|   |                  \::/    /                 ~~              
                              \/____/                  \|___|                   \/____/                                  
                                                                                                                         
     """
    print(titulo)

### Função para apresentar as regras do jogo.
def verRegras():
    mantem_while = True
    while mantem_while:
        mantem_while = False
        escolha = input('Deseja visualizar as regras do jogo? [s] sim ou [n] não\n')
        if escolha == 's':
            print('O jogador deve adivinhar a palavra em até 6 tentativas.\nA palavra tem 5 letras e acentos são verificados automaticamente.\n')
        elif escolha == 'n':
            print('Pois bem, daremos inicio ao jogo\n')
        else:
            print('Não entendi, pode repetir?\n')

def resumoDaRodada(lista):
    print(lista)
    listaComQuantidades = retornaListaComQuantidadesDeElementosPresentes(lista)
    quantidadetotalDePartidas = len(lista)
    for i in range(len(listaComQuantidades)-1):
        porcentagem = (listaComQuantidades[i]/quantidadetotalDePartidas) * 100
        print(f'Terminou o jogo com {i+1} tentativas: {porcentagem} %. ')
    porcentagem = (listaComQuantidades[6]/quantidadetotalDePartidas) * 100
    print(f'Não acertou a palavra: {porcentagem} %. ')

def retornaListaComQuantidadesDeElementosPresentes(lista):
    listaComQuantidades = []
    for i in range(0, 7):
        listaComQuantidades.append(lista.count(i+1))
    return listaComQuantidades