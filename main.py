
from produto import Produto
from venda import Venda
from datetime import datetime
from Pagamento_debito import PagamentoDebito
from Pagamento_Pix import PagamentoPix
from Pagamento_Dinheiro import PagamentoDinheiro
from Pagamento_Cartao import PagamentoCartao


# OS PRODUTOS

produto1 = Produto(
    1,
    "Mouse",
    100.00,
    "Mouse Gamer",
    10
)

produto2 = Produto(
    2,
    "Teclado",
    180.00,
    "Teclado Mecânico",
    7
)

produto3 = Produto(
    3,
    "Monitor",
    1000.00,
    "Monitor 24 polegadas",
    4
)


# VENDA 1 - PIX (desconto de 5%)

venda1 = Venda(
    1,
    datetime.now(),
    PagamentoPix()
)

venda1.adicionar_item(produto1, 2)
venda1.adicionar_item(produto2, 1)
venda1.adicionar_item(produto3, 1)

if venda1.remover_item(produto2):
    print("Teclado removido da venda!")
else:
    print("Produto não encontrado na venda.")

venda1.finalizar_venda()


# VENDA 2 - DINHEIRO (desconto de 3%)

venda2 = Venda(
    2,
    datetime.now(),
    PagamentoDinheiro()
)

venda2.adicionar_item(produto1, 1)
venda2.adicionar_item(produto2, 1)

venda2.finalizar_venda()


# VENDA 3 - CARTÃO (acréscimo de 5%)

venda3 = Venda(
    3,
    datetime.now(),
    PagamentoCartao()
)

venda3.adicionar_item(produto3, 1)

venda3.finalizar_venda()


# VENDA 4 - DÉBITO (sem alteração)

venda4 = Venda(
    4,
    datetime.now(),
    PagamentoDebito()
)

venda4.adicionar_item(produto1, 1)

venda4.finalizar_venda()


# VISUALIZAR QUANTIDADE DE VENDAS

print("\n========== CONTROLE DE VENDAS ==========")

print(
    f"Total de vendas existentes no sistema: "
    f"{Venda.get_total_vendas()}"
)


# VISUALIZAR O ESTOQUE

print("\n========== ESTOQUE ==========")

print(
    f"{produto1.nome}: "
    f"{produto1.verificarEstoque()}"
)

print(
    f"{produto2.nome}: "
    f"{produto2.verificarEstoque()}"
)

print(
    f"{produto3.nome}: "
    f"{produto3.verificarEstoque()}"
)
