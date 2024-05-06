class Personagem(object): # Construtor superclasse
    def __init__(self, name, life, mana, attack):
        self.name = name
        self.life = life
        self.attack = attack
        self.mana = mana

class Inimigo(Personagem): # Construtor sub
    def __init__(self, name, life, attack):
        super().__init__(name, life, attack)  # Chama o construtor da superclasse Personagem
        

# Exemplo de uso:
# meu_personagem = Personagem("Herói", 100, 100, 20) -> Herói, 100hp, 100 mana, 20 atack
# inimigo = inimigo("Zequinha Dragão", 50, 100, 10)