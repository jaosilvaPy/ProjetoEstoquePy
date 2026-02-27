
class Produto:
    """
    Representa um produto no sistema de estoque.
    
    Attributes:
        cod_produto (int): Código único do produto
        nome (str): Nome do produto
        categoria (str): Categoria do produto
        preco_custo (float): Preço de custo
        estoque (int): Quantidade em estoque
        preco (float): Preço de venda
        estoque_minimo (int): Quantidade mínima recomendada
    """
    def __init__(self, cod_produto, nome, categoria, preco_custo, preco, estoque_minimo, estoque, fornecedor):
        self.cod_produto = cod_produto
        self.nome = nome
        self.categoria = categoria
        self.preco_custo = float(preco_custo)
        self.preco = float(preco)
        self.estoque_minimo = int(estoque_minimo)
        self.estoque = int(estoque)
        self.fornecedor = fornecedor

    def adicionar_estoque(self, quantidade):
        if quantidade > 0:
            self.estoque += quantidade
            print(
                f"Sucesso! Novo estoque para '{self.nome}': {self.estoque} unidades.")
        else:
            print("ERRO: A quantidade deve ser um número positivo.")

    def remover_estoque(self, quantidade):
        if quantidade <= 0:
            print("ERRO: A quantidade a ser removida deve ser um número positivo.")
            return False

        if quantidade <= self.estoque:
            self.estoque -= quantidade
            print(f"Sucesso! {quantidade} unidades removidas.")
            print(f"Novo estoque para '{self.nome}': {self.estoque} unidades.")
            return True
        else:
            print(
                f"ERRO: Estoque insuficiente. Você tentou remover {quantidade}, mas só há {self.estoque} em estoque.")
            return False
    def para_dicionario(self):
        
        return {
            "cod_produto": self.cod_produto,
            "nome": self.nome,
            "categoria": self.categoria,
            "preco_custo": self.preco_custo,
            "preco": self.preco,
            "estoque_minimo": self.estoque_minimo,
            "estoque": self.estoque,
            "fornecedor": self.fornecedor
        }
    def __str__(self):
        """Para exibição ao usuário final (usado por listar_produtos)."""
        return (f"Cód: {self.cod_produto} | Nome: {self.nome} | "
                f"Estoque: {self.estoque} | Preço: R$ {self.preco:.2f}")

    def __repr__(self):
        return f"Produto({self.nome}, Fornecedor: {self.fornecedor}, Estoque: {self.estoque})"
