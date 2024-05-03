import random


class Fight(object):
  
  def vermelho(self):
    print("\033[1;31;0m ")

  def despintar(self):
    print("\033[0;0;0m ")


  

  print("\nVocê encontrou um inimigo\n")

    
  def enter(self):

    your_life = 20
    inimigo_life = 20
    inimigo = True
   

    while your_life > 0 and (inimigo):
      your_attack = random.randint(1,10)
      inimigo_attack = random.randint(1,10)

      attack = int(input("\n\nDigite 1 para atacar o inimigo 1, digite 0 para tentar fugir -> "))

      if attack < 0 or attack > 1:
        print('Valor inválido')
        return 0

      if attack == 0:
        print("Para a tentativa de fuga, será lançado um dado. Se o resultado for > 3, fuga bem sucedida, caso contrário seguirá para o ataque.")
        fuga = random.randint(1,6)
        if fuga > 3:
          print("Resultado do dado: %d\nFuga bem sucedida!!"  % fuga)
          return 0
        else:
          print("Resultado do dado: %d\nFuga falhou!!"  % fuga)
          attack = 2
      

      if attack == 1:
        if inimigo:
          inimigo_life = inimigo_life - your_attack
          print ("\nVocê causou %d de dano no inimigo." % your_attack)
          if inimigo_life <= 0:
            inimigo = False
            print ("Inimigo morreu!")
          else:
            print ("O inimigo ainda possui %d de vida" % inimigo_life)

        else:
          print ("inimigo já está morto!")
    

      if inimigo:
        your_life = your_life - inimigo_attack
        print ("\nO inimigo causou %d de dano em você, você ainda possui %d"
           " pontos de vida." %(inimigo_attack, your_life))
        if your_life <= 0:
          print ('Você morreu!!!')
          break
      

a_fight = Fight()
a_fight.enter()
