import os

restaurantes = [{'nome':"Dio's Café & Pizza", 'categoria':'Pizza', 'ativo':False},
                {'nome':"Cazum's Pudding & Co.", 'categoria':'Doceria', 'ativo':True},
                {'nome':"Xaulinho Cozinhador De Porco", 'categoria':'Churrascaria', 'ativo':False}]

def nome_programa():
    '''Exibe o nome do programa'''
    print('𝑆𝑎𝑏𝑜𝑟 𝐸𝑥𝑝𝑟𝑒𝑠𝑠\n')

def options():   
    '''Exibe as opções disponíveis para escolher'''
    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. Alternar polaridade do estado restaurante")
    print("4. Sair\n")

def subtitulo(textinhi):
    '''Limpa a tela para a próxima ação'''
    os.system('cls')
    linha = '-' * (len(textinhi))
    print(linha)
    print(textinhi)
    print(linha)
    print()

def retorno():
    input("\nDigitar uma tecla qualquer para retornar ao menu inical. ")
    main()

def cadastrar():
    '''Cadastra um novo restaurante e registra ele na lista'''
    subtitulo('Cadastro de novos restaurantes.')
    #nomeR = nome do restaurante
    nomeR = input("Digite o nome do restaurante a ser cadastrado: ")
    categoria = input(f'Digite o nome da categoria do restaurante {nomeR}: ')
    dadox = {'nome':nomeR, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dadox)
    print(f'Restaurante "{nomeR}" cadastrado com sucesso!')
    retorno()

def listar():
    '''Exibe todos os restaurantes na lista'''
    subtitulo('Lista dos restaurantes já cadastrados:')
    print(f'{'Nome do restaurante'.ljust(42)} | {'Categoria'.ljust(40)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(40)} | {categoria.ljust(40)} | {ativo}')
    retorno()

def alternar_estado():
    '''Inverte a polaridade do estado do restaurante'''
    subtitulo('Alterando a polaridade do estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado.')
    retorno()

def finalizar_app():
    '''Auto explicativo'''
    subtitulo('Finalizando o app...')

def invalido():
    '''Declara inválida a opção escolhida e retorna para options()'''
    os.system('cls')
    print("Opção inválida!")
    retorno()

def escolha():
    '''Detecta a escolha do usuário e da uma resposta'''
    try:
        choice = int(input("Escolha uma opção: "))
        if choice == 1:
            cadastrar()
        elif choice == 2:
            listar()
        elif choice == 3:
            alternar_estado()
        elif choice ==4:
            finalizar_app()
        else:
            invalido()
    except:
        invalido()

def main():
    '''Exibe as funções básicas'''
    os.system('cls')
    nome_programa()
    options()
    escolha()

if __name__ == "__main__":
    main()


