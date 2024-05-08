#####BLOCO DE CREDITOS:



#####BLOCO DE IMPORTS

import random

#####BLOCO DE ARQUIVOS

with open('mapa2.txt', 'r') as f:
    big_mapa = [[int(num) for num in line.split()] for line in f]

f.close()

with open('blocos.txt', 'r') as f:
    blocos = [[ele for ele in line.split()] for line in f]

f.close()

#####MACRO BLOCO DE CLASSES

##CLASSES GRAFICAS

##CLASSES DE GAMEPLAY

#-classe player
class Player():
    pos_y=0
    pos_x=0
    def __init__(self, pos_y, pos_x):
        self.pos_y=pos_y
        self.pos_x=pos_x
    

#-funcao que anda pelo mapa
def mover(dire, p:Player, matriz):
    if matriz[p.pos_y+dire[0]][p.pos_x+dire[1]] != 1:
        p.pos_y+=dire[0]
        p.pos_x+=dire[1]
    else:
        print("não pode andar!")


#####MACRO BLOCO DE FUNCOES

##FUNCOES GRAFICAS

#-funcao que desenha cabecalho de menus
def cabecalho(tipo):

    cor = pega_cor(tipo)
        
    
    pinta("<-------------------------------->", cor, 0)
    print()

    if tipo=="mapa":
        print("|         MAPA MUNDI             |")
    if tipo=="combate":
        print("|         FIGHT!                 |")
              

    pinta("<-------------------------------->", cor, 0)
    pinta("",0,0)

#-funcao que desenha rodapes de menus  
def rodape(tipo):
    cor = pega_cor(tipo)
    pinta("<-------------------------------->\n", cor, 0)
    print("|         CONTROLES              |")
    print("|  a = esquerda    w = cima      |")
    print("|  s = baixo       d = direita   |")
    pinta("<-------------------------------->", cor, 0)

#-funcao que desenha o mapa e derivados
def map_print(mapa, p:Player):
    aux = 0
    for row in range(len(mapa)):
        pinta("|  ", 6, 8)
        for column in range(len(mapa[0])):
            if row == p.pos_y and column== p.pos_x:
                pinta("P",0,6)
            else:
                pinta( blocos[ mapa[row][column] ][1] ,int(blocos[mapa[row][column]][2]),int(blocos[mapa[row][column]][3]) )
            pinta("",0,0)

        pinta("  |", 6, 8)
        info_print(aux)
        aux+=1
        
        
        print()

 

#-funcao que desenha menus
def desenhar_menu(tipo, mapa, p:Player):
    cabecalho(tipo)

    pinta("",6,0)
    print()
    print(".", end="")
    for i in range(len(mapa[0])+4):
        print("-", end="")
    print(".", end="")
    print()

    map_print(mapa, p)

    
    
    print("'", end="")
    for i in range(len(mapa[0])+4):
        print("-", end="")
    print("'", end="")
    print()

    rodape(tipo)

#-funcao que desenha barras de vida
def display_barra(tipo, atual, total):
    if tipo =="HP":
        cor = 1
    else:
        cor = 4
    
    pinta("< {} :  {}/ {} \t> ||".format(tipo, atual, total), cor, -0)
    for hp in range(atual):
        pinta(" |", 0, cor)
    for hp in range(total-atual):
        pinta(" |", 0, 0)
    pinta("|", 0,0)

#-funcao de display lateral do mapa na tela mapa
def info_print(linha):
    match linha:
        case 0:
            print("\t<<CHAR INFO>>\t", end="")
        case 1:
            display_barra("HP", 40, 40)
        case 2:
            display_barra("MP", 10, 10)

#-funcao que retorna uma cor tematica para cada tipo de menu
def pega_cor(tipo):
    match tipo:
        case "mapa":
            return 6
        case "combate":
            return 1
        case "evento":
            return 3
        case _:
            print("avaliacao de cor inadequada")



##FUNCOES DE GAMEPLAY



##FUNCOES DE UTILIDADE PUBLICA

#-funcao que possibilita pintar caracteres e o fundo
def pinta(char, cor, fundo):
    print("\033[1;{};{}m{}".format(30+cor, 40+fundo, char), end="" )

#-print basicao de matrizes
def print_matrix(matriz):
    for i in range(len(matriz)):
        print("[", end="")
        for j in range(len(matriz[0])):
            print("{},".format(matriz[i][j]),end="")
        print("\b]")

#-funcao de obtencao de direcoes cardinais com base em wasd
def obter_dire(letra):
    match letra:
        case "a":
            return [0, -1 ]
        case "s":
            return [+1, 0]
        case "d":
            return [0, +1]
        case "w":
            return [-1, 0]
        case _:
            print("Inpute errado")


#####BLOCO GAMEPLAY LOOP

p = Player(1,1)
desenhar_menu("mapa", big_mapa, p)

    




########
    


for i in range(0,10):
    mover(obter_dire(input()), p, big_mapa)
    # print("{} - y {} - x".format(p.pos_y, p.pos_x))
    desenhar_menu("mapa", big_mapa, p)


