class Aluno:
    def __init__(self, nome="", nota1=0.0, nota2=0.0):
        self.__nome = nome
        self.__nota1 = nota1
        self.__nota2 = nota2

    def set_nome(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome

    def set_nota1(self, nota1):
        self.__nota1 = nota1

    def get_nota1(self):
        return self.__nota1

    def set_nota2(self, nota2):
        self.__nota2 = nota2

    def get_nota2(self):
        return self.__nota2

    def calcular_media(self):
        return (self.__nota1 + self.__nota2) / 2
    
    def exibir_nome_e_media(self):
        media = self.calcular_media()
        return f"Nome: {self.__nome}, Média: {media:.2f}"

aluno = Aluno("Alexandre Barreto", 7.5, 8.0)
print(aluno.exibir_nome_e_media())

aluno.set_nota1(9.0)
aluno.set_nota2(8.5)
print(aluno.exibir_nome_e_media())
