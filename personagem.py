class Personagem(object): # Construtor superclasse
    def __init__(self, name, life, attack):
        self.name = name
        self.life = life
        self.attack = attack

class Inimigo(Personagem): # Construtor sub
    def __init__(self, name, life, attack):
        super().__init__(nome, vida, ataque)  # Chama o construtor da superclasse Personagem
        

# Exemplo de uso:
# meu_personagem = Personagem("Herói", 100, 20)
# inimigo = Inimigo("Inimigo 1", 50, 10, "Fácil")
