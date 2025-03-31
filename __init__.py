from sys import exit
from Ex115.arquivo import *

def menuprincial():
    print('-'*40)
    print('MENU PRINCIPAL'.center(40))
    print('-'*40)
    print('1- Ver Pessoas Cadastradas\n2- Cadastrar Nova Pessoa\n3- Sair do Sistema')
    print('-'*40)

def menu():
    arq = 'pessoas.txt'
    if not ArquivoExiste(arq):
        CriarArquivo(arq)
    while True:
        try:
            menuprincial()
            resp = int(input('Opção: '))
        except (TypeError,ValueError):
            print('ERRO!! Digite Uma Opção Válida.')
            continue
        except KeyboardInterrupt:
            exit()
        else:
            if resp == 1: # Lista o arquivo
                print('-'*40)
                LerArquivo(arq)
            elif resp == 2: #cadastra pessoas novas no arquivo
                while True:
                    try:
                        print('-'*40)
                        print('Novo Cadastro'.center(40))
                        nome= str(input('Nome: ')).strip().capitalize()
                        idade = int(input('Idade: '))
                        Cadastrar(arq, nome, idade)
                    except (TypeError, ValueError):
                        print('ERRO!! Digite Nome/Idade Válidos.')
                        continue
                    else:
                        print('Cadastro Finalizado.')
                        break
            elif resp == 3:
                print('Saindo Do Sistema...')
                exit()
            else: print('ERRO! Digite Uma Opção Válida.')