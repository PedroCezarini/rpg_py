class Personagem:
    def __init__(self, name, life, mana):
        self.name = name
        self.life = life
        self.mana = mana
      
        # Método para mudar os atributos
        
    def setMago(self,new_name="Magnus,o Mago",new_life=70,new_mana=100):
        self.name=new_name
        self.life=new_life
        self.mana=new_mana
        self.a1="Bola de fogo"
        self.a2="Espinho de gelo"
        self.a3="Missel arcano"


    def setGuerreiro(self,new_name="Absalom,o Barbaro",new_life=100,new_mana=50):
        self.name=new_name
        self.life=new_life
        self.mana=new_mana
        self.a1="Golpe giratório"
        self.a2="Golpe perfurante"
        self.a3="Rasga bucho"

    def setLadino(self,new_name="Febror, o Ladino",new_life=80,new_mana=60):
        self.name=new_name
        self.life=new_life
        self.mana=new_mana
        self.a1="Ataque das sombras"
        self.a2="Golpe fantasma"
        self.a3="Lâmina das trevas"
