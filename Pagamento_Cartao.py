from pagamento import Pagamento


class PagamentoCartao(Pagamento):
    def __init__(self):
        super().__init__("Cartão")

    def calcular_valor_final(self, valor):
        return valor * 1.05