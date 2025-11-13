from use_cases.executar_funcoes import testar_funcoes
from use_cases.testar_condicionais import testar_condicionais
from use_cases.rodar_lacos import testar_lacos

def iniciar():
    print("=== Menu de Prática Python ===")
    print("1 - Testar Funções")
    print("2 - Testar Condicionais")
    print("3 - Testar Laços")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        resultado, mensagem = testar_funcoes()
        print(f"Soma: {resultado}, Mensagem: {mensagem}")
    elif opcao == "2":
        print(testar_condicionais())
    elif opcao == "3":
        print(testar_lacos())
    else:
        print("Opção inválida!")
