class Animal:
    def __init__(self, nome):
         self.nome = nome

    def falar(self):
        ...
class Cachorro(Animal):
    def falar(self):
        return f"{self.nome} emite latido!"
class Gato(Animal):
    def falar(self):
        return f"{self.nome} emite miau!"
    
huck = Cachorro("Huck")
fred = Gato("fred")

print(huck.falar())
print(fred.falar())
