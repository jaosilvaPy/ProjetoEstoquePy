# 🏪 Sistema de Gestão de Estoque

Sistema completo de gerenciamento de estoque e controle de vendas desenvolvido em Python com persistência de dados em JSON.

## 📋 Sobre o Projeto

Sistema desenvolvido para facilitar o controle de estoque de produtos, permitindo registro de vendas, controle de quantidades mínimas e histórico completo de transações. Ideal para pequenos e médios comércios que precisam de uma solução simples e eficiente.

## ✨ Funcionalidades

- ✅ **Gerenciamento de Estoque**
  - Adicionar quantidade ao estoque de produtos
  - Remover quantidade do estoque
  - Buscar produtos por código
  - Listar todos os produtos cadastrados
  - Alertas de estoque mínimo

- ✅ **Sistema de Vendas**
  - Registro de vendas com múltiplos produtos
  - Carrinho de compras
  - Suporte a múltiplas formas de pagamento (Crédito, Débito, Pix, Boleto, Dinheiro)
  - Geração automática de recibo
  - Validação de estoque disponível

- ✅ **Histórico e Relatórios**
  - Histórico completo de vendas
  - Informações detalhadas de cada transação
  - Identificação única (UUID) para cada venda

- ✅ **Persistência de Dados**
  - Salvamento automático em JSON
  - Carregamento automático ao iniciar o sistema
  - Backup de dados entre sessões

## 🛠️ Tecnologias Utilizadas

- **Python 3.7+**
- **JSON** - Persistência de dados
- **UUID** - Identificação única de vendas
- **Datetime** - Controle de data e hora das transações
- **Programação Orientada a Objetos (OOP)**

## 📁 Estrutura do Projeto

```
ProjetoEstoquePy/
│
├── main.py                      # Arquivo principal (interface do sistema)
├── produtos.json                # Banco de dados de produtos
├── vendas.json                  # Histórico de vendas
│
└── Models/
    ├── __init__.py
    ├── Produto.py               # Classe Produto
    ├── Venda.py                 # Classe Venda
    └── SistemaEstoque.py        # Classe principal do sistema
```

## 🚀 Como Executar

### Pré-requisitos

- Python 3.7 ou superior instalado

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/jaosilvaPy/ProjetoEstoquePy.git
cd ProjetoEstoquePy
```

2. Execute o sistema:
```bash
python main.py
```

## 💻 Como Usar

### Menu Principal

Ao executar o sistema, você verá o seguinte menu:

```
===== SISTEMA DE GESTÃO DE ESTOQUE =====
1. Adicionar Estoque a um Produto
2. Remover Estoque de um Produto
3. Buscar Produto por Código
4. Listar todos os Produtos
5. Registrar Venda
6. Listar Histórico de Vendas
7. APAGAR TODOS OS REGISTROS DE VENDA
8. Sair do Sistema
========================================
```

### Exemplo de Uso - Registrar uma Venda

1. Selecione a opção `5` (Registrar Venda)
2. Digite o código do produto desejado
3. Informe a quantidade
4. Repita para adicionar mais produtos ou digite `0` para finalizar
5. Escolha a forma de pagamento
6. Informe o código do vendedor
7. Digite o nome do comprador
8. ✅ Venda registrada e estoque atualizado!

## 🎯 Destaques Técnicos

### Validações Implementadas

- ✅ Validação de tipos de dados (int, float, string)
- ✅ Verificação de estoque disponível
- ✅ Alertas de estoque mínimo com confirmação
- ✅ Tratamento robusto de exceções
- ✅ Validação de quantidade (não permite valores negativos ou zero)
- ✅ Validação de formas de pagamento

### Arquitetura

- **Separação de responsabilidades**: Classes independentes para Produto, Venda e SistemaEstoque
- **Encapsulamento**: Métodos bem definidos com responsabilidades únicas
- **Persistência**: Sistema de salvamento automático e seguro
- **Recuperação**: Carregamento de dados preserva histórico completo

## 📊 Estrutura de Dados

### Produto
```json
{
  "cod_produto": 201,
  "nome": "Dell XPS 13",
  "categoria": "Notebooks",
  "preco_custo": 5200.0,
  "preco": 6999.9,
  "estoque_minimo": 5,
  "estoque": 16,
  "fornecedor": "Dell"
}
```

### Venda
```json
{
  "id_venda": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "data_hora": "2025-02-23T14:30:00",
  "forma_pagamento": "Pix",
  "cod_vendedor": 101,
  "nome_comprador": "João Silva",
  "produtos_vendidos": [...],
  "valor_total": 6999.90,
  "status": "Concluída"
}
```

## 🔒 Segurança e Confiabilidade

- ✅ Tratamento de exceções em todas as operações críticas
- ✅ Validação de entrada de dados
- ✅ Backup automático antes de operações destrutivas
- ✅ Confirmação para ações irreversíveis
- ✅ Mensagens de erro claras e informativas

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fazer um Fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/NovaFuncionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/NovaFuncionalidade`)
5. Abrir um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👨‍💻 Autor

**João Gabriel Silva Pinto**

- GitHub: [@jaosilvaPy](https://github.com/jaosilvaPy)
- LinkedIn: [João Gabriel](www.linkedin.com/in/joão-silva-a2b9323b0)
- Email: jaodevsilva@gmail.com

## 🙏 Agradecimentos

- Projeto desenvolvido como parte do aprendizado de Python e Programação Orientada a Objetos
- Agradecimentos especiais à comunidade Python pela documentação e recursos

---

⭐ Se este projeto te ajudou, considere dar uma estrela no repositório!
