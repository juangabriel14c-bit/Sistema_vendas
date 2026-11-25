
from produto import Produto
from venda import Venda
from datetime import datetime

from Pagamento_debito import PagamentoDebito
from Pagamento_Pix import PagamentoPix
from Pagamento_Dinheiro import PagamentoDinheiro
from Pagamento_Cartao import PagamentoCartao


# LISTAS DO SISTEMA

produtos = [
    Produto(1, "Mouse", 100.00, "Mouse Gamer", 10),
    Produto(2, "Teclado", 180.00, "Teclado Mecânico", 7),
    Produto(3, "Monitor", 1000.00, "Monitor 24 polegadas", 4)
]

vendas = []

# FUNÇÕES AUXILIARES

def ler_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Digite um número inteiro válido.")


def ler_float(mensagem):
    while True:
        try:
            valor = float(input(mensagem).replace(",", "."))
            if valor > 0:
                return valor
            print("Digite um valor maior que zero.")
        except ValueError:
            print("Digite um valor válido.")


def buscar_produto(id_produto):
    for produto in produtos:
        if produto.id == id_produto:
            return produto
    return None


# 1. CADASTRAR PRODUTO

def cadastrar_produto():
    print("\n========== CADASTRAR PRODUTO ==========")

    if produtos:
        novo_id = max(p.id for p in produtos) + 1
    else:
        novo_id = 1

    nome = input("Nome do produto: ")
    preco = ler_float("Preço unitário: R$ ")
    descricao = input("Descrição: ")
    estoque = ler_inteiro("Quantidade em estoque: ")

    if not nome.strip() or estoque < 0:
        print("Dados inválidos.")
        return

    produto = Produto(
        novo_id,
        nome,
        preco,
        descricao,
        estoque
    )

    produtos.append(produto)

    print("Produto cadastrado com sucesso!")


# 2. ALTERAR PRODUTO

def alterar_produto():
    print("\n========== ALTERAR PRODUTO ==========")

    id_produto = ler_inteiro("Digite o ID do produto: ")

    produto = buscar_produto(id_produto)

    if produto is None:
        print("Produto não encontrado.")
        return

    print("\n1. Alterar nome")
    print("2. Alterar preço")
    print("3. Alterar descrição")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        novo_nome = input("Novo nome: ")

        if produto.alterar_nome(novo_nome):
            print("Nome alterado com sucesso!")
        else:
            print("Nome inválido.")

    elif opcao == "2":
        novo_preco = ler_float("Novo preço: R$ ")

        produto.alterar_preco(novo_preco)
        print("Preço alterado com sucesso!")

    elif opcao == "3":
        nova_descricao = input("Nova descrição: ")

        if produto.alterar_descricao(nova_descricao):
            print("Descrição alterada com sucesso!")
        else:
            print("Descrição inválida.")

    else:
        print("Opção inválida.")


# 3. LISTAR PRODUTOS

def listar_produtos():
    print("\n========== PRODUTOS CADASTRADOS ==========")

    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    for produto in produtos:
        print("---------------------------------")
        print(f"ID: {produto.id}")
        print(f"Nome: {produto.nome}")
        print(f"Preço: R$ {produto.preco_unitario:.2f}")
        print(f"Descrição: {produto.descricao}")
        print(f"Estoque: {produto.verificarEstoque()}")

    print("---------------------------------")


# 4. REALIZAR VENDA

def realizar_venda():
    print("\n========== REALIZAR VENDA ==========")

    if not produtos:
        print("Não existem produtos cadastrados.")
        return

    listar_produtos()

    # Monta o carrinho antes de criar a venda
    carrinho = []
    estoque_disponivel = {
        produto.id: produto.verificarEstoque()
        for produto in produtos
    }

    while True:
        id_produto = ler_inteiro(
            "\nDigite o ID do produto (0 para terminar): "
        )

        if id_produto == 0:
            break

        produto = buscar_produto(id_produto)

        if produto is None:
            print("Produto não encontrado.")
            continue

        quantidade = ler_inteiro("Quantidade: ")

        if quantidade <= 0:
            print("A quantidade deve ser maior que zero.")
            continue

        if quantidade > estoque_disponivel[id_produto]:
            print("Estoque insuficiente.")
            continue

        carrinho.append((produto, quantidade))
        estoque_disponivel[id_produto] -= quantidade

        print("Produto adicionado ao carrinho!")

    if not carrinho:
        print("Venda cancelada: nenhum produto selecionado.")
        return

    print("\n========== FORMA DE PAGAMENTO ==========")
    print("1. Pix")
    print("2. Dinheiro")
    print("3. Cartão")
    print("4. Débito")

    opcao = input("Escolha o pagamento: ")

    if opcao == "1":
        pagamento = PagamentoPix()
    elif opcao == "2":
        pagamento = PagamentoDinheiro()
    elif opcao == "3":
        pagamento = PagamentoCartao()
    elif opcao == "4":
        pagamento = PagamentoDebito()
    else:
        print("Forma de pagamento inválida.")
        return

    # Cria a venda somente depois de montar o carrinho
    novo_id = len(vendas) + 1

    venda = Venda(
        novo_id,
        datetime.now(),
        pagamento
    )

    for produto, quantidade in carrinho:
        venda.adicionar_item(produto, quantidade)

    if venda.finalizar_venda():
        vendas.append(venda)
        print("Venda registrada com sucesso!")


# 5. RELATÓRIO DE VENDAS

def relatorio_vendas():
    print("\n========== RELATÓRIO DE VENDAS ==========")

    if not vendas:
        print("Nenhuma venda realizada.")
        return

    print(f"Total de vendas realizadas: {len(vendas)}")

    for venda in vendas:
        print("\n---------------------------------")
        print(f"Venda: {venda.id}")
        print(f"Data: {venda.data.strftime('%d/%m/%Y %H:%M')}")
        print(f"Pagamento: {venda.pagamento.nome}")

        print("Produtos:")

        for item in venda.itens:
            print(
                f"{item.produto.nome} - "
                f"{item.quantidade}x - "
                f"R$ {item.calcular_subtotal():.2f}"
            )

        print(f"Valor total: R$ {venda.valor_total:.2f}")
        print(
            f"Valor final: "
            f"R$ {venda.calcular_valor_final():.2f}"
        )

    print("---------------------------------")

    print(
        f"Total registrado pela classe Venda: "
        f"{Venda.get_total_vendas()}"
    )


# MENU PRINCIPAL

def menu():
    while True:
        print("\n========== SISTEMA DE VENDAS ==========")
        print("1. Cadastrar produto")
        print("2. Alterar produto")
        print("3. Listar produtos")
        print("4. Realizar venda")
        print("5. Relatório de vendas")
        print("0. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            cadastrar_produto()

        elif opcao == "2":
            alterar_produto()

        elif opcao == "3":
            listar_produtos()

        elif opcao == "4":
            realizar_venda()

        elif opcao == "5":
            relatorio_vendas()

        elif opcao == "0":
            print("Sistema encerrado.")
            break

        else:
            print("Opção inválida. Tente novamente.")


# INICIAR SISTEMA

menu()
