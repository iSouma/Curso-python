# Criar um escritor, uma caneta e uma máquina de escrever. Cada um terá uma classe diferente e elas terão que se
# relacionar.


class Escritor:
    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = None

    @property
    def nome(self):
        return self.__nome

    @property
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta


class Caneta:
    def __init__(self, cor):
        self.__cor = cor

    @property
    def cor(self):
        return self.__cor

    def escrever(self):
        print(f'Caneta {self.__cor} está escrevendo...')


class MaquinaDeEscrever:
    def escrever(self):
        print(f'Máquina está escrevendo...')
