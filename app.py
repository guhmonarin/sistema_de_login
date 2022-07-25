from getpass import getpass


def cadastrarUsuario():
    usuario = input('Digite o usuario: ')
    senha = getpass('Digite a senha: ')
    arquivo = open('usuario.txt', 'a')
    arquivo.write(f'{usuario},')
    arquivo.write(f'{senha}')
    arquivo.write(f'\n')
    arquivo.close()
    print('CADASTRO REALIZADO COM SUCESSO!\n')

def loginUsuario():
    validar = 0
    arquivo = open('usuario.txt', 'r', encoding='utf-8') 
    while True:
        usuario = input('Digite o login: ')
        senha = getpass('Digite a senha do login: ')
        for linha in arquivo:
            usu,sen = linha.split(',')
            print(f'{usu}')
            print(f'{sen}')
            if usuario == usu and senha == sen:
                print('LOGIN REALIZADO COM SUCESSO!')
                validar = 1
                break
        if validar == 0:
            print('USUARIO NÃO ENCONTRADO OU DADOS DIGITADO INCORRETO!')
            escolher = input('Deseja tentar novamente ? (s/n): ')
        
        if escolher == 'n':
            break
        
        if validar == 1:
            break

        
    arquivo.close()

def Linhas():
    print('-'*50)

while True:
   
    print('SISTEMA DE LOGIN')
    print('[1] - EFETUAR O LOGIN')
    print('[2] - REALIZAR O CADASTRO')
    opcao = int(input('Digite a sua opção: '))

    if opcao == 1:
        loginUsuario()
    elif opcao == 2:
        cadastrarUsuario()
    


