import random

x = int(input("Selecione o personagem (1 para Mago, 2 para Guerreiro, 3 para Ladino): "))
y = int(input("Inimigo:"))

class Inimigo:
    def __init__(self, nome, vida, aparencia):
        self.nome = nome
        self.vida = vida
        self.aparencia = aparencia

    def getNome(self):
        return self.nome

    def getVida(self):
        return self.vida

    def getAparencia(self):
        return self.aparencia
    
        

class Personagem:
    def __init__(self, name, life, mana, hab1, hab2, hab3):
        self.name = name
        self.life = life
        self.mana = mana
        self.hab1 = hab1
        self.hab2 = hab2
        self.hab3 = hab3

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

class Fight:
    def mostrar_status(self, vida, energia):
        print('\n')
        print('----- Seu Status -----')
        print("Vida: %d" % vida)
        print("Energia: %d" % energia)
        print('----------------------')
        print('\n')

    def inimigo_status(self, vida):
        print('\n')
        print('----- Status do Inimigo -----')
        print("Vida: %d" % vida)
        print('-----------------------------')
        print('\n')

    def entrada(self):
        print("\n!!Você encontrou um inimigo!!\n")
        # desenho inimigo
        print("                                                 \n                       .....-==:.     .          \n                      .-+***#%##**++++:          \n                   .-=*#**%%##*#*+*+##*:         \n                  .**#**#%%#%%##**++++*#####*+:  \n                  ###******#*+*#*+=***++###*-.   \n         .-=-.    .==: .-+####%%%###+++++##*:    \n        ..      .  :-:  .=##%%%#=%%%#***+*###+:  \n        :               .+%%=.    *%##*+=**#=    \n         :.           .=#*=.       +%##*++*%#.   \n          .::      .:+=.    .::..  -%#*****#%=   \n             .:---:..  :*########+:*##*+**#%%:   \n                   .:=###***#***##%%#*++*##%*    \n                 :=*%%#**#%#*+*#%%#*****##%%-    \n                  -####*#%#*******+*++**##%+.    \n     .:.        -#######%%##***+**+****###=      \n  .-+.          :###*#%%%%%###*******###%=.      \n .=+.          .+#####%%%%%%#########%#=:        \n.=*:           .*%####%%@%.+%%%%%%%%*.           \n.**.           :#%##%%%%%-    .--:.              \n.*#:           .*%%%%%%%%%-:-==--::.             \n.##+           .*%#*****++*++****###**=.         \n =###.       .+##*+**+**+++***#*#***###%#:       \n .=###+-.  .*%####*##**#*###########%%%%%*.      \n   :*%###%%%%%#########%%%%%%%%%%%%%%%%%%*.      \n     .+%%%%%%#%%%%%%%%%%%%@@@@@%%%%@@@@@%+       \n        .:#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%=.       \n           :#%@@%%%%%%%##*#**##****#****###+-    \n             .*%%%%%%%#####*###***##*###%##%%*.  \n           :. #%%%%%%%%%%%#%%%####%##%%%%#%%%#:  \n            =.+%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#:  \n          .--#+*%%%%%%%%%%%%%%%%%%%%%%%%%%%%#::  \n            .:..  ..:-*#%%%%%#*=---:.=*++#%*-    \n                                 .-=-:.....      \n")

    def opcoes(self, poder1, poder2, poder3):
        print("\nDigite 1 para usar %s - 0 de mana" % poder1)
        print("Digite 2 para usar %s - 4 de mana" % poder2)
        print('Digite 3 para usar %s - 6 de mana' % poder3)

    def enter(self):
        if x == 1:  # mago
            personagem = Personagem("Magnus, o Mago", 70, 100, "Bola de fogo", "Espinho de gelo", "Míssel Arcano")
        elif x == 2:  # guerreiro
            personagem = Personagem("Absalom, o Bárbaro", 100, 50, "Golpe giratório", "Golpe perfurante", "Rasga bucho")
        elif x == 3:  # Ladino
            personagem = Personagem("Febror, o Ladino", 80, 60, "Ataque das sombras", "Golpe fantasma", "Lâmina das trevas")

        if y == 1:
            inimigo = Inimigo("Cobrinha", 60,"                                                 \n                       .....-==:.     .          \n                      .-+***#%##**++++:          \n                   .-=*#**%%##*#*+*+##*:         \n                  .**#**#%%#%%##**++++*#####*+:  \n                  ###******#*+*#*+=***++###*-.   \n         .-=-.    .==: .-+####%%%###+++++##*:    \n        ..      .  :-:  .=##%%%#=%%%#***+*###+:  \n        :               .+%%=.    *%##*+=**#=    \n         :.           .=#*=.       +%##*++*%#.   \n          .::      .:+=.    .::..  -%#*****#%=   \n             .:---:..  :*########+:*##*+**#%%:   \n                   .:=###***#***##%%#*++*##%*    \n                 :=*%%#**#%#*+*#%%#*****##%%-    \n                  -####*#%#*******+*++**##%+.    \n     .:.        -#######%%##***+**+****###=      \n  .-+.          :###*#%%%%%###*******###%=.      \n .=+.          .+#####%%%%%%#########%#=:        \n.=*:           .*%####%%@%.+%%%%%%%%*.           \n.**.           :#%##%%%%%-    .--:.              \n.*#:           .*%%%%%%%%%-:-==--::.             \n.##+           .*%#*****++*++****###**=.         \n =###.       .+##*+**+**+++***#*#***###%#:       \n .=###+-.  .*%####*##**#*###########%%%%%*.      \n   :*%###%%%%%#########%%%%%%%%%%%%%%%%%%*.      \n     .+%%%%%%#%%%%%%%%%%%%@@@@@%%%%@@@@@%+       \n        .:#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%=.       \n           :#%@@%%%%%%%##*#**##****#****###+-    \n             .*%%%%%%%#####*###***##*###%##%%*.  \n           :. #%%%%%%%%%%%#%%%####%##%%%%#%%%#:  \n            =.+%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#:  \n          .--#+*%%%%%%%%%%%%%%%%%%%%%%%%%%%%#::  \n            .:..  ..:-*#%%%%%#*=---:.=*++#%*-    \n                                 .-=-:.....      \n" )
        elif y == 2:
            inimigo = Inimigo("Ogro", 80,"                                          \n                                                 \n   .--::.   +=+=#==##%#+**+#++*-..               \n  -*+**##   .##*#%%#*##%%+++*#**%@*              \n  +#****#  .==#%%@@%##@%#+*%#++++*@%.            \n :+*#***#: =%%+***#%@%%%#*#*=++****+++           \n  -%%#####+-*#%#%+**#%%%*%@%**##*+**##*:         \n   :@%%%@@:  %%+++*%%@@#@%##@@%**+*##+*%#        \n    =%%%@:   .%@%%@@@@@#++**%@@@%%%@#*#@@:       \n     :##%*    -**%%%%@@%#%%%%%@@@@@@#%@@@:       \n      +%#@-..==*#%@@@@@@@@@@@@@@@@@+:*#%.        \n     :***+**-:=***%@%*+**=**%%%%@@@*#%%:         \n     .+#@@@@###%@@@@%%#**#@@%#%@#+++*#@:         \n      :*%@@*=-+%%%@#**####=+%%%@%*##*%@=         \n        -#=    .++*%%##+=+#%@%*#%@@@@@%%         \n              -*++++*%@%##@%*+*++#@@%=-.         \n             =**#***%@@@@#@@#*+*#%@@%.           \n             =%%@%%@@@@*  .:#@**#@@%@*.          \n            .%*+##**%@@+    -##@@#++@@*.         \n              --:*@@%###:    -+#*%@@@%@%.        \n                 -*%####%:       .#@@@@%+        \n              .=#****#@%@#*******##**#*%@=       \n             =#############@@@@@%%%%%%%%@#.      \n")

        your_life = personagem.getLife()
        your_energy = personagem.getMana()
        habilidade1 = personagem.getHab1()
        habilidade2 = personagem.getHab2()
        habilidade3 = personagem.getHab3()


        inimigo_life = inimigo.getVida()
        inimigo_name = inimigo.getNome()
        inimigo_aparencia = inimigo.getAparencia()
        inimigo = True

        print("Voce encontrou %s" % inimigo_name)
        print("%s" % inimigo_aparencia)
        self.inimigo_status(inimigo_life)

        while your_life > 0 and (inimigo):
            your_attack = random.randint(1, 10)
            ataque_pesado = random.randint(5, 15)
            ataque_especial = random.randint(10, 20)
            inimigo_attack = random.randint(1, 10)

            self.opcoes(habilidade1, habilidade2, habilidade3)
            attack = int(input("Digite 0 para tentar fugir -> "))

            # digito errado
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

            # ataque comum
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

            # ataque pesado
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

            # ataque especial
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

            self.mostrar_status(your_life, your_energy)

    

a_fight = Fight()
a_fight.enter()

        
