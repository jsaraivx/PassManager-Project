import time
import os
import utils

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
    "\t\t SnapChat = 9\n",
    "\t\t iCloud = 10\n",
    "\t\t Reddit = 11\n",
    "\t\t MiCloud = 12")
    opcaoselecionada = int(input("\t\tOpção Selecionada: "))
        
        
        #Inicio de captura de daodos.
    match opcaoselecionada:
        case 1:
            opcaoselecionada = 1
            print("\t\tVocê selecionou: Instagram <=")
        case 2:
            opcaoselecionada = 2
            print("\t\tVocê selecionou: Facebook <=")
        case 3:
            opcaoselecionada = 3
            print("\t\tVocê selecionou: GitHub <=")
        case 4:
            opcaoselecionada = 4
            print("\t\tVocê selecionou: Twitter <=")
        case 5:
            opcaoselecionada = 5
            print("\t\tVocê selecionou Google <=")
        case 6:
            opcaoselecionada = 6
            print("\t\tVocê selecionou: YouTube <=")
        case 7:
            opcaoselecionada = 7
            print("\t\tVocê selecionou: LinkedIn <=")
        case 8:
            opcaoselecionada = 8
            print("\t\tVocê selecionou: TikTok <=")
        case 9:
            opcaoselecionada = 9
            print("\t\tVocê selecionou: SnapChat <=")
        case 10:
            opcaoselecionada = 10
            print("\t\tVocê selecionou: iCloud <=")
        case 11:
            opcaoselecionada = 11
            print("\t\tVocê selecionou: Reddit <=")
        case 12:
            opcaoselecionada = 12
            print("\t\tVocê selecionou: MiCloud <=")
        case _:
            os.system('color 4')
            print("\t\tO valor que você digitou está errado!\n"
            "\t\to programa será fechado em 4 segundos.\n")
            time.sleep(4)
            os.system('cls')
            exit(0)
        

        #Decisão do arquivo a ser escrito.
    senhagerenciada = opcaoselecionada

    if senhagerenciada==1:
        arquivoasersalvo = open(utils.get_path("Instagram.txt"),'a')

    elif senhagerenciada == 2:
        arquivoasersalvo = open(utils.get_path("Facebook.txt"),'a')

    elif senhagerenciada == 3:
        arquivoasersalvo = open(utils.get_path("GitHub.txt"),'a')

    elif senhagerenciada == 4:
        arquivoasersalvo = open(utils.get_path("Twitter.txt"),'a')

    elif senhagerenciada == 5:
        arquivoasersalvo = open(utils.get_path("Google.txt"),'a')

    elif senhagerenciada == 6:
        arquivoasersalvo = open(utils.get_path("YouTube.txt"),'a')

    elif senhagerenciada == 7:
        arquivoasersalvo = open(utils.get_path("LinkedIn.txt"),'a')

    elif senhagerenciada == 8:
        arquivoasersalvo = open(utils.get_path("TikTok.txt"),'a')

    elif senhagerenciada == 9:
        arquivoasersalvo = open(utils.get_path("SnapChat.txt"),'a')

    elif senhagerenciada == 10:
        arquivoasersalvo = open(utils.get_path("iCloud.txt"),'a')

    elif senhagerenciada == 11:
        arquivoasersalvo = open(utils.get_path("Reddit.txt"),'a')

    elif senhagerenciada == 12:
        arquivoasersalvo = open(utils.get_path("MiCloud.txt"),'a')

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
    arquivoasersalvo.write('\n')

        #finalização do processamento

    print("\n\t\tO processamento terminou, os dados foram salvos.\n\t\t"
    "Agora para buscar as senhas salvas, é só abrir o programa\n\t\t"
    'ConsultaSenha.py ')


def depoisdesalvardados():
    print("\n\t\tVocê deseja salvar outra senha?\n")
    escolher1 = int(input('\t\tDigite 1 para sim, 2 para sair do programa.\n'))
    if escolher1 == 1:
        programaparasalvar()
    elif escolher1 == 2: 
        exit(0)
    else:
        print("\t\tVocê digitou errado!\n")
