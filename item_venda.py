class ItemVenda:
    def __init__(self, quantidade, produto):
        self.__quantidade = quantidade
        self.__produto = produto
        self.__valor_item = produto.preco_unitario

    @property
    def quantidade(self):
        return self.__quantidade

    @property
    def produto(self):
        return self.__produto

    @property
    def valor_item(self):
        return self.__valor_item

    def calcular_subtotal(self):
        return self.__quantidade * self.__valor_item
