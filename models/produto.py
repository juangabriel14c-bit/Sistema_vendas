class Produto:
    def __init__(self, id, nome, preco, descricao, quantidadeEstoque):
        self.__id = id
        self.__nome = nome
        self.__preco = preco
        self.__descricao = descricao
        self.__quantidadeEstoque = quantidadeEstoque

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @property
    def preco(self):
        return self.__preco

    @property
    def descricao(self):
        return self.__descricao

    def decrementarEstoque(self, quantidade):
        if quantidade <= 0:
            return False

        if self.__quantidadeEstoque >= quantidade:
            self.__quantidadeEstoque -= quantidade
            return True

        return False

    def incrementarEstoque(self, quantidade):
        if quantidade > 0:
            self.__quantidadeEstoque += quantidade

    def verificarEstoque(self):
        return self.__quantidadeEstoque
