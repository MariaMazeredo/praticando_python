#1

clientes = ["João", "Maria", "Carlos", "Ana", "Beatriz"]
for cliente in clientes:
    print(cliente)

#2

contador = 0

while contador < 10:
    print("Processando dados...")
    contador += 1 

#3 Ajude Marcos a escrever um programa que exiba a mensagem: "Bem-vindo ao Buscante!" o número exato de vezes que ele precisa.

num_repeticoes = int(input("Digite o número de vezes que deseja exibir a mensagem: "))
for i in range(num_repeticoes):
    print("Bem-vindo ao Buscante!")

#4

valores = [10, 20, 30, 40, 50]
soma = 0
for valor in valores:
    soma += valor
print("A soma dos valores é:", soma)

#5 Crie um programa que ajude Ana a percorrer a lista de projetos e exiba os nomes dos projetos válidos. Se encontrar um item None, o programa deve exibir a mensagem: "Projeto ausente".

projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]
for projeto in projetos:
    if projeto is None:
        print("Projeto ausente")
    else:
        print(projeto)

#6

livros = ["1984", "Dom Casmurro", "O Pequeno Príncipe", "O Hobbit", "Orgulho e Preconceito"]
for livro in livros:
    if livro == "O Hobbit":
        print(f"Livro encontrado: {livro}")
        break

#7

estoque = 5

while estoque > 0:
    estoque -= 1
    print(f"Produto vendido. Itens restantes no estoque: {estoque}")

print("Estoque esgotado.")

#8

for segundos in range(10, 0, -1):  
    if segundos % 2 == 0: 
        print(f"Faltam apenas {segundos} segundos - Não perca essa oportunidade!")
    else: 
        print(f"A contagem continua: {segundos} segundos restantes.")

print("Aproveite a promoção agora!")

#9

livros = [
    {"nome": "1984", "estoque": 5},
    {"nome": "Dom Casmurro", "estoque": 0},
    {"nome": "O Pequeno Príncipe", "estoque": 3},
    {"nome": "O Hobbit", "estoque": 0},
    {"nome": "Orgulho e Preconceito", "estoque": 2}
]

for livro in livros:
    if livro["estoque"] > 0:
        print(f"O livro '{livro['nome']}' está disponível.")
    else:
        print(f"O livro '{livro['nome']}' está esgotado.")

#10 Validação de entrada para login

while True:
    nome_usuario = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")
    if len(nome_usuario) < 5:
        print("O nome de usuário deve ter pelo menos 5 caracteres.")
        continue

    if len(senha) < 8:
        print("A senha deve ter pelo menos 8 caracteres.")
        continue

    print("Cadastro realizado com sucesso!")
    break

