class Personagem:
    def __init__(self, name, life, mana):
        self.name = name
        self.life = life
        self.mana = mana
      
        # Método para mudar os atributos do mago
    def setMago(self,new_name="Magnus,o Mago",new_life=70,new_mana=100):
        self.name=new_name
        self.life=new_life
        self.mana=new_mana
        self.a1="Bola de fogo"
        self.a2="Espinho de gelo"
        self.a3="Missel arcano"

    def getLifeMago(self):
        return self.life
        
    def getNameMago(self):
        return self.name
        
    def getManaMago(self):
        return self.mana
        
    def getHab1Mago(self):
        return self.a1
        
    def getHab2Mago(self):
        return self.a1
    
    def getHab3Mago(self):
        return self.a1

        # Método para mudar os atributos do guerreiro
    def setGuerreiro(self,new_name="Absalom,o Barbaro",new_life=100,new_mana=50):
        self.name=new_name
        self.life=new_life
        self.mana=new_mana
        self.a1="Golpe giratório"
        self.a2="Golpe perfurante"
        self.a3="Rasga bucho"

    def getLifeGuerreiro(self):
        return self.life
    
    def getNameGuerreiro(self):
        return self.name
    
    def getManaGuerreiro(self):
        return self.mana
    
    def getHab1Guerreiro(self):
        return self.a1
    
    def getHab2Guerreiro(self):
        return self.a1
    
    def getHab3Guerreiro(self):
        return self.a1

        # Método para mudar os atributos do ladino
    def setLadino(self,new_name="Febror, o Ladino",new_life=80,new_mana=60):
        self.name=new_name
        self.life=new_life
        self.mana=new_mana
        self.a1="Ataque das sombras"
        self.a2="Golpe fantasma"
        self.a3="Lâmina das trevas"

    def getLifeLadino(self):
        return self.life
    
    def getNameLadino(self):
        return self.name
    
    def getManaLadino(self):
        return self.mana
    
    def getHab1Ladino(self):
        return self.a1
    
    def getHab2Ladino(self):
        return self.a1
    
    def getHab3Ladino(self):
        return self.a1
