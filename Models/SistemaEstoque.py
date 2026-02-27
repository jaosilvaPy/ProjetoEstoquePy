import json
from .Produto import Produto
from .Venda import Venda


class SistemaEstoque:
    def __init__(self):
        self.produtos = {}
        self.vendas = []

    def carregar_produtos_de_json(self, caminho_arquivo):
        try:
            with open(caminho_arquivo, 'r', encoding='utf-8') as f:
                dados_produtos = json.load(f)

                for dados in dados_produtos:

                    p = Produto(**dados)

                    self.produtos[p.cod_produto] = p

            print(
                f"Sucesso: {len(self.produtos)} produtos carregados de '{caminho_arquivo}'.")

        except FileNotFoundError:
            print(
                f"AVISO: O arquivo '{caminho_arquivo}' não foi encontrado. O sistema iniciará vazio.")
        except Exception as e:
            print(f"ERRO: Ocorreu um erro ao carregar o arquivo JSON: {e}")

    def adicionar_produto_estoque(self):
        if not self.produtos:
            print("\nNenhum produto cadastrado no estoque.")
            return

        try:
            cod_input = input("\nDigite o Código do Produto: ")
            cod_para_buscar = int(cod_input)

            codEncontrado = self.buscar_produto(cod_para_buscar)

            if codEncontrado:

                print(f"\n--- Produto Encontrado ---")
                print(f"Código: {codEncontrado.cod_produto}")
                print(f"Nome:   {codEncontrado.nome}")
                print(f"Estoque Atual: {codEncontrado.estoque}")
                print(f"--------------------------")

                conf = input("É este o produto correto? (s/n): ").lower()

                if conf == 's':
                    try:
                        qtdAddEstoque = int(
                            input("Digite a quantidade a ser adicionada: "))

                        codEncontrado.adicionar_estoque(qtdAddEstoque)
                        self.salvar_produtos_em_json("produtos.json")

                    except ValueError:
                        print("\nERRO: A quantidade deve ser um número inteiro.")
                else:
                    print("\nOperação cancelada pelo usuário.")
            else:

                print(
                    f"\nERRO: Nenhum produto encontrado com o código {cod_para_buscar}.")

        except ValueError:
            print("\nERRO: O código do produto deve ser um número inteiro.")

    def remover_produto_estoque(self):
        if not self.produtos:
            print("Nenhum produto cadastrado no estoque.")
            return
        try:
            codProdRemove = input("Digite o Código do Produto:")
            codBuscaRemove = int(codProdRemove)
            codEncontrado = self.buscar_produto(codBuscaRemove)

            if codEncontrado:
                print(f"Código : {codEncontrado.cod_produto}")
                print(f"Nome   : {codEncontrado.nome}")
                print(f"Estoque: {codEncontrado.estoque}")

                conf = input("É este o produto correto? (s/n): ").lower()
                if conf == 's':
                    try:
                        qtdRemove = int(
                            input("Digite a quantidade a ser removida do estoque:"))
                        sucesso = codEncontrado.remover_estoque(qtdRemove)
                        if sucesso:
                            self.salvar_produtos_em_json("produtos.json")
                    except ValueError:
                        print("\nERRO: A quantidade deve ser um número inteiro.")
                else:
                    print("\nOperação cancelada pelo usuário.")
            else:
                print(
                    f"ERRO | Nenhum produto encontrado com o código {codBuscaRemove}.")
        except ValueError:
            print("\nERRO: O código do produto deve ser um número inteiro.")

    def salvar_produtos_em_json(self, caminho_arquivo):
        try:
            lista_de_produtos_para_salvar = []

            for produto_obj in self.produtos.values():
                lista_de_produtos_para_salvar.append(
                    produto_obj.para_dicionario())

            with open(caminho_arquivo, 'w', encoding='utf-8') as f:

                json.dump(lista_de_produtos_para_salvar,
                          f, indent=4, ensure_ascii=False)

            print(
                f"\nSucesso! Os dados de {len(self.produtos)} produtos foram salvos em '{caminho_arquivo}'.")

        except Exception as e:
            print(
                f"\nERRO CRÍTICO: Não foi possível salvar os dados no arquivo. Causa: {e}")

    def registrar_venda(self):
        """
        Registra uma nova venda no sistema.

        Permite ao usuário adicionar produtos ao carrinho, escolher forma
        de pagamento e finalizar a transação. Atualiza automaticamente o
        estoque e salva a venda no histórico.
        """
        if not self.produtos:
            print("\nNenhum produto cadastrado no sistema.")
            return
        carrinho = []
        while True:
            try:
                cod_input = input(
                    "\nDigite o Código do Produto ou '0' para finalizar a venda: ")
                if cod_input == '0':
                    break
                produto = self.buscar_produto(int(cod_input))
                if not produto:
                    print(
                        f"\nERRO: Nenhum produto encontrado com o código {cod_input}.")
                    continue
                while True:
                    try:
                        qtd = int(
                            input(f"Digite a quantidade para o produto {produto.nome}: "))
                        if qtd <= 0:
                            print("\nERRO: A quantidade deve ser maior que zero.")
                            continue
                        break
                    except ValueError:
                        print("\nERRO: A quantidade deve ser um número inteiro.")
                if qtd > produto.estoque:
                    print(
                        f"\nERRO: Estoque insuficiente para o produto {produto.nome}.")
                    continue
                if (produto.estoque - qtd) < produto.estoque_minimo:
                    print("⚠️  ATENÇÃO: Esta venda deixará o estoque abaixo do mínimo!")
                    print(
                        f"Estoque atual: {produto.estoque} | Após venda: {produto.estoque - qtd} | Mínimo: {produto.estoque_minimo}")
                    confirmar = input(
                        "Deseja continuar mesmo assim? (s/n): ").lower()
                    if confirmar != 's':
                        print("Venda cancelada.")
                        continue
                carrinho.append({"produto": produto, "quantidade": qtd})
                print(
                    f"\nSucesso! Produto {produto.nome} adicionado ao carrinho.")

            except ValueError:
                print(
                    "\nERRO: O código do produto e quantidade deve ser um número inteiro.")
            except Exception as e:
                print(f"Ocorreu um erro: {e}")
        if not carrinho:
            print("\nVenda cancelada (carrinho vazio).")
            return
        print("FINALIZANDO A VENDA")
        formas_pagamento = {
            1: "Cartão de Crédito",
            2: "Cartão de Débito",
            3: "Pix",
            4: "Boleto",
            5: "Dinheiro"
        }
        while True:
            try:
                cod_pagamento = int(input(
                    "Digite a forma de pagamento: \n[1] Cartão de Crédito\n[2] Cartão de Débito\n[3] Pix\n[4] Boleto\n[5] Dinheiro\n>> "))

                forma_pagamento = formas_pagamento.get(cod_pagamento)

                if forma_pagamento:
                    break
                else:
                    print("\nERRO: Forma de pagamento inválida. Escolha entre 1 e 5.")
            except ValueError:
                print("\nERRO: Digite um número válido (1 a 5).")
        while True:
            try:
                cod_vendedor = int(input("Digite o Código do Vendedor: "))
                break
            except ValueError:
                print("ERRO: Código do vendedor deve ser um número inteiro.")
        nome_comprador = input("Digite o Nome do Comprador: ")
        print("\nConfirmando transação e atualizando estoque...")

        # RETIRADA DO ESTOQUE
        for item in carrinho:
            item['produto'].remover_estoque(item['quantidade'])

        # CRIAÇÃO DO REGISTRO DE VENDA
        nova_venda = Venda(carrinho, forma_pagamento,
                           cod_vendedor, nome_comprador)
        self.vendas.append(nova_venda)
        print("SUCESSO, registro de venda criado")
        print(nova_venda)

        # ATUALIZAÇÃO DO ESTOQUE
        self.salvar_produtos_em_json("produtos.json")
        print("ESTOQUE ATUALIZADO COM SUCESSO")

        # SALVAR HISTÓRICO DE VENDAS
        self.salvar_vendas_em_json("vendas.json")
        print("HISTÓRICO DE VENDAS ATUALIZADO COM SUCESSO")

    def listar_produtos(self):

        if not self.produtos:
            print("\nNenhum produto cadastrado no sistema.")
            return

        print("\n------------------- LISTA DE PRODUTOS -------------------")

        for produto in self.produtos.values():

            print(produto)
        print("---------------------------------------------------------")

    def carregar_vendas_de_json(self, caminho_arquivo):
        try:
            with open(caminho_arquivo, 'r', encoding='utf-8') as f:
                dados_vendas = json.load(f)

                self.vendas = [Venda.from_dict(dados)
                               for dados in dados_vendas]
            print(
                f"Sucesso: {len(self.vendas)} registros de venda carregados de '{caminho_arquivo}'.")
        except FileNotFoundError:
            print(
                f"AVISO: Arquivo de vendas '{caminho_arquivo}' não encontrado. Histórico de vendas iniciado do zero.")
        except Exception as e:
            print(
                f"ERRO: Ocorreu um erro ao carregar o histórico de vendas: {e}")

    def salvar_vendas_em_json(self, caminho_arquivo):
        try:
            with open(caminho_arquivo, 'w', encoding='utf-8') as f:
                lista_de_vendas = [venda.para_dicionario()
                                   for venda in self.vendas]
                json.dump(lista_de_vendas, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(
                f"ERRO CRÍTICO: Não foi possível salvar o histórico de vendas. Causa: {e}")

    def listar_vendas(self):
        if not self.vendas:
            print("\nNenhum registro de venda encontrado.")
            return

        print("\n------------------- HISTÓRICO DE VENDAS -------------------")
        for venda in self.vendas:
            print(venda)
        print("-----------------------------------------------------------")

    def eliminar_todas_as_vendas(self):
        if not self.vendas:
            print("\nNenhum registro de venda para apagar.")
            return

        print("\n--- ATENÇÃO! ---")
        confirmacao = input(
            "Tem certeza que deseja apagar TODOS os registros de venda? Essa ação não pode ser desfeita. (s/n): ").lower()
        if confirmacao == 's':
            self.vendas.clear()
            self.salvar_vendas_em_json('vendas.json')
            print("\nTodos os registros de venda foram eliminados com sucesso.")
        else:
            print("\nOperação cancelada.")

    def buscar_produto(self, codProduto):
        return self.produtos.get(codProduto)
