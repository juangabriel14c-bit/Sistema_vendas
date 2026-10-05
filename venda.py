from item_venda import ItemVenda


class Venda:
    def __init__(self, id, data):
        self.__id = id
        self.__data = data
        self.__itens = []

    @property
    def id(self):
        return self.__id

    @property
    def data(self):
        return self.__data

    @property
    def itens(self):
        return self.__itens.copy()

    def adicionarItem(self, produto, quantidade):
        if quantidade <= 0:
            print("A quantidade deve ser maior que zero.")
            return False

        if produto.decrementarEstoque(quantidade):

            item = ItemVenda(
                quantidade,
                produto
            )

            self.__itens.append(item)

            print(
                f"{quantidade}x {produto.nome} "
                f"adicionado(s) à venda."
            )

            return True

        print(
            f"Estoque insuficiente para "
            f"{produto.nome}."
        )

        return False

    def calcularTotal(self):
        total = 0

        for item in self.__itens:
            total += item.calcularSubtotal()

        return total

    def calcularQtdTotal(self):
        quantidadeTotal = 0

        for item in self.__itens:
            quantidadeTotal += item.quantidade

        return quantidadeTotal

    def exibirComprovante(self):
        print("\n========== COMPROVANTE ==========")

        print(f"Venda: {self.__id}")
        print(f"Data: {self.__data}")

        print("---------------------------------")

        for item in self.__itens:
            print(
                f"{item.produto.nome} | "
                f"{item.quantidade}x | "
                f"R$ {item.produto.preco:.2f} | "
                f"Subtotal: R$ {item.calcularSubtotal():.2f}"
            )

        print("---------------------------------")

        print(
            f"Quantidade total: "
            f"{self.calcularQtdTotal()}"
        )

        print(
            f"Valor total: "
            f"R$ {self.calcularTotal():.2f}"
        )

        print("=================================")