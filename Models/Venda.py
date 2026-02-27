from datetime import datetime
import uuid
from .Produto import Produto


class Venda:
    def __init__(self, carrinho: list, forma_pagamento: str, cod_vendedor: int, nome_comprador: str, status: str = "Concluída"):
        self.id_venda = uuid.uuid4()
        self.data_hora = datetime.now()
        self.forma_pagamento = forma_pagamento
        self.cod_vendedor = cod_vendedor
        self.nome_comprador = nome_comprador
        self.status = status

        # CARRINHO
        self.produtos_vendidos = []
        self.cod_produtos_vendidos = []
        self.nome_produtos_vendidos = []
        self.valor_total = 0.0

        for item in carrinho:
            produto = item["produto"]
            quantidade = item["quantidade"]

            # subtotal
            subtotal_item = produto.preco * quantidade
            self.valor_total += subtotal_item

            # adicionar itens vendidos
            self.cod_produtos_vendidos.append(produto.cod_produto)
            self.nome_produtos_vendidos.append(produto.nome)

            # gerar cópia para recibo
            self.produtos_vendidos.append({
                "codigo": produto.cod_produto,
                "nome": produto.nome,
                "quantidade": quantidade,
                "preco_unitario": produto.preco,
                "subtotal": subtotal_item
            }
    )
    @classmethod
    def from_dict(cls, dados: dict):
    # Criar objeto SEM chamar __init__
        venda = object.__new__(cls)
        
        # Preencher os atributos manualmente
        venda.id_venda = uuid.UUID(dados['id_venda'])
        venda.data_hora = datetime.fromisoformat(dados['data_hora'])
        venda.forma_pagamento = dados['forma_pagamento']
        venda.cod_vendedor = dados['cod_vendedor']
        venda.nome_comprador = dados['nome_comprador']
        venda.status = dados['status']
        venda.produtos_vendidos = dados['produtos_vendidos']
        venda.valor_total = dados['valor_total']
    
        return venda
    


    
    def para_dicionario(self):
        return {
            'id_venda': str(self.id_venda),
            'data_hora': self.data_hora.isoformat(),
            'forma_pagamento': self.forma_pagamento,
            'status': self.status,
            'cod_vendedor': self.cod_vendedor,
            'nome_comprador': self.nome_comprador,
            'produtos_vendidos': self.produtos_vendidos,
            'valor_total': self.valor_total
        }
    def __str__(self):
        itens_str = ""
        for item in self.produtos_vendidos:
            itens_str += (f"  - {item['nome']} (Cód: {item['codigo']})\n"
                        f"    {item['quantidade']} un x R$ {item['preco_unitario']:.2f} = R$ {item['subtotal']:.2f}\n")

        return (f"\n================ RECIBO DE VENDA ================\n"
                f"ID da Venda: {self.id_venda}\n"
                f"Data/Hora: {self.data_hora.strftime('%d/%m/%Y %H:%M:%S')}\n"
                f"Cliente: {self.nome_comprador}\n"
                f"Vendedor(a): Cód {self.cod_vendedor}\n"
                f"Status: {self.status}\n"
                f"------------------ ITENS ------------------\n"
                f"{itens_str}"
                f"---------------------------------------------\n"
                f"VALOR TOTAL: R$ {self.valor_total:.2f}\n"
                f"Forma de Pagamento: {self.forma_pagamento}\n"
                f"=============================================\n")