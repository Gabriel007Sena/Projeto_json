import json


def carregar_dados():
    try:
        with open('bd.json', 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []


def salvar_dados(dados):
    with open('dados.json', 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)

def inserir_produto(dados):
    codigo = input("Digite o código do produto: ")
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    
    novo_produto = {
        'codigo': codigo,
        'nome': nome,
        'preco': preco
    }
    
    for produto in dados:
        if produto['codigo'] == codigo:
            print("Erro: Código de produto duplicado. O produto não foi inserido.")
            return
    
    dados.append(novo_produto)
    salvar_dados(dados)
    print("Produto inserido com sucesso!")


def consultar_produto(dados):
    codigo = input("Digite o código do produto que deseja consultar: ")
    
    for produto in dados:
        if produto['codigo'] == codigo:
            print("Código:", produto['codigo'])
            print("Nome:", produto['nome'])
            print("Preço:", produto['preco'])
            return
    
    print("Produto não encontrado.")


def consultar_todos(dados):
    if not dados:
        print("Nenhum produto cadastrado.")
        return
    
    for produto in dados:
        print("Código:", produto['codigo'])
        print("Nome:", produto['nome'])
        print("Preço:", produto['preco'])
        print()


def alterar_preco(dados):
    codigo = input("Digite o código do produto que deseja alterar o preço: ")
    novo_preco = float(input("Digite o novo preço: "))
    
    for produto in dados:
        if produto['codigo'] == codigo:
            produto['preco'] = novo_preco
            salvar_dados(dados)
            print("Preço alterado com sucesso!")
            return
    
    print("Produto não encontrado.")


def aplicar_acrescimo_desconto(dados):
    percentual = float(input("Digite o percentual de acréscimo  ou desconto (-): "))
    
    for produto in dados:
        produto['preco'] *= (1 + percentual / 100)
    
    salvar_dados(dados)
    print("Acréscimo/desconto aplicado com sucesso!")


def excluir_produto(dados):
    codigo = input("Digite o código do produto que deseja excluir: ")
    
    for produto in dados:
        if produto['codigo'] == codigo:
            dados.remove(produto)
            salvar_dados(dados)
            print("Produto excluído com sucesso!")
            return
    
    print("Produto não encontrado.")


def main():
    dados = carregar_dados()
    
    while True:
        print("Menu de Opções:")
        print("1. Inserir um novo produto: ")
        print("2. Consultar um produto por código: ")
        print("3. Consultar todos os produtos: ")
        print("4. Alterar o preço de um determinado produto: ")
        print("5. Aplicar um acréscimo ou desconto em todos os produtos: ")
        print("6. Excluir um registro de produto: ")
        print("7. Sair do programa: ")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            inserir_produto(dados) 
        elif opcao == '2':
            consultar_produto(dados) 
        elif opcao == '3':
            consultar_todos(dados) 
        elif opcao == '4':
            alterar_preco(dados)
        elif opcao == '5':
            aplicar_acrescimo_desconto(dados) 
        elif opcao == '6':
            excluir_produto(dados) 
        elif opcao == '7':
            salvar_dados(dados) 
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__": 
    main()
