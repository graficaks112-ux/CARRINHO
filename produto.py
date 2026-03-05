class Produto:
   # Método construtor - executado quando criamos um novo produto
    def __init__(self, nome, preco, quantidade=1):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    # Método que calcula o valor total daquele produto
    def subtotal(self):
        return self.preco * self.quantidade
    # Método especial que define como o objeto será exibido
    def __str__(self):
        return f"{self.nome} | R$ {self.preco:.2f} | Qtd: {self.quantidade} | Subtotal: R$ {self.subtotal():.2f}"