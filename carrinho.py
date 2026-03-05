# Classe responsável por gerenciar os produtos adicionados
class Carrinho:
    
    # Construtor da classe Carrinho
    def __init__(self):
        self.produtos = []
        self.desconto = 0
    
    # Método para adicionar um produto à lista
    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        print("Produto adicionado com sucesso!")
    
     # Método para remover um produto pelo nome
    def remover_produto(self, nome_produto):
        for produto in self.produtos:
            if produto.nome.lower() == nome_produto.lower():
                self.produtos.remove(produto)
                print("Produto removido com sucesso!")
                return
        print("Produto não encontrado.")

    # Método que calcula o total da compra com desconto
    def calcular_total(self):
        # Soma todos os subtotais dos produtos
        total = sum(produto.subtotal() for produto in self.produtos)
        return total - self.desconto

    # Método para aplicar desconto
    def aplicar_desconto(self, valor):
        self.desconto = valor
        print("Desconto aplicado com sucesso!")

    # Método que gera a nota fiscal formatada
    def gerar_nota_fiscal(self):
        print("\n" + "=" * 50)
        print("NOTA FISCAL".center(50))
        print("=" * 50)

        # Verifica se o carrinho está vazio
        if not self.produtos:
            print("Carrinho vazio.")
            return

        total_bruto = 0

        # Exibe cada produto do carrinho
        for produto in self.produtos:
            print(produto)
            total_bruto += produto.subtotal()

        print("-" * 50)
        print(f"Total Bruto: R$ {total_bruto:.2f}")
        print(f"Desconto: R$ {self.desconto:.2f}")
        print(f"Total Final: R$ {self.calcular_total():.2f}")
        print("=" * 50)