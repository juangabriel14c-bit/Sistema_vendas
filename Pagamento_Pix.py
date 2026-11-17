from pagamento import Pagamento


class PagamentoPix(Pagamento):
    def __init__(self):
        super().__init__("Pix")

    def calcular_valor_final(self, valor):
        return valor * 0.95