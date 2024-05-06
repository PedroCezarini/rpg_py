class Personagem(object): # Construtor superclasse
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

class Inimigo(Personagem): # Construtor sub
    def __init__(self, nome, vida, ataque, dificuldade):
        super().__init__(nome, vida, ataque)  # Chama o construtor da superclasse Personagem
        self.dificuldade = dificuldade

# Exemplo de uso:
# meu_personagem = Personagem("Herói", 100, 20)
# inimigo = Inimigo("Inimigo 1", 50, 10, "Fácil")
