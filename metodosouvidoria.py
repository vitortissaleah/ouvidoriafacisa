
from operacoesbd import *

def menuListar():
        print(" Digite (1) Listar todas ocorrências.")
        print(" Digite (2) Listar todos elogios.")
        print(" Digite (3) Listar todas reclamações.")
        print(" Digite (4) Sair.")


def menu():
    print()
    print("1) Listar ocorrências: ")
    print("2) Adicionar nova ocorrência: ")
    print("3) Pesquisar pelo código da ocorrência: ")
    print("4) Remover ocorrências: ")
    print("5) Sair: ")



def listaTodasOcorrencias(conexao):

    print('OUVIDORIA FACISA | OCORRÊNCIAS:')
    print()

    consultaListagemOcorrencias = 'select * from ouvidoriafacisa'
    listaTodasOcorrencias = listarBancoDados(conexao, consultaListagemOcorrencias)

    for i in listaTodasOcorrencias:
        print('-Código DA Ocorrência:', i[0])
        print('-', i[1], ':', i[2])
        print()
        if len(listaTodasOcorrencias) == 0:
                print('Não existem ocorrências a serem exibido.')

def listaTodosElogios(conexao):

    consultaOcorrenciaElogio = 'select * from ouvidoriafacisa where tipo = "elogio"'
    listaTodosElogios= listarBancoDados(conexao, consultaOcorrenciaElogio)

    for i in listaTodosElogios:
        if len(listaTodosElogios) == 0:
            print('Não existem elogios a serem exibido.')
        else:
            for elogio in listaTodosElogios:
                print('-Código da Ocorrência:', elogio[0])
                print('-', elogio[1], ':', elogio[2])
                print()


def listaTodasReclamacoes(conexao):

    consultaListagemReclamacoes = 'select * from ouvidoriafacisa where tipo = "reclamação"'
    listaTodasReclamacoes = listarBancoDados(conexao, consultaListagemReclamacoes)

    for reclamacao in listaTodasReclamacoes:
        print('-Código da Ocorrência:', reclamacao[0])
        print('-', reclamacao[1], ':', reclamacao[2])
        print()


def novaOcorrencia(conexao):

    tipoOcorrencia = 4
    while tipoOcorrencia != 3:
        print(" Digite (1) para elogio.")
        print(" Digite (2) para reclamação.")
        print(" Digite (3) para sair.")
        print()
        tipoOcorrencia = int(input("Qual o tipo da sua ocorrência: "))

        if tipoOcorrencia == 1:
            elogio = "Elogio"
            novaOcorrencia = input('Digite sua ocorrência: ')
            consultaNovaReclamacao = 'insert into ouvidoriafacisa(tipo, descrição_ocorrências)values(%s,%s)'
            dados = (elogio, novaOcorrencia)
            insertNoBancoDados(conexao, consultaNovaReclamacao, dados)
            print("Elogio adicionado com sucesso!")
            print()
        elif tipoOcorrencia == 2:
            reclamacao = "Reclamação"
            novaOcorrencia = input('Digite sua ocorrência: ')
            consultaNovaReclamacao = 'insert into ouvidoriafacisa(tipo, descrição_ocorrências)values(%s,%s)'
            dados = (reclamacao, novaOcorrencia)
            insertNoBancoDados(conexao, consultaNovaReclamacao, dados)
            print("Reclamação adicionado com sucesso!")
            print()

def pesquisarOcorrenciaPeloCodigo(conexao):
    consultaListagemOcorrencias = 'select * from ouvidoriafacisa'
    listaTodasOcorrencias = listarBancoDados(conexao, consultaListagemOcorrencias)

    for i in listaTodasOcorrencias:
        print('-CÓDIGO DA Ocorrência:', i[0])
        print('-',i[1], ':',i[0])
        print()

    print("|PESQUISE PELO CODIGO| ")
    codigo = input('digite o codigo:')
    print()
    consultaReclamacaoCodigo = 'select * from ouvidoriafacisa where codigo_ocorrências=' + codigo
    listaOcorrencias = listarBancoDados(conexao, consultaReclamacaoCodigo)

    for i in listaOcorrencias:
        if len(listaOcorrencias) == 0:
            print('Não existem reclamações a serem exibido.')
        else:
            for i in listaOcorrencias:
                print('- CÓDIGO DA RECLAMAÇÃO:', i[0])
                print('-',i[1],':',i[2])
                print()

def removerReclamacao(conexao):
    opcao = 4
    while opcao != 3:
        print(" Digite (1) Remover ocorrência pelo código.")
        print(" Digite (2) Remover todas ocorrência.")
        print(" Digite (3) Voltar.")
        opcao = int(input("Digite sua opção:"))

        if opcao == 1 :
            codigo =  int(input('Digite o codigo da reclamação a ser removido: '))
            consultaRemoverOcorrenciaCodigo = 'delete from ouvidoriafacisa where codigo_ocorrências = %s '
            dados = (codigo,)
            linhasExcluidas = excluirBancoDados(conexao, consultaRemoverOcorrenciaCodigo, dados)

            if linhasExcluidas == 0:
                print('Não existe o código informado na base de dados. ')
            elif linhasExcluidas == 1:
                print('Reclamação removida com sucesso! ')


        elif opcao == 2:
            consultaRemoverReclamacao = ' delete from ouvidoriafacisa; '
            excluirBancoDados(conexao, consultaRemoverReclamacao)


        elif opcao  <= 0 or opcao > 3:
            print("Não existe essa opção. ")

