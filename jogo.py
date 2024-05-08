def pinta(char, cor, fundo):
    print("\033[1;{};{}m{}".format(30+cor, 40+fundo, char), end="" )

import random

with open('mapa2.txt', 'r') as f:
    l = [[int(num) for num in line.split()] for line in f]
print(l)
f.close()

with open('blocos.txt', 'r') as f:
    blocos = [[ele for ele in line.split()] for line in f]
print(blocos)
f.close()


for row in range(10):
    for column in range(18):
        
        pinta( blocos[ l[row][column] ][1] ,int(blocos[l[row][column]][2]),int(blocos[l[row][column]][3]) )
        
    
    print()


def desenhar_menu(tipo, mapa, alt, lat):
    cabecalho(tipo)

    pinta("",6,0)
    print()
    print(".", end="")
    for i in range(lat+4):
        print("-", end="")
    print(".", end="")
    print()

    map_print(alt, lat, mapa)

    
    
    print("'", end="")
    for i in range(lat+4):
        print("-", end="")
    print("'", end="")
    print()

    rodape(tipo)
    
    
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

    
def info_print(linha):
    match linha:
        case 0:
            print("\t<<CHAR INFO>>\t", end="")
        case 1:
            display_barra("HP", 40, 40)
        case 2:
            display_barra("MP", 10, 10)
        
def map_print(alt, lat, mapa):
    aux = 0
    for row in range(alt):
        pinta("|  ", 6, 8)
        for column in range(lat):
            
            
            pinta( blocos[ mapa[row][column] ][1] ,int(blocos[mapa[row][column]][2]),int(blocos[mapa[row][column]][3]) )
            pinta("",0,0)

        pinta("  |", 6, 8)
        info_print(aux)
        aux+=1
        
        
        print()


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
    
def rodape(tipo):
    cor = pega_cor(tipo)
    pinta("<-------------------------------->\n", cor, 0)
    print("|         CONTROLES              |")
    print("|  a = esquerda    w = cima      |")
    print("|  s = baixo       d = direita   |")
    pinta("<-------------------------------->", cor, 0)

desenhar_menu("mapa", l, 10, 10)

# def encontra_jogador(matriz_mapa):
#     for i in range(len(matriz_mapa)):
        
#         for j in range(len(matriz_mapa[0])):
#             #print(matriz_mapa[i][j])
#             if matriz_mapa[i][j]==11:
#                 print("achei miseravel")
#                 return i, j

# class player:
#     pos_x, pos_y = encontra_jogador(l)
    

# jose = player()


# print(jose.pos_y, jose.pos_x)

matriz= [[1, 1, 1, 1, 1],
         [1, 0, 0, 0, 1],
         [1, 0, 2, 0, 1],
         [1, 0, 0, 0, 1],
         [1, 1, 1, 1, 1]]

matriz_cp = matriz.copy()
print_matrix(matriz_cp)

def removedor_de_player(matriz_original):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == 2:
                matriz[i][j]=0

removedor_de_player(matriz)
print_matrix(matriz)

def print_matrix(matriz):
    for i in range(len(matriz)):
        print("[", end="")
        for j in range(len(matriz)):
            print("{},\t".format(matriz[i][j]),end="")
        print("\b\b]")

def obter_dire(letra):
    match letra:
        case "a":
            return 0, -1 
        case "s":
            return +1, 0
        case "d":
            return 0, +1
        case "w":
            return -1, 0
        case _:
            print("Inpute errado")

def mover(dire, pos_x, pos_y, matriz, matriz_nova):
    if matriz[pos_y+dire[0]][pos_x+dire[1]] != 1:
        matriz_nova[pos_y+dire[0]][pos_x+dire[1]] = 2
        matriz_nova[pos_y][pos_x]= matriz[pos_y][pos_x]

        
    else:
        print("não pode andar!")
    
    
    
