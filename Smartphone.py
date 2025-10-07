# Classe base
class Smartphone:
    def __init__(self, marca, modelo, bateria):
        self.marca = marca
        self.modelo = modelo
        self.__bateria = bateria  # atributo encapsulado (privado)

    def ligar(self):
        print(f"{self.marca} {self.modelo} está ligado!")

    def mostrar_bateria(self):
        print(f"Nível de bateria: {self.__bateria}%")

    def carregar(self, quantidade):
        self.__bateria += quantidade
        if self.__bateria > 100:
            self.__bateria = 100
        print(f"Bateria carregada para {self.__bateria}%")

# Subclasse com herança
class SmartphoneAvancado(Smartphone):
    def tirar_foto(self):
        print(f"{self.marca} {self.modelo} tirou uma foto incrível!")

# Criando objetos
s1 = Smartphone("Samsung", "A52", 50)
s1.ligar()
s1.mostrar_bateria()
s1.carregar(30)

s2 = SmartphoneAvancado("iPhone", "14 Pro", 80)
s2.ligar()
s2.tirar_foto()
s2.mostrar_bateria()
