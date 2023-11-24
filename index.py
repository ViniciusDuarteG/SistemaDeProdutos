
#codigo do produto:produto
produtos_cadastrados = {}

#produto:valor 
preco_produtos = {}

escolha = 9

def SistemaDeCadastro():
    codigo_produto=int(input("Digite o código do produto: "))
    nome_produto=str(input("Nome do produto: ")).upper()
    valor_produto=str(input("Preço: R$"))
    produtos_cadastrados[codigo_produto] = nome_produto
    preco_produtos[codigo_produto] = valor_produto
    
def SistemaDeAtualização():
    codigo_pesquisa = int(input("Digite o código de pesquisa: "))
    produtos_cadastrados.pop(codigo_pesquisa)
    preco_produtos.pop(codigo_pesquisa)
    
    nome_produto=str(input("Nome do produto: ")).upper()
    valor_produto=str(input("Preço: R$"))
    produtos_cadastrados[codigo_pesquisa] = nome_produto
    preco_produtos[codigo_pesquisa] = valor_produto


while escolha != 0:
    escolha = int(input("O que deseja fazer?\n1-CADASTRAR NOVO PRODUTO\n2-VER PRODUTOS CADASTRADOS\n3-EXCLUIR PRODUTOS\n4-ATUALIZAR PRODUTOS\n0-SAIR\n\n"))
    if escolha == 1:
        SistemaDeCadastro()
    
    elif escolha == 2:
        codigo_pesquisa = int(input("Digite o código de pesquisa: "))
        print("Produto: ",produtos_cadastrados[codigo_pesquisa])
        print("Valor R$",preco_produtos[codigo_pesquisa])
    
    elif escolha == 3:
        codigo_pesquisa = int(input("Digite o código de pesquisa: "))
        produtos_cadastrados.pop(codigo_pesquisa)
        preco_produtos.pop(codigo_pesquisa)
        
    elif escolha == 4:
        SistemaDeAtualização()
        
        
