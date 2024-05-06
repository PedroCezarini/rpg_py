class Personagem:
    def __init__(self, name, life, attack_type):
        self.name = name
        self.life = life
        self.attack_type = attack_type

def getAttack(self, n):
        if 0 <= n < len(self.attack_type):
            return f"Ataque {n + 1} - {self.attack_type[n]}, custo de mana."
        else:
            return "Ataque inválido."

class Mago(Personagem):
    def __init__(self, name):
        super().__init__(name, 70, ["Bola de fogo", "Espinho de gelo", "Missel arcano"])

class Guerreiro(Personagem):
    def __init__(self, name):
        super().__init__(name, 100, ["Golpe giratório", "Golpe perfurante", "Fura bucho"])

class Ladino(Personagem):
    def __init__(self, name):
        super().__init__(name, 80, ["Ataque das sombras", "Golpe fantasma", "Lâmina das trevas"])
        

class Inimigo(Personagem):
    def __init__(self, name, life): # Deve ser passado os pontos de ataque do inimigo?
        super().__init__(name, life, [])  # Chama o construtor da superclasse Personagem
        

# Exemplo de uso:
# meu_personagem = Personagem("Herói", 100, [])
# inimigo = Inimigo("Zequinha Dragão", 50)
