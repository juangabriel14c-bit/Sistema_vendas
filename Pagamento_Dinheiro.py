from pagamento import Pagamento


class PagamentoDinheiro(Pagamento):
    def __init__(self):
        super().__init__("Dinheiro")

    def calcular_valor_final(self, valor):
        return valor * 0.97