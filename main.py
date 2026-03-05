# Importando as classes criadas em outros arquivos
from produto import Produto
from carrinho import Carrinho

# 🔹 FUNÇÃO DO MENU 
def mostrar_menu():
    print("\n" + "=" * 60)
    print("🛒 SISTEMA DE CARRINHO ONLINE 🛒".center(60))
    print("=" * 60)
    print(" [1] ➜ Adicionar Produto")
    print(" [2] ➜ Remover Produto")
    print(" [3] ➜ Aplicar Desconto")
    print(" [4] ➜ Ver Nota Fiscal")
    print(" [5] ➜ Sair do Sistema")
    print("=" * 60)


# Criando o objeto carrinho
carrinho = Carrinho()


# Loop principal do sistema
while True:

    # 🔹 Aqui chama a função
    mostrar_menu()

    opcao = input("Escolha uma opção: ")
    # Opção 1 - Adicionar produto
    if opcao == "1":
        try:
            nome = input("Nome do produto: ")
            preco = float(input("Preço do produto: R$ "))
            quantidade = int(input("Quantidade: "))

            # Criando objeto Produto
            produto = Produto(nome, preco, quantidade)

            # Adicionando ao carrinho
            carrinho.adicionar_produto(produto)
        
        except ValueError as erro:
            # Captura erros de validação
            print(f"Erro: {erro}")

    # Opção 2 - Remover produto
    elif opcao == "2":
        nome = input("Digite o nome do produto para remover: ")
        carrinho.remover_produto(nome)

    # Opção 3 - Aplicar desconto
    elif opcao == "3":
        desconto = float(input("Valor do desconto: R$ "))
        carrinho.aplicar_desconto(desconto)

    # Opção 4 - Gerar nota fiscal
    elif opcao == "4":
        carrinho.gerar_nota_fiscal()

    # Opção 5 - Encerrar sistema
    elif opcao == "5":
        print("Encerrando sistema...")
        break

    # Caso digite opção inválida
    else:
        print("Opção inválida. Tente novamente.")