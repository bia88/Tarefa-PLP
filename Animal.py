class Animal:
    def move(self):
        pass  # método genérico

class Cachorro(Animal):
    def move(self):
        print("Correndo 🐕")

class Gato(Animal):
    def move(self):
        print("Saltando 🐈")

class Passaro(Animal):
    def move(self):
        print("Voando 🐦")

# Criando objetos
animais = [Cachorro(), Gato(), Passaro()]

# Chamando move() de forma polimórfica
for animal in animais:
    animal.move()
