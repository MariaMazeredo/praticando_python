# domain/lacos.py

def listar_clientes(clientes):
    """Retorna a lista de clientes."""
    return clientes


def processar_dados(qtd_processos=10):
    """Simula processamento de dados."""
    mensagens = []
    contador = 0
    while contador < qtd_processos:
        mensagens.append(f"Processando dados... {contador + 1}")
        contador += 1
    return mensagens


def repetir_mensagem(mensagem, vezes):
    """Repete uma mensagem o número de vezes indicado."""
    return [mensagem for _ in range(vezes)]


def soma_valores(valores):
    """Soma todos os valores de uma lista."""
    return sum(valores)


def listar_projetos(projetos):
    """Exibe nomes válidos e marca 'Projeto ausente' quando None."""
    return ["Projeto ausente" if p is None else p for p in projetos]

livros = ["1984", "Dom Casmurro", "O Pequeno Príncipe", "O Hobbit", "Orgulho e Preconceito"]
for livro in livros:
    if livro == "O Hobbit":
        print(f"Livro encontrado: {livro}")
        break


def vender_estoque(estoque):
    """Simula vendas até o estoque acabar."""
    mensagens = []
    while estoque > 0:
        estoque -= 1
        mensagens.append(f"Produto vendido. Itens restantes: {estoque}")
    mensagens.append("Estoque esgotado.")
    return mensagens


def contagem_regressiva(segundos_iniciais):
    """Retorna mensagens de contagem regressiva."""
    mensagens = []
    for segundos in range(segundos_iniciais, 0, -1):
        if segundos % 2 == 0:
            mensagens.append(f"Faltam apenas {segundos} segundos - Não perca essa oportunidade!")
        else:
            mensagens.append(f"A contagem continua: {segundos} segundos restantes.")
    mensagens.append("Aproveite a promoção agora!")
    return mensagens


def verificar_estoque_livros(livros):
    """Verifica disponibilidade de livros."""
    mensagens = []
    for livro in livros:
        if livro["estoque"] > 0:
            mensagens.append(f"O livro '{livro['nome']}' está disponível.")
        else:
            mensagens.append(f"O livro '{livro['nome']}' está esgotado.")
    return mensagens


def validar_login(nome_usuario, senha):
    """Valida nome e senha e retorna mensagens de erro ou sucesso."""
    if len(nome_usuario) < 5:
        return "O nome de usuário deve ter pelo menos 5 caracteres."
    if len(senha) < 8:
        return "A senha deve ter pelo menos 8 caracteres."
    return "Cadastro realizado com sucesso!"
