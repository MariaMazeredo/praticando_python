#Crie um programa que receba o número de vendas dos dois produtos e exiba uma mensagem indicando qual deles vendeu mais. Se as quantidades forem iguais, exiba uma mensagem dizendo que houve empate.

vendas_maca = int(input("Digite o número de vendas das maçãs: "))
vendas_bananas = int(input("Digite o número de vendas das bananas: "))

if vendas_maca > vendas_bananas:
    print("As maçãs venderam mais.")
elif vendas_bananas > vendas_maca:
    print("As bananas venderam mais.")
else:
    print("Houve empate nas vendas.")

#2

dias_atividade_A = int(input("Digite o número de dias para a atividade A:")) 
dias_atividade_B = int(input("Digite o número de dias para a atividade B:"))
dias_atividade_C = int(input("Digite o número de dias para a atividade C:"))

tempo_total = dias_atividade_A + dias_atividade_B + dias_atividade_C

if (dias_atividade_A <=0) or (dias_atividade_B <=0) or (dias_atividade_C <=0):
    print("O tempo total para completar todas as atividades é de", tempo_total, "dias.")
else:
    print("Erro: O número de dias para cada atividade deve ser maior que zero.")

#3

temperatura = int(input("Digite a temperatura em graus Celsius: "))
if temperatura <=25:
    print("A temperatura está dentro do intervalo aceitável.")
else:
    print("A temperatura está fora do intervalo aceitável.")

#4 Calcula IMC

peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a altura em metros: "))
imc = peso / (altura ** 2)
if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc < 24.9:
    print("Peso normal")
elif 25 <= imc < 29.9:
    print("Sobrepeso")

#5 O programa deve receber o total de despesas realizadas e informar se ele ultrapassou o limite ou ainda está dentro do orçamento.

despesas = float(input("Digite o total de despezas do mês (R$): "))
limite_orcamento = 3000

if despesas > limite_orcamento:
    print("Você ultrapassou o limite do orçamento.")
else:
    print("Você está dentro do orçamento.")

#6 Permissão para entrar no escritório

hora_de_entrada = int(input("Digite a hora atual (formato 24 horas):  "))
if hora_de_entrada >=8 and hora_de_entrada <=18:
    print("Acesso permitido.")
else:
    print("Acesso negado.")

#7 calcula média final

nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))
nota3 = float(input("Digite a terceira nota:"))
media_final = (nota1+nota2+nota3)/3
if media_final >=7:
    print("Aprovado")
elif 5 <= media_final <7:
    print("Recuperação")
else:
    print("Reprovado")

#8 Calcula pedágio

distancia_percorrida = int(input("Digite a distância percorrida em km: "))
if distancia_percorrida <=100:
    print("O valor do pedágio é R$ 10,00.")
elif distancia_percorrida >100 and distancia_percorrida <=200:
    print("O valor do pedágio é R$ 20,00.")
else:
    print("O valor do pedágio é R$ 30,00.") 
    
#9 Verifica se é par ou ímpar

numero=int(input("Digite um número inteiro: "))
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

#10 Aprovação emprestimo

renda_mensal = int(input("Digite sua renda mensal (R$): "))
valor_parcela= int(input("Digite o valor da parcela desejada (R$): "))
if renda_mensal >= 2000 and valor_parcela <=0.3 * renda_mensal:
    print("Empréstimo aprovado.")
elif renda_mensal < 2000:
    print("Empréstimo negado. Renda mensal insuficiente.")
else:
    print("Empréstimo negado. Valor da parcela excede 30% da renda mensal.")



