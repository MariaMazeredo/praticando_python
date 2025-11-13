from domain.lacos import (
    listar_clientes,
    processar_dados,
    repetir_mensagem,
    soma_valores,
    listar_projetos,
    buscar_livro,
    vender_estoque,
    contagem_regressiva,
    verificar_estoque_livros,
    validar_login
)


def testar_lacos():
    print("\n--- Exercício 1: Listar Clientes ---")
    qtd_clientes = int(input("Quantos clientes deseja cadastrar? "))
    clientes = [input(f"Digite o nome do cliente {i + 1}: ") for i in range(qtd_clientes)]
    print("Clientes cadastrados:")
    print(listar_clientes(clientes))

    print("\n--- Exercício 2: Processar Dados ---")
    qtd = int(input("Quantos processos deseja simular? "))
    for msg in processar_dados(qtd):
        print(msg)

    print("\n--- Exercício 3: Repetir Mensagem ---")
    mensagem = input("Digite a mensagem a ser repetida: ")
    vezes = int(input("Quantas vezes deseja repetir? "))
    for msg in repetir_mensagem(mensagem, vezes):
        print(msg)

    print("\n--- Exercício 4: Somar Valores ---")
    qtd_valores = int(input("Quantos valores deseja somar? "))
    valores = [float(input(f"Digite o valor {i + 1}: ")) for i in range(qtd_valores)]
    print("Soma =", soma_valores(valores))

    print("\n--- Exercício 5: Listar Projetos ---")
    qtd_projetos = int(input("Quantos projetos deseja listar? "))
    projetos = []
    for i in range(qtd_projetos):
        nome = input(f"Digite o nome do projeto {i + 1} (ou deixe em branco para ausente): ")
        projetos.append(nome if nome else None)
    for p in listar_projetos(projetos):
        print(p)

    print("\n--- Exercício 6: Buscar Livro ---")
    qtd_livros = int(input("Quantos livros há na biblioteca? "))
    livros = [input(f"Digite o nome do livro {i + 1}: ") for i in range(qtd_livros)]
    nome_buscado = input("Qual livro deseja buscar? ")
    print(buscar_livro(livros, nome_buscado))

    print("\n--- Exercício 7: Vender Estoque ---")
    estoque = int(input("Digite a quantidade inicial em estoque: "))
    for msg in vender_estoque(estoque):
        print(msg)

    print("\n--- Exercício 8: Contagem Regressiva ---")
    segundos = int(input("Digite o número de segundos para a contagem regressiva: "))
    for msg in contagem_regressiva(segundos):
        print(msg)

    print("\n--- Exercício 9: Verificar Estoque de Livros ---")
    qtd = int(input("Quantos livros deseja cadastrar? "))
    livros = []
    for i in range(qtd):
        nome = input(f"Digite o nome do livro {i + 1}: ")
        estoque = int(input(f"Digite o estoque do livro '{nome}': "))
        livros.append({"nome": nome, "estoque": estoque})
    for msg in verificar_estoque_livros(livros):
        print(msg)

    print("\n--- Exercício 10: Validar Login ---")
    nome_usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    print(validar_login(nome_usuario, senha))
    return "Testes de laços concluídos."