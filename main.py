from produto import Produto
from venda import Venda


# ==============================
# CRIANDO OS PRODUTOS
# ==============================

produto1 = Produto(
    1,
    "Mouse",
    80.00,
    "Mouse Gamer",
    10
)

produto2 = Produto(
    2,
    "Teclado",
    150.00,
    "Teclado Mecânico",
    5
)

produto3 = Produto(
    3,
    "Monitor",
    900.00,
    "Monitor 24 polegadas",
    3
)


# ==============================
# CRIANDO A VENDA
# ==============================

venda1 = Venda(
    1,
    "04/10/2026"
)


# ==============================
# ADICIONANDO PRODUTOSx
# ==============================

venda1.adicionarItem(produto1, 2)

venda1.adicionarItem(produto2, 1)

venda1.adicionarItem(produto3, 1)


# ==============================
# EXIBINDO O COMPROVANTE
# ==============================

venda1.exibirComprovante()


# ==============================
# MOSTRANDO O ESTOQUE
# ==============================

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