class Pagamento:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def calcular_valor_final(self, valor):
        return valor