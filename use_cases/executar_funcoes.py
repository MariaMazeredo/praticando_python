from domain.funcoes import (
    calcular_idade,
    contar_caracteres,
    saudacao_personalizada,
    converter_telefones,
    verifica_tipos,
    calcular_desconto,
    soma_recursiva
)

def testar_funcoes():
    print("\n--- Exercício 1: Calcular Idade ---")
    ano_nasc = int(input("Digite o ano de nascimento: "))
    ano_atual = int(input("Digite o ano atual: "))
    print("A idade é:", calcular_idade(ano_nasc, ano_atual))

    print("\n--- Exercício 2: Contar Caracteres ---")
    palavra = input("Digite uma palavra: ")
    print("Quantidade de caracteres:", contar_caracteres(palavra))

    print("\n--- Exercício 3: Saudação Personalizada ---")
    hora = int(input("Digite a hora atual (0–23): "))
    nome = input("Digite seu nome: ")
    print(saudacao_personalizada(hora, nome))

    print("\n--- Exercício 4: Converter Telefones ---")
    telefones = input("Digite os números de telefone separados por vírgula: ").split(",")
    convertidos = converter_telefones(telefones)
    print(verifica_tipos(convertidos))

    print("\n--- Exercício 5: Soma de Vendas ---")
    valores = input("Digite os valores de vendas separados por espaço: ").split()
    total = sum(map(float, valores))
    print(f"Total de vendas: R$ {total:.2f}")

    print("\n--- Exercício 6: Números Pares ---")
    numeros = input("Digite números separados por espaço: ").split()
    pares = [n for n in numeros if int(n) % 2 == 0]
    print("Números pares:", " ".join(pares))

    print("\n--- Exercício 7: Juntar Listas (Produto e Preço) ---")
    produtos = input("Digite os produtos separados por vírgula: ").split(",")
    precos = input("Digite os preços separados por vírgula: ").split(",")
    for p, preco in zip(produtos, precos):
        print(f"{p.strip()}: R$ {preco.strip()}")

    print("\n--- Exercício 8: Operações Matemáticas ---")
    x = float(input("Primeiro número: "))
    y = float(input("Segundo número: "))
    operador = input("Operador (+, -, *, /): ") 
    operacoes = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b if b != 0 else "Erro: divisão por zero"
    }
    if operador in operacoes:
        print("Resultado:", operacoes[operador](x, y))
    else:
        print("Operador inválido.")

    print("\n--- Exercício 9: Função de Desconto (Closure) ---")
    desconto = float(input("Digite a porcentagem de desconto: "))
    preco = float(input("Digite o preço do produto: "))
    aplicar = calcular_desconto(desconto)
    print(f"Preço final: R$ {aplicar(preco):.2f}")

    print("\n--- Exercício 10: Soma Recursiva ---")
    n = int(input("Digite um número inteiro positivo: "))
    print(f"Soma de 1 até {n} = {soma_recursiva(n)}")

    print("\n--- Fim dos Exercícios de Funções ---")
    return total, f"Exercícios de funções concluídos com sucesso!"
