class Cão:
    especie = "Canis Famliaris"

    def __init__(self, nome, raça):
        self.nome = nome
        self.raça = raça

        def bark(self):
            return f"{self.nome} latiu."


meu_cao = Cão("Luke", "Vira-lata")
seu_cao = Cão("Bola", "Caramelo")
cao_vizinho = Cão("Pit", "Chihuahua")
cao_vizinha = Cão("Mika", "Golden Retriever")
saudades = Cão("Tuti", "Poodle")


print(f"A nome do meu cachorro é {meu_cao.nome}, e sua raça é um {meu_cao.raça}")
print(f"A nome do seu cachorro é {seu_cao.nome}, e sua raça é um {seu_cao.raça}")
print(f"A nome do cachorro do vizinho é {cao_vizinho.nome}, e sua raça é um {cao_vizinho.raça}")
print(f"e a da vizinha é {cao_vizinha.nome}, e sua raça é um {cao_vizinha.raça}")
print(f"Eu tive um cachorro chamado {saudades.nome}, e sua raça era um {saudades.raça}")