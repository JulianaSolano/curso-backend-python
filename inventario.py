print ("--- Controle de Inventário Básico ---")
produtos = {}

while True:
    print("\n=== MENU PRINCIPAL ===")
    print("1. Adicionar Itens")
    print("2. Remover Item")
    print("3. Listar Inventário")
    print("4. Sair")

    opcao = input("Escolha uma opção (1-4): ")

    if opcao == '1':
        nome = input("Nome do produto: ")
        quantidade = int(input("Quantidade: "))
        produtos[nome] = produtos.get(nome, 0) + quantidade

        print("Item adicionado com sucesso!")

    elif opcao == "2":
        nome = input("Nome do item a ser removido: ")
        if nome in produtos:
            del produtos[nome]
            print("Item removido com sucesso!")
        else:
            print("Item não encontrado no inventário.")

    elif opcao == "3":
        if not produtos:
            print("O inventário está vazio.")
        else:
            print("\n--- Inventário Atual ---")
            for nome, quantidade in produtos.items():
                print(f"{nome}: {quantidade}")

    elif opcao == "4":
        print("Saindo. Até mais!")
        break