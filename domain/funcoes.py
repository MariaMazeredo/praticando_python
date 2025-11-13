def calcular_idade(ano_nascimento, ano_atual):
    return ano_atual - ano_nascimento


def contar_caracteres(palavra):
    return len(palavra)


def saudacao_personalizada(hora, nome):
    if hora < 12:
        return f"Bom dia, {nome}!"
    elif hora < 18:
        return f"Boa tarde, {nome}!"
    else:
        return f"Boa noite, {nome}!"


def converter_telefones(lista):
    return [int(telefone) for telefone in lista]


def verifica_tipos(lista):
    for num in lista:
        if not isinstance(num, int):
            return "Erro na conversão."
    return "Todos os números foram convertidos corretamente!"


def soma_recursiva(n):
    if n == 1:
        return 1
    else:
        return n + soma_recursiva(n - 1)


def calcular_desconto(desconto):
    def aplicar_desconto(preco):
        return preco - (preco * desconto / 100)
    return aplicar_desconto


operacoes = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y if y != 0 else "Erro: Divisão por zero"
}