class ItemVenda:
    def __init__(self, quantidade, produto):
        self.__quantidade = quantidade
        self.__produto = produto

    @property
    def quantidade(self):
        return self.__quantidade

    @property
    def produto(self):
        return self.__produto

    def calcularSubtotal(self):
        return self.__quantidade * self.__produto.preco
