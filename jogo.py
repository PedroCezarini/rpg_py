#####BLOCO DE CREDITOS:



#####BLOCO DE IMPORTS

import random

#####BLOCO DE ARQUIVOS

with open('mapa3.txt', 'r') as f:
    big_mapa = [[int(num) for num in line.split()] for line in f]

f.close()





with open('blocos.txt', 'r') as f:
    blocos = [[ele for ele in line.split()] for line in f]

f.close()

#####MACRO BLOCO DE CLASSES

##CLASSES GRAFICAS

##CLASSES DE GAMEPLAY

#-classe autoexplicativa
class SelecaoPersonagem:

    classe = 0

    def menu(self):

        with open('menu_principal.txt', 'r') as f:
            self.menu_principal = [[ele for ele in line.split()] for line in f]

        f.close()

        with open('menu_herois.txt', 'r') as f:
            self.menu_herois = [[ele for ele in line.split()] for line in f]

        f.close()
        pinta("", 3, 0)
        menus_em_geral(self.menu_principal)
        input()

        menus_em_geral(self.menu_herois)

    
        self.classe = int(input())

            #chamadas para começar a briga
        

#Classe principal da fight, onde a mágica acontece
class Fight:

    #função ilustrativa de status do personagem durante a luta (pode ser alterado para status dinamicos)
    def mostrar_status(self, vida, energia):
        print('\n')
        print('----- Seu Status -----')
        print("Vida: %d" % vida)
        print("Energia: %d" % energia)
        print('----------------------')
        print('\n')
    
    #função ilustrativa de vida do inimigo para início da luta (aparece somente quando enconstra inimigo)
    def inimigo_status(self, vida):
        print('\n')
        print('----- Status do Inimigo -----')
        print("Vida: %d" % vida)
        print('-----------------------------')
        print('\n')

    #Função para escolha de ataque
    def opcoes(self, poder1, poder2, poder3):
        print("\nDigite 1 para usar %s - 0 de mana" % poder1)
        print("Digite 2 para usar %s - 4 de mana" % poder2)
        print('Digite 3 para usar %s - 6 de mana' % poder3)

    #Função com todo o codigo procedural da luta, onde realmente a mágica acontece
    def enter(self, escolha:int):

        pinta("\n\n",1,0)
        #sets que dependem de uma variável global definida no menu de personagems
        if escolha == 1:  # set do personagem mago
            personagem = Personagem("Magnus, o Mago", 70, 100, "Bola de fogo", "Espinho de gelo", "Míssel Arcano")
        elif escolha == 2:  # set do personagem guerreiro
            personagem = Personagem("Absalom, o Cavalheiro", 100, 50, "Golpe giratório", "Golpe perfurante", "Rasga bucho")
        elif escolha == 3:  # set do personagem Ladino
            personagem = Personagem("Febror, o Ladino", 80, 60, "Ataque das sombras", "Golpe fantasma", "Lâmina das trevas")

        

        #sets que dependem de uma variável global na escolha de inimigo
        if y == 1: # set do inimigo "cobrinha"
            inimigo = Inimigo("Cobrinha", 60,"                                                 \n                       .....-==:.     .          \n                      .-+***#%##**++++:          \n                   .-=*#**%%##*#*+*+##*:         \n                  .**#**#%%#%%##**++++*#####*+:  \n                  ###******#*+*#*+=***++###*-.   \n         .-=-.    .==: .-+####%%%###+++++##*:    \n        ..      .  :-:  .=##%%%#=%%%#***+*###+:  \n        :               .+%%=.    *%##*+=**#=    \n         :.           .=#*=.       +%##*++*%#.   \n          .::      .:+=.    .::..  -%#*****#%=   \n             .:---:..  :*########+:*##*+**#%%:   \n                   .:=###***#***##%%#*++*##%*    \n                 :=*%%#**#%#*+*#%%#*****##%%-    \n                  -####*#%#*******+*++**##%+.    \n     .:.        -#######%%##***+**+****###=      \n  .-+.          :###*#%%%%%###*******###%=.      \n .=+.          .+#####%%%%%%#########%#=:        \n.=*:           .*%####%%@%.+%%%%%%%%*.           \n.**.           :#%##%%%%%-    .--:.              \n.*#:           .*%%%%%%%%%-:-==--::.             \n.##+           .*%#*****++*++****###**=.         \n =###.       .+##*+**+**+++***#*#***###%#:       \n .=###+-.  .*%####*##**#*###########%%%%%*.      \n   :*%###%%%%%#########%%%%%%%%%%%%%%%%%%*.      \n     .+%%%%%%#%%%%%%%%%%%%@@@@@%%%%@@@@@%+       \n        .:#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%=.       \n           :#%@@%%%%%%%##*#**##****#****###+-    \n             .*%%%%%%%#####*###***##*###%##%%*.  \n           :. #%%%%%%%%%%%#%%%####%##%%%%#%%%#:  \n            =.+%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#:  \n          .--#+*%%%%%%%%%%%%%%%%%%%%%%%%%%%%#::  \n            .:..  ..:-*#%%%%%#*=---:.=*++#%*-    \n                                 .-=-:.....      \n" )
        elif y == 2: # set do inimigo "ogro"
            inimigo = Inimigo("Ogro", 80,"                                          \n                                                 \n   .--::.   +=+=#==##%#+**+#++*-..               \n  -*+**##   .##*#%%#*##%%+++*#**%@*              \n  +#****#  .==#%%@@%##@%#+*%#++++*@%.            \n :+*#***#: =%%+***#%@%%%#*#*=++****+++           \n  -%%#####+-*#%#%+**#%%%*%@%**##*+**##*:         \n   :@%%%@@:  %%+++*%%@@#@%##@@%**+*##+*%#        \n    =%%%@:   .%@%%@@@@@#++**%@@@%%%@#*#@@:       \n     :##%*    -**%%%%@@%#%%%%%@@@@@@#%@@@:       \n      +%#@-..==*#%@@@@@@@@@@@@@@@@@+:*#%.        \n     :***+**-:=***%@%*+**=**%%%%@@@*#%%:         \n     .+#@@@@###%@@@@%%#**#@@%#%@#+++*#@:         \n      :*%@@*=-+%%%@#**####=+%%%@%*##*%@=         \n        -#=    .++*%%##+=+#%@%*#%@@@@@%%         \n              -*++++*%@%##@%*+*++#@@%=-.         \n             =**#***%@@@@#@@#*+*#%@@%.           \n             =%%@%%@@@@*  .:#@**#@@%@*.          \n            .%*+##**%@@+    -##@@#++@@*.         \n              --:*@@%###:    -+#*%@@@%@%.        \n                 -*%####%:       .#@@@@%+        \n              .=#****#@%@#*******##**#*%@=       \n             =#############@@@@@%%%%%%%%@#.      \n")

        # definição de atributos do personagem selecionado em variáveis locais para funcionar no codigo
        your_life = personagem.getLife()
        your_energy = personagem.getMana()
        habilidade1 = personagem.getHab1()
        habilidade2 = personagem.getHab2()
        habilidade3 = personagem.getHab3()

        # definição de atributos do inimigo selecionado em variáveis locais para funcionar no codigo
        inimigo_life = inimigo.getVida()
        inimigo_name = inimigo.getNome()
        inimigo_aparencia = inimigo.getAparencia()
        inimigo = True

        # cena de aparencia do inimigo ao encontra-lo
        print("Voce encontrou %s" % inimigo_name)
        print("%s" % inimigo_aparencia)
        self.inimigo_status(inimigo_life)

        # loop da briga toda
        while your_life > 0 and (inimigo):

            #Rolagem de dados para definir o dano na atual passagem do loop
            your_attack = random.randint(1, 10)
            ataque_pesado = random.randint(5, 15)
            ataque_especial = random.randint(10, 20)
            inimigo_attack = random.randint(1, 10)

            # chamada das opções de habilidades junto com um input
            self.opcoes(habilidade1, habilidade2, habilidade3)
            attack = int(input("Digite 0 para tentar fugir -> "))

            # opção invalida encerra o código
            if attack < 0 or attack > 3:
                print('Valor inválido')
                return 0

            # fuga
            if attack == 0:
                print("Para a tentativa de fuga, será lançado um dado. Se o resultado for maior 3, fuga bem sucedida, caso contrário seguirá para o ataque.")
                fuga = random.randint(1, 6)
                if fuga > 3:
                    print("Resultado do dado: %d\nFuga bem sucedida!!" % fuga)
                    return 0
                else:
                    print("Resultado do dado: %d\nFuga falhou!!" % fuga)
                    attack = 4

            # ataque 1
            if attack == 1:
                if inimigo:
                    inimigo_life = inimigo_life - your_attack
                    print("\nVocê utilizou %s!!" % habilidade1 )
                    print("Inimigo sofreu %d de dano." % your_attack)
                    if inimigo_life <= 0:
                        inimigo = False
                        print("Inimigo morreu!")
                    else:
                        print("O inimigo ainda possui %d de vida" % inimigo_life)

            # ataque 2
            if attack == 2:
                if inimigo:
                    if your_energy >= 4:
                        inimigo_life = inimigo_life - ataque_pesado
                        print("\nVocê utilizou %s!!" % habilidade2)
                        print("Inimigo sofreu %d de dano." % ataque_pesado)
                        your_energy = your_energy - 4
                        if inimigo_life <= 0:
                            inimigo_life = 0
                            inimigo = False
                            print("Inimigo morreu!")
                        else:
                            print("O inimigo ainda possui %d de vida" % inimigo_life)
                    else:
                        print('Você não possui mana suficiente')

            # ataque 3
            if attack == 3:
                if inimigo:
                    if your_energy >= 6:
                        inimigo_life = inimigo_life - ataque_especial
                        print("\nVocê utilizou %s!!" % habilidade3)
                        print("Inimigo sofreu %d de dano." % ataque_especial)
                        your_energy = your_energy - 6
                        if inimigo_life <= 0:
                            inimigo = False
                            print("Inimigo morreu!")
                        else:
                            print("O inimigo ainda possui %d de vida" % inimigo_life)
                    else:
                        print('Você não possui mana suficiente')

            # ataque do inimigo
            if inimigo:
                your_life = your_life - inimigo_attack
                print("\nO inimigo causou %d de dano em você, você ainda possui %d pontos de vida." % (inimigo_attack, your_life))
                if your_life <= 0:
                    print('Você morreu!!!')
                    break

            #mostra seus status ao final dos ataques e recomeça o loop
            self.mostrar_status(your_life, your_energy)



#-classe player
class Player():
    pos_y=0
    pos_x=0
    def __init__(self, pos_y, pos_x):
        self.pos_y=pos_y
        self.pos_x=pos_x


        
#classe construtora de personagem
class Personagem:
    def __init__(self, name, life, mana, hab1, hab2, hab3):
        self.name = name
        self.life = life
        self.mana = mana
        self.hab1 = hab1
        self.hab2 = hab2
        self.hab3 = hab3

    #funções para retornar posteriormente valores personagem
    def getName(self):
        return self.name

    def getLife(self):
        return self.life

    def getMana(self):
        return self.mana
    
    def getHab1(self):
        return self.hab1
    
    def getHab2(self):
        return self.hab2
    
    def getHab3(self):
        return self.hab3


#classe construtora de inimido
class Inimigo:
    def __init__(self, nome, vida, aparencia):
        self.nome = nome
        self.vida = vida
        self.aparencia = aparencia

    #funções para retornar informações posteriormente 
    def getNome(self):
        return self.nome

    def getVida(self):
        return self.vida

    def getAparencia(self):
        return self.aparencia

    

#-funcao que anda pelo mapa
def mover(dire, p:Player, matriz):
    if matriz[p.pos_y+dire[0]][p.pos_x+dire[1]] != 1:
        p.pos_y+=dire[0]
        p.pos_x+=dire[1]
    else:
        print("não pode andar!")


#####MACRO BLOCO DE FUNCOES

##FUNCOES GRAFICAS

def menus_em_geral(menu):
    for i in range(len(menu)):
        for l in range(len(menu[i])):
            print(menu[i][l], end=" ")
        
        pinta("\n", 3, 0)
        

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

        
#-funcao que verifica se o espaco precisa de um salve:
def verifica_pos(p:Player, per:SelecaoPersonagem):
    if p.pos_y==11  and p.pos_x==9:
        a_fight = Fight()
        a_fight.enter(per.classe)

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


############################################################################################
############################################################################################
############################################################################################
#####BLOCO GAMEPLAY LOOP

x = 0
y = int(input("Inimigo:"))

per = SelecaoPersonagem
per.menu(per)

p = Player(1,1)
desenhar_menu("mapa", big_mapa, p)

    




########
    


for i in range(0,99):

    verifica_pos(p, per)
    mover(obter_dire(input()), p, big_mapa)
    # print("{} - y {} - x".format(p.pos_y, p.pos_x))
    desenhar_menu("mapa", big_mapa, p)


##########codigos que ainda não foram colocados no seu lugar:
##########################################################################################
##########################################################################################
##########################################################################################






    

