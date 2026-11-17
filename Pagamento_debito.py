from pagamento import Pagamento


class PagamentoDebito(Pagamento):
    def __init__(self):
        super().__init__("Débito")

    def calcular_valor_final(self, valor):
        return valor