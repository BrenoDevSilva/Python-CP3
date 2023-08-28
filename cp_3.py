estoque = {
    "rolhas": 100,
    "garrafas": 200,
    "rotulos": 150,
    "caixas": 50
}

pedidos = []

def linha_vazia():
    print(' ')

def separador():
    print(32 * '=')
    return

def calcular_frete(total_pedido):
    frete = 10 + 0.1 * total_pedido + 10
    return frete

def adicionar_produto(nome, quantidade, tipo_produto):
    if nome in estoque:
        estoque[nome] += quantidade
    else:
        estoque[nome] = quantidade

def cadastrar_pedido(cliente, itens_pedido, data_entrega):
    for item in itens_pedido:
        nome_produto = item["nome"]
        quantidade = item["quantidade"]
        if estoque.get(nome_produto, 0) >= quantidade:
            estoque[nome_produto] -= quantidade
        else:
            print("Estoque insuficiente para o pedido.")
            return
    pedidos.append({
        "cliente": cliente,
        "itens_pedido": itens_pedido,
        "data_entrega": data_entrega
    })

def exibir_estoque():
    for produto, quantidade in estoque.items():
        print(f"{produto}: {quantidade}")

def exibir_pedidos():
    for pedido in pedidos:
        print("Cliente:", pedido["cliente"])
        print("Itens do pedido:", pedido["itens_pedido"])
        print("Data de entrega:", pedido["data_entrega"])
        print("=" * 30)

while True:
    print('     Vinheria Agnelo')
    separador()
    linha_vazia()
    print("1. Adicionar Produto ao Estoque")
    print("2. Cadastrar Pedido")
    print("3. Exibir Estoque")
    print("4. Exibir Pedidos")
    print("5. Sair")
    linha_vazia()
    separador()
    linha_vazia()
    escolha = input('Escolha uma opção: ')
    linha_vazia()
    
    if escolha == "1":
        nome = input("Nome do produto: ")
        quantidade = int(input("Quantidade: "))
        adicionar_produto(nome, quantidade, "produto")
        print('Produto adicionado com sucesso!')
        linha_vazia()
    elif escolha == "2":
        cliente = input("Nome do cliente: ")
        itens_pedido = []
        continuar = "s"
        while continuar.lower() == "s":
            nome_produto = input("Nome do produto no pedido: ")
            quantidade = int(input("Quantidade: "))
            itens_pedido.append({"nome": nome_produto, "quantidade": quantidade})
            continuar = input("Adicionar mais itens? (s/n): ")
        data_entrega = input("Data de entrega: ")
        cadastrar_pedido(cliente, itens_pedido, data_entrega)
    elif escolha == "3":
        print('Estoque:')
        linha_vazia()
        exibir_estoque()
        linha_vazia()
        separador()
    elif escolha == "4":
        exibir_pedidos()
    elif escolha == "5":
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Escolha novamente.")
