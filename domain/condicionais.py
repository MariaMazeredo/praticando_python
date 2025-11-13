def comparar_vendas(vendas_maca, vendas_banana):
    if vendas_maca > vendas_banana:
        return "As maçãs venderam mais."
    elif vendas_banana > vendas_maca:
        return "As bananas venderam mais."
    else:
        return "Houve empate nas vendas."


def verificar_tempo_atividades(a, b, c):
    tempo_total = a + b + c
    if a <= 0 or b <= 0 or c <= 0:
        return "Erro: O número de dias deve ser maior que zero."
    else:
        return f"O tempo total para completar todas as atividades é de {tempo_total} dias."


def verificar_temperatura(temp):
    if temp <= 25:
        return "A temperatura está dentro do intervalo aceitável."
    else:
        return "A temperatura está fora do intervalo aceitável."


def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"


def verificar_orcamento(despesas, limite=3000):
    if despesas > limite:
        return "Você ultrapassou o limite do orçamento."
    else:
        return "Você está dentro do orçamento."


def verificar_acesso(hora):
    if 8 <= hora <= 18:
        return "Acesso permitido."
    else:
        return "Acesso negado."


def calcular_media(n1, n2, n3):
    media = (n1 + n2 + n3) / 3
    if media >= 7:
        return "Aprovado"
    elif 5 <= media < 7:
        return "Recuperação"
    else:
        return "Reprovado"


def calcular_pedagio(distancia):
    if distancia <= 100:
        return "O valor do pedágio é R$ 10,00."
    elif distancia <= 200:
        return "O valor do pedágio é R$ 20,00."
    else:
        return "O valor do pedágio é R$ 30,00."


def verificar_par_ou_impar(numero):
    return "Par" if numero % 2 == 0 else "Ímpar"


def aprovar_emprestimo(renda, parcela):
    if renda < 2000:
        return "Empréstimo negado. Renda insuficiente."
    elif parcela > 0.3 * renda:
        return "Empréstimo negado. Parcela acima do limite."
    else:
        return "Empréstimo aprovado."