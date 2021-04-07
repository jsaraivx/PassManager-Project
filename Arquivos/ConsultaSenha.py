"""
                                Este projeto está sendo desenvolvido inteiramente
                                Por João Saraiva, e eu disponibilizei este projeto
                                Para o público, para que o conhecimento se espalhe 
                                sempre! 
                                 
                                 This project is being developed entirely
                                 By João Saraiva, and I made this project available
                                 For the public, for knowledge to spread
                                 ever!
"""
import time
import os
def consultarsenhassalvas():
    #filtro da rede social a ser buscada.
        print("\t\tOlá, para inciarmos digite o nome da rede social\n" "\t\tque deseja buscar!")
        time.sleep(1)
    #comprovando o nome da rede social a ser buscada.
            #lista de variaveis (redes sociais)
        instagramvar = int
        facebookvar = int 
        githubvar = int
        twittervar = int
        googlevar = int 
        youtubevar = int
        linkedinvar = int
        tiktokvar = int
        snapchatvar = int
        icloudvar = int
        redditvar = int
        micloudvar = int
            #exibição da lista de variaveis
        print("\t\tLISTA DE REDES SOCIAIS SUPORTADAS:\n",
        "\t\t Instagram = 1\n",
        "\t\t Facebook = 2\n",
        "\t\t GitHub = 3\n",
        "\t\t Twitter = 4\n",
        "\t\t Google = 5\n",
        "\t\t Youtube = 6\n",
        "\t\t LinkedIn = 7\n",
        "\t\t Tiktok = 8\n",
        "\t\t SnapChat = 9\n",
        "\t\t iCloud = 10\n",
        "\t\t Reddit = 11\n",
        "\t\t MiCloud = 12")
        opcaoselecionada = int(input("\t\tOpção Selecionada: "))
            
            
            #Inicio de captura de daodos.
        if(opcaoselecionada == 1):
            opcaoselecionada = 1
            print("\t\tVocê selecionou: Instagram <=")

        elif(opcaoselecionada == 2):
            opcaoselecionada = 2
            print("\t\tVocê selecionou: Facebook <=")

        elif(opcaoselecionada == 3):
            opcaoselecionada = 3
            print("\t\tVocê selecionou: GitHub <=")

        elif(opcaoselecionada == 4):
            opcaoselecionada = 4
            print("\t\tVocê selecionou: Twitter <=")

        elif(opcaoselecionada == 5):
            opcaoselecionada = 5
            print("\t\tVocê selecionou Google <=")

        elif(opcaoselecionada == 6):
            opcaoselecionada = 6
            print("\t\tVocê selecionou: YouTube <=")

        elif(opcaoselecionada == 7 ):
            opcaoselecionada = 7
            print("\t\tVocê selecionou: LinkedIn <=")

        elif(opcaoselecionada == 8):
            opcaoselecionada = 8
            print("\t\tVocê selecionou: TikTok <=")

        elif(opcaoselecionada == 9):
            opcaoselecionada = 9
            print("\t\tVocê selecionou: SnapChat <=")

        elif(opcaoselecionada == 10):
            opcaoselecionada = 10
            print("\t\tVocê selecionou: iCloud <=")

        elif(opcaoselecionada == 11):
            opcaoselecionada = 11
            print("\t\tVocê selecionou: Reddit <=")

        elif(opcaoselecionada == 12):
            opcaoselecionada = 12
            print("\t\tVocê selecionou: MiCloud <=")

        else:
            os.system('color 4')
            print("\t\tO valor que você digitou está errado!\n"
            "\t\to programa será fechado em 4 segundos.\n")
            time.sleep(4)
            os.system('cls')
            exit(0)


        senhaAserBuscada = opcaoselecionada
        if senhaAserBuscada == 1:
            arquivoasersalvo = open("Arquivos\SenhasSalvas\SenhaIntagram.txt",'r')

        elif senhaAserBuscada == 2:
            arquivoasersalvo = open("Arquivos\SenhasSalvas\SenhaFacebook.txt",'r')

        elif senhaAserBuscada == 3:
            arquivoasersalvo = open("Arquivos\SenhasSalvas\SenhaGitHub.txt",'r')

        elif senhaAserBuscada == 4:
            arquivoasersalvo = open("Arquivos\SenhasSalvas\SenhaTwitter.txt",'r')

        elif senhaAserBuscada == 5:
            arquivoasersalvo = open("Arquivos\SenhasSalvas\SenhaGoogle.txt",'r')

        elif senhaAserBuscada == 6:
            arquivoasersalvo = open("Arquivos\SenhasSalvas\SenhaYoutube.txt",'r')

        elif senhaAserBuscada == 7:
            arquivoasersalvo = open("Arquivos\SenhasSalvas\SenhaLinkedIn.txt",'r')

        elif senhaAserBuscada == 8:
            arquivoasersalvo = open("Arquivos\SenhasSalvas\SenhaTikTok.txt",'r')

        elif senhaAserBuscada == 9:
            arquivoasersalvo = open("Arquivos\SenhasSalvas\SenhaSnapChat.txt",'r')

        elif senhaAserBuscada == 10:
            arquivoasersalvo = open("Arquivos\SenhasSalvas\SenhaiCloud.txt",'r')

        elif senhaAserBuscada == 11:
            arquivoasersalvo = open("Arquivos\SenhasSalvas\SenhaReddit.txt",'r')

        elif senhaAserBuscada == 12:
            arquivoasersalvo = open("Arquivos\SenhasSalvas\SenhaMiCloud.txt",'r')

        #retorno de dados.
        print("\t\tAs senhas salvas para a rede social escolhida são:")
        lista = arquivoasersalvo.readlines()
        listaa = lista

        listaa.sort()

        print('\t\t',listaa)
        #pergunta se deve buscar mais alguma lista.
consultarsenhassalvas()
input('')