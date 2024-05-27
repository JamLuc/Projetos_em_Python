import os

#restaurantes = ['Burger King', 'Pizza Hut']
restaurantes = [{'nome' : 'Sabores do Mundo',  'categoria' : 'Francesa Bistrô, Creperia', 'ativo' : False },
                {'nome' : 'Aromas e Sabores',  'categoria' : 'Vegetariana Indiana', 'ativo' : True },
                {'nome' : 'Casa da Sopa',  'categoria' : 'Mexicana Tacos, Burritos', 'ativo' : False },
                {'nome' : 'Padaria Pão Doce',  'categoria' : 'Argentina Parrilla, Empanadas', 'ativo' : True }]


def exibir_name_do_programa():
    
    print("""
╔═══╗─────╔╗──────────────╔╗───────╔════╗───────╔╗
║╔═╗║────╔╝╚╗────────────╔╝╚╗──────║╔╗╔╗║──────╔╝╚╗
║╚═╝╠══╦═╩╗╔╬══╦╗╔╦═╦══╦═╬╗╔╬══╦══╗╚╝║║╠╩═╦╗╔╦═╩╗╔╬╦══╦══╦══╗
║╔╗╔╣║═╣══╣║║╔╗║║║║╔╣╔╗║╔╗╣║║║═╣══╣──║║║║═╣╚╝║╔╗║║╠╣╔═╣╔╗║══╣
║║║╚╣║═╬══║╚╣╔╗║╚╝║║║╔╗║║║║╚╣║═╬══║──║║║║═╣║║║╔╗║╚╣║╚═╣╚╝╠══║
╚╝╚═╩══╩══╩═╩╝╚╩══╩╝╚╝╚╩╝╚╩═╩══╩══╝──╚╝╚══╩╩╩╩╝╚╩═╩╩══╩══╩══╝""")


def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizando_app():
    os.system('cls')
    print('Finalizando o aplicativo')

def voltar_ao_menu_principal():
    os.system('cls')
    input('\nDigite qualquer tecla e perte enter para voltar ao menu principal')
    

    
def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)    

def opcao_invalida():
    print('Opção inválida, tente novamente.\n')
    input('\nDigite qualquer tecla e perte enter para voltar ao menu principal')
    main()

def cadastrar_novo_restaurante():
    os.system('cls')
    print('Cadastro de novos restaurantes\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}')
    
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    input('Digite qualquer tecla e perte enter para voltar ao menu principal')
    main()
    

def listar_restaurantes():
    os.system('cls')
    print('Listando os restauranttes')
    
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']

        categoria = restaurante['categoria']
        ativo = restaurante['ativo']
        
        print(f'.{nome_restaurante} | {categoria} | {ativo}')
    input('Digite qualquer tecla e perte enter para voltar ao menu principal')
    main()



def alternar_estado_restaurante():
    exibir_subtitulo('Alternando o estado do restaurante')
    
    nome_restaurante = input('Digite o nome do restaurante que deseja altenar o estado:  ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} 
            foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')        
    voltar_ao_menu_principal()
    
    
    
def escolhar_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
            #print('Cadastrar restaurante')
        elif opcao_escolhida == 2:
            listar_restaurantes()
            #print('Listar restaurantes')
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
            #print('Ativar restaurantes')
        elif opcao_escolhida == 4:
            finalizando_app()        
        else:
            opcao_invalida()
    except:
        opcao_invalida()        
    
def main():
    os.system('cls')
    exibir_name_do_programa()
    exibir_opcoes()
    escolhar_opcao()
        
    
if __name__ == '__main__':
    main()    
    
    

    
