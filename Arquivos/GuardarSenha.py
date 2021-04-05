import time
import os
def programaparasalvar():
    # coding: utf-8
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
        #INTRODUÇÃO 
    print("\t \t Olá, primeiro selecione a sua rede social. \n"
    "\t \t Caso a sua rede social favorita não esteja aqui,\n"
    '\t \t você pode comentar a sua sujestão para que ela seja adicionada. \n\n')


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
    print("\t\tLISTA DE REDES SOCIAIS\n",
    "\t\tSUPORTADAS:\n",
    "\t\t Instagram = 1\n",
    "\t\t Facebook = 2\n",
    "\t\t GitHub = 3\n",
    "\t\t Twitter = 4\n",
    "\t\t Google = 5\n",
    "\t\t Youtube = 6\n",
    "\t\t LinkedIn = 7\n",
    "\t\t Tiktok = 8\n",
    "\t\t SnapChat = \n",
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
        

        #Decisão do arquivo a ser escrito.
    senhagerenciada = opcaoselecionada
    if senhagerenciada==1:
        arquivoasersalvo = open("Arquivos\SenhasSalvas\SenhaIntagram.txt",'a')

    elif senhagerenciada == 2:
        arquivoasersalvo = open("Arquivos\SenhasSalvas\SenhaFacebook.txt",'a')

    elif senhagerenciada == 3:
        arquivoasersalvo = open("Arquivos\SenhasSalvas\SenhaGitHub.txt",'a')

    elif senhagerenciada == 4:
        arquivoasersalvo = open("Arquivos\SenhasSalvas\SenhaTwitter.txt",'a')

    elif senhagerenciada == 5:
        arquivoasersalvo = open("Arquivos\SenhasSalvas\SenhaGoogle.txt",'a')

    elif senhagerenciada == 6:
        arquivoasersalvo = open("Arquivos\SenhasSalvas\SenhaYoutube.txt",'a')

    elif senhagerenciada == 7:
        arquivoasersalvo = open("Arquivos\SenhasSalvas\SenhaLinkedIn.txt",'a')

    elif senhagerenciada == 8:
        arquivoasersalvo = open("Arquivos\SenhasSalvas\SenhaTikTok.txt",'a')

    elif senhagerenciada == 9:
        arquivoasersalvo = open("Arquivos\SenhasSalvas\SenhaSnapChat.txt",'a')

    elif senhagerenciada == 10:
        arquivoasersalvo = open("Arquivos\SenhasSalvas\SenhaiCloud.txt",'a')

    elif senhagerenciada == 11:
        arquivoasersalvo = open("Arquivos\SenhasSalvas\SenhaReddit.txt",'a')

    elif senhagerenciada == 12:
        arquivoasersalvo = open("Arquivos\SenhasSalvas\SenhaMiCloud.txt",'a')

        #Processamento dos dados de login.

    print("\n\t\tAgora, preciso que você me informe o usuário/email a ser salvo: ")
    usuario = input("\t\t Usuário a ser salvo: ")

    print("\n\t\tAgora, por último preciso da senha a ser salva:")
    senha = input("\t\t Senha a ser salva: ")

    arquivoasersalvo.write(usuario)
    arquivoasersalvo.write(' ')
    arquivoasersalvo.write('==')
    arquivoasersalvo.write(' ')
    arquivoasersalvo.write(senha)

        #finalização do processamento

    print("\n\t\tO processamento terminou, os dados foram salvos.\n\t\t"
    "Agora para buscar as senhas salvas, é só abrir o programa\n\t\t"
    'ConsultaSenha.py ')
programaparasalvar();
def depoisdesalvardados():
    print("\n\t\tVocê deseja salvar outra senha?\n")
    escolher1 = int(input('\t\tDigite 1 para sim, 2 para sair do programa.\n'))
    if escolher1 == 1:
        programaparasalvar()
    elif escolher1 == 2: 
        exit(0)
    else:
        print("\t\tVocê digitou errado!\n")
depoisdesalvardados();

