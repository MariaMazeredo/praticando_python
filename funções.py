#1 criar uma função que receba o ano de nascimento e o ano atual e retorne à idade correspondente.

def calcular_idade(ano_nascimento, ano_atual):
    idade = ano_atual - ano_nascimento
    return idade

#uso da função

ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))
idade = calcular_idade(int(ano_nascimento), int(ano_atual))
print("A idade é:", idade)

#2 Ajude Sara criando uma função que receba uma palavra e exiba a quantidade de caracteres.

def contar_caracteres(palavra):
    return len(palavra)

#uso da função

palavra = input("Digite uma palavra: ")
quantidade = contar_caracteres(palavra)
print("A quantidade de caracteres na palavra é:", quantidade)

#3

def saudacao_personalizada(hora, nome):
    if hora < 12:
        return f"Bom dia, {nome}!"
    elif 12 <= hora < 18:
        return f"Boa tarde, {nome}!"
    else:
        return f"Boa noite, {nome}!"
    
#uso da função

hora= int(input("Digite a hora atual (0-23): "))
nome = input("Digite seu nome: ")
mensagem = saudacao_personalizada(hora, nome)
print(mensagem)

#4 conversão para int


def converter_telefones(lista):  

   return [int(telefone) for telefone in lista] 

def verifica_tipos(lista):  

   for num in lista:  

       if not isinstance(num, int):  

           return "Erro na conversão."  

   return "Todos os números foram convertidos corretamente!" 

telefones = ["11987654321", "21912345678", "31987654321", "11911223344"] 

telefones_convertidos = converter_telefones(telefones) 

print(verifica_tipos(telefones_convertidos)) 

#5 

valores = input("Digite os valores de vendas: ").split()
total = sum(map(float, valores)) 
print(f"O total de vendas foi: {total}") 

#6

numeros = input("Digite os números separados por espaço: ").split() 
pares = filter(lambda x: int(x) % 2 == 0, numeros) 
print("Números pares:", " ".join(pares)) 

#7 Crie um programa que junte as listas e exiba o resultado no formato produto: preço

produtos = input("Digite os produtos separados por vírgula: ").split(",") 
precos = input("Digite os preços separados por vírgula: ").split(",") 
 
for produto, preco in zip(produtos, precos): 
    print(f"{produto.strip()}: {preco.strip()}") 

#8 Sua tarefa é criar um programa usando funções lambda que receba dois números e um operador matemático escolhido pelo usuário (+, -, * ou /) e exiba o resultado correspondente.

operacoes = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y if y != 0 else "Erro: Divisão por zero"
}   

x = float(input("Digite o primeiro número: "))
y = float(input("Digite o segundo número: "))
operador = input("Digite o operador (+, -, *, /): ")
if operador in operacoes:
    resultado = operacoes[operador](x, y)
    print("O resultado é:", resultado)
else:
    print("Operador inválido.")

#9 crie uma closure que gere uma função capaz de calcular o preço final com um desconto fixo definido pelo usuário.

def calcular_desconto(desconto):
    def aplicar_desconto(preco):
        return preco - (preco * desconto / 100)
    return aplicar_desconto

desconto= float(input("Digite a porcentagem de desconto: "))
preco = float(input("Digite o preço do produto: "))
aplicar_desconto = calcular_desconto(desconto)
preco_final = aplicar_desconto(preco)
print(f"O preço final com desconto é: R$ {preco_final:.2f}")

#10 Crie uma função recursiva que receba um número n e retorne a soma de todos os números inteiros de 1 até N.

def soma_recursiva(n):
    if n == 1:
        return 1
    else:
        return n + soma_recursiva(n - 1)
    n = int(input("Digite um número inteiro positivo: "))
    resultado = soma_recursiva(n)
    print(f"A soma de todos os números inteiros de 1 até {n} é: {resultado}")

    



