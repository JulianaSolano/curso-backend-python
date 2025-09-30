#juh's store
from abc import ABC, abstractmethod

class Produto(ABC):
    
    def __init__(self, nome: str, preco_base: float):
        self.nome =  nome
        self.preco_base = preco_base
    
    @abstractmethod
    def calcular_preco_final(self) -> float:
        "Calcula o preço final do produto"
        pass

class ProdutoFisico(Produto):

    def __init__(self, nome: str, preco_base: float, custo_frete: float):
        super().__init__(nome, preco_base)
        self.custo_frete = custo_frete
    
    def calcular_preco_final(self) -> float:
        return self.preco_base + self.custo_frete
    
class ProdutoDigital(Produto):

    def __init__(self, nome: str, preco_base: float, taxa_servico: float):
        super().__init__(nome, preco_base)
        self.taxa_servico = taxa_servico
    
    def calcular_preco_final(self) -> float:
        return self.preco_base + self.taxa_servico
    
#testes

if __name__ == "__main__":

    livro = ProdutoFisico("Fonética e Fonologia da Língua Portuguesa", 70.0, 15.0,)
    caneca = ProdutoFisico("Caneca Personalizada", 50.0, 15.0)
    ebook = ProdutoDigital("E-book de Gramática Universal de Línguas Indígenas", 65.0, 15.0)
    curso = ProdutoDigital("Curso Online de Fonética Articulatória", 150.0, 0.0)

    carrinho = [livro,caneca, ebook, curso]

    total = 0.0
    print("Carrinho de Compras: ")
    print("-" * 30)

    for produto in carrinho:
        preco_final = produto.calcular_preco_final()
        print(f"{produto.nome}: R$ {preco_final: .2f}")
        total += preco_final
    
    print("-" * 30)
    print(f"Total a pagar: R$ {total: .2f}")