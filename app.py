from getpass import getpass
import os


def cadastrarUsuario():
    usuario = input('Digite o usuario: ')
    senha = getpass('Digite a senha: ')
    with open('usuario.txt', 'a', newline='') as arquivo:
        arquivo.write(f'{usuario},')
        arquivo.write(f'{senha}')
        arquivo.close()
    print('CADASTRO REALIZADO COM SUCESSO!\n')

def loginUsuario():
    validar = 0
    escolher = 'n'
    while True:
        usuario = input('Digite o login: ')
        senha = getpass('Digite a senha do login: ')
        with open('usuario.txt', 'r') as arquivo:
            for linha in arquivo:
                usuario_senha = list(linha.split(','))
            
                if usuario in usuario_senha and senha in usuario_senha:
                    print('LOGIN REALIZADO COM SUCESSO!\n')
                    validar = 1

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
   
    print('SISTEMA DE LOGIN - Digite "0" para sair')
    print('[1] - EFETUAR O LOGIN')
    print('[2] - REALIZAR O CADASTRO')
    opcao = int(input('Digite a sua opção: '))
    if opcao ==0:
        break
    if opcao == 1:
        loginUsuario()
    elif opcao == 2:
        cadastrarUsuario()
    


