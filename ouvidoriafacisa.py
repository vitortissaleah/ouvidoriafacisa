#Vitor Tissaleah Bezerra Vasconcelos
#Maria Luiza Cavalanti
#Henrique Albuquerque Araújo
#Iasmin Amorim Torquato
#Isabela Vitoriano Sena de Sousa
#Igor Gomes Batista dos Santos


from metodosouvidoria import *

conexao = abrirBancoDados('localhost','root', 'root', 'bdouvidoria')

opcao = 6

while opcao != 5:

    menu()
    opcao = int(input('Digite sua opção: '))

    if opcao == 1:

        opcaoListar = 5
        while opcaoListar != 4:
            menuListar()
            opcaoListar = int(input("Digite sua opção:"))

            if opcaoListar == 1:
                print()
                listaTodasOcorrencias(conexao)

            elif opcaoListar == 2 :
                print()
                listaTodosElogios(conexao)

            elif opcaoListar == 3:
                print()
                listaTodasReclamacoes(conexao)

            elif opcaoListar <= 0 or opcao > 4:
                print()
                print("Não existe essa opção.")
                print()

    elif opcao == 2:

        novaOcorrencia(conexao)
        print("-Adicionado com sucesso!")
        print()
        listaTodasOcorrencias(conexao)

    elif opcao == 3:
        pesquisarOcorrenciaPeloCodigo(conexao)

    elif opcao == 4:

        print()
        removerReclamacao(conexao)
        print()
        listaTodasOcorrencias(conexao)

    elif opcao == 5:
        break

    elif opcao <= 0 or opcao > 5:
        print("Não existe essa opção")

print('Obrigado, volte sempre!!')
encerrarBancoDados(conexao)
