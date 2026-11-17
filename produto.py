class Produto:
    def __init__(self, id, nome, preco_unitario, descricao, estoque):
        self.__id = id
        self.__nome = nome
        self.__preco_unitario = preco_unitario
        self.__descricao = descricao
        self.__estoque = estoque

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome
                                                                          
    @property
    def preco_unitario(self):
        return self.__preco_unitario

    @property
    def descricao(self):
        return self.__descricao

    def decrementar_estoque(self, quantidade):
        if quantidade <= 0:
            return False

        if self.__estoque >= quantidade:
            self.__estoque -= quantidade
            return True

        return False

    def incrementarEstoque(self, quantidade):
        if quantidade > 0:
            self.__estoque += quantidade

    def verificarEstoque(self):
        return self.__estoque
