# arquivo: main.py

from Models.SistemaEstoque import SistemaEstoque


def exibir_menu():

    print("\n===== SISTEMA DE GESTÃO DE ESTOQUE =====")
    print("1. Adicionar Estoque a um Produto")
    print("2. Remover Estoque de um Produto")
    print("3. Buscar Produto por Código")
    print("4. Listar todos os Produtos")
    print("5. Registrar Venda")
    print("6. Listar Histórico de Vendas")
    print("7. APAGAR TODOS OS REGISTROS DE VENDA")
    print("8. Sair do Sistema")
    print("========================================")
    return input(">> Escolha uma opção: ")


def fluxo_buscar_produto(sistema: SistemaEstoque):

    print("\n--- Buscar Produto por Código ---")
    try:
        cod_input = int(
            input("Digite o código do produto que deseja buscar: "))
        produto_encontrado = sistema.buscar_produto(cod_input)

        if produto_encontrado:
            print("\n--- Produto Encontrado ---")

            print(produto_encontrado)
        else:
            print(
                f"\nERRO: Nenhum produto encontrado com o código {cod_input}.")
    except ValueError:
        print("\nERRO: O código do produto deve ser um número inteiro.")


if __name__ == "__main__":
    ARQUIVO_VENDAS = 'vendas.json'
    ARQUIVO_DE_DADOS = 'produtos.json'

    sistema = SistemaEstoque()

    sistema.carregar_produtos_de_json(ARQUIVO_DE_DADOS)
    sistema.carregar_vendas_de_json(ARQUIVO_VENDAS)
    while True:
        opcao = exibir_menu()
        if opcao == '1':
            sistema.adicionar_produto_estoque()
        elif opcao == '2':
            sistema.remover_produto_estoque()
        elif opcao == '3':
            fluxo_buscar_produto(sistema)
        elif opcao == '4':
            sistema.listar_produtos()
        elif opcao == '5':
            sistema.registrar_venda()
        elif opcao == '6':
            sistema.listar_vendas()
        elif opcao == '7':
            sistema.eliminar_todas_as_vendas()
        elif opcao == '8':
            print("\nSalvando alterações no arquivo de dados...")
            sistema.salvar_produtos_em_json(ARQUIVO_DE_DADOS)
            print("Sistema finalizado. Até logo, Vendedor!")
            break

        else:
            print("\nOpção inválida. Por favor, escolha uma opção válida do menu.")
