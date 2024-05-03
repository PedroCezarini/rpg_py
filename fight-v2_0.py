import random


class Fight(object):
  
  def mostrar_status(self, vida, energia):
    print("Vida: %d" % vida)
    print("Energia: %d" % energia)

  

  print("\n!!Você encontrou um inimigo!!\n")
  #desenho inimigo
  print("                                                 \n                       .....-==:.     .          \n                      .-+***#%##**++++:          \n                   .-=*#**%%##*#*+*+##*:         \n                  .**#**#%%#%%##**++++*#####*+:  \n                  ###******#*+*#*+=***++###*-.   \n         .-=-.    .==: .-+####%%%###+++++##*:    \n        ..      .  :-:  .=##%%%#=%%%#***+*###+:  \n        :               .+%%=.    *%##*+=**#=    \n         :.           .=#*=.       +%##*++*%#.   \n          .::      .:+=.    .::..  -%#*****#%=   \n             .:---:..  :*########+:*##*+**#%%:   \n                   .:=###***#***##%%#*++*##%*    \n                 :=*%%#**#%#*+*#%%#*****##%%-    \n                  -####*#%#*******+*++**##%+.    \n     .:.        -#######%%##***+**+****###=      \n  .-+.          :###*#%%%%%###*******###%=.      \n .=+.          .+#####%%%%%%#########%#=:        \n.=*:           .*%####%%@%.+%%%%%%%%*.           \n.**.           :#%##%%%%%-    .--:.              \n.*#:           .*%%%%%%%%%-:-==--::.             \n.##+           .*%#*****++*++****###**=.         \n =###.       .+##*+**+**+++***#*#***###%#:       \n .=###+-.  .*%####*##**#*###########%%%%%*.      \n   :*%###%%%%%#########%%%%%%%%%%%%%%%%%%*.      \n     .+%%%%%%#%%%%%%%%%%%%@@@@@%%%%@@@@@%+       \n        .:#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%=.       \n           :#%@@%%%%%%%##*#**##****#****###+-    \n             .*%%%%%%%#####*###***##*###%##%%*.  \n           :. #%%%%%%%%%%%#%%%####%##%%%%#%%%#:  \n            =.+%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#:  \n          .--#+*%%%%%%%%%%%%%%%%%%%%%%%%%%%%#::  \n            .:..  ..:-*#%%%%%#*=---:.=*++#%*-    \n                                 .-=-:.....      \n")
  print("\n\n\n")
   
  def enter(self):

    your_life = 40
    your_energy = 15
    inimigo_life = 40
    inimigo = True
   

    while your_life > 0 and (inimigo):
      your_attack = random.randint(1,5)
      ataque_pesado = random.randint(5,7)
      ataque_especial = random.randint(7,10)
      inimigo_attack = random.randint(1,10)

      a_fight.mostrar_status(your_life,your_energy)
      print("\nDigite 1 para ataque básico - 0 de mana")
      print("Digite 2 para ataque pesado - 4 mana")
      print('Digite 3 para Investida - 6 de mana')
      attack = int(input("Digite 0 para tentar fugir -> "))

      #digito errado
      if attack < 0 or attack > 3:
        print('Valor inválido')
        return 0

      #fuga
      if attack == 0:
        print("Para a tentativa de fuga, será lançado um dado. Se o resultado for > 3, fuga bem sucedida, caso contrário seguirá para o ataque.")
        fuga = random.randint(1,6)
        if fuga > 3:
          print("Resultado do dado: %d\nFuga bem sucedida!!"  % fuga)
          return 0
        else:
          print("Resultado do dado: %d\nFuga falhou!!"  % fuga)
          attack = 4
      
      #ataque comum
      if attack == 1:
        if inimigo:
          inimigo_life = inimigo_life - your_attack
          print ("\nVocê causou %d de dano no inimigo." % your_attack)
          if inimigo_life <= 0:
            inimigo = False
            print ("Inimigo morreu!")
          else:
            print ("O inimigo ainda possui %d de vida" % inimigo_life)


    
      #ataque pesado
      if attack == 2:
          if inimigo:
            if your_energy >= 4:
              inimigo_life = inimigo_life - ataque_pesado
              print ("\nVocê causou %d de dano no inimigo." % ataque_pesado)
              your_energy = your_energy - 4
              if inimigo_life <= 0:
                inimigo_life = 0
                inimigo = False
                print ("Inimigo morreu!")
              else:
                print ("O inimigo ainda possui %d de vida" % inimigo_life)
            else:
              print('Você não possui mana suficiente')


      #ataque especial
      if attack == 3:
        if inimigo:
          if your_energy >= 6:            
            inimigo_life = inimigo_life - ataque_especial
            print ("\nVocê causou %d de dano no inimigo." % ataque_especial)
            your_energy = your_energy - 6
            if inimigo_life <= 0:
              inimigo = False
              print ("Inimigo morreu!")
            else:
              print ("O inimigo ainda possui %d de vida" % inimigo_life)
          else:
            print('Você não possui mana suficiente')
    

      #ataque do inimigo
      if inimigo:
        your_life = your_life - inimigo_attack
        print ("\nO inimigo causou %d de dano em você, você ainda possui %d"
           " pontos de vida." %(inimigo_attack, your_life))
        if your_life <= 0:
          print ('Você morreu!!!')
          break
      

a_fight = Fight()
a_fight.enter()
