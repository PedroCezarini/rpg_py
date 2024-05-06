class Personagem(object): # Construtor superclasse
    def __init__(self, name, life, attack):
        self.name = name
        self.life = life
        self.attack = attack

class Inimigo(Personagem): # Construtor sub
    def __init__(self, name, life, attack):
        super().__init__(name, life, attack)  # Chama o construtor da superclasse Personagem
        

# Exemplo de uso:
# meu_personagem = Personagem("Herói", 100, 20)
# inimigo = inimigo("Zequinha Dragão", 50, 10)
