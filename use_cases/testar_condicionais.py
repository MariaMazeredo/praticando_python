from domain.condicionais import (
    comparar_vendas,
    verificar_tempo_atividades,
    verificar_temperatura,
    calcular_imc,
    verificar_orcamento,
    verificar_acesso,
    calcular_media,
    calcular_pedagio,
    verificar_par_ou_impar,
    aprovar_emprestimo
)

def testar_condicionais():
    print("\n--- Exercício 1: Comparar Vendas ---")
    vendas_maca = int(input("Digite as vendas de maçãs: "))
    vendas_banana = int(input("Digite as vendas de bananas: "))
    print(comparar_vendas(vendas_maca, vendas_banana))

    print("\n--- Exercício 2: Tempo de Atividades ---")
    a = int(input("Dias da atividade A: "))
    b = int(input("Dias da atividade B: "))
    c = int(input("Dias da atividade C: "))
    print(verificar_tempo_atividades(a, b, c))

    print("\n--- Exercício 3: Verificar Temperatura ---")
    temp = float(input("Digite a temperatura atual: "))
    print(verificar_temperatura(temp))

    print("\n--- Exercício 4: Calcular IMC ---")
    peso = float(input("Digite seu peso (kg): "))
    altura = float(input("Digite sua altura (m): "))
    print(calcular_imc(peso, altura))

    print("\n--- Exercício 5: Verificar Orçamento ---")
    despesas = float(input("Digite o valor total das despesas: "))
    print(verificar_orcamento(despesas))

    print("\n--- Exercício 6: Verificar Acesso ---")
    hora = int(input("Digite a hora atual (0–23): "))
    print(verificar_acesso(hora))

    print("\n--- Exercício 7: Média Final ---")
    n1 = float(input("Digite a 1ª nota: "))
    n2 = float(input("Digite a 2ª nota: "))
    n3 = float(input("Digite a 3ª nota: "))
    print(calcular_media(n1, n2, n3))

    print("\n--- Exercício 8: Calcular Pedágio ---")
    distancia = float(input("Digite a distância percorrida (km): "))
    print(calcular_pedagio(distancia))

    print("\n--- Exercício 9: Verificar Par ou Ímpar ---")
    numero = int(input("Digite um número: "))
    print(verificar_par_ou_impar(numero))

    print("\n--- Exercício 10: Aprovar Empréstimo ---")
    renda = float(input("Digite sua renda mensal: "))
    parcela = float(input("Digite o valor da parcela desejada: "))
    print(aprovar_emprestimo(renda, parcela))
    return "Testes de condicionais concluídos."
