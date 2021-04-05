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
""" 
                    EintUTURA FUNCIONAL DE GERAR UM ARQUIVO NA PASTA COM O RELATIONAL PATH
arquivo = open("Arquivos\SenhasSalvas\senhas.txt",'a')
arquivo.write("By: Joao saraivx")
arquivo.close()

"""
"""#Rede Social
print("Para inciarmos você deve digitar o nome da rede social que você quer armazenar a senha.")
redeSocial = input("\n" "Digite o nome da rede social. ")
print("")

#Login
print("Agora você deverá digitar o nome de usuario/email vinculado a conta.")
print("Como por exemplo: \n"
"@exemplodeuser ou")
print("exemplo@email.com.br")
print("")
User = input("\n" "Digite o seu nome de usúario. ")

#Senhas
print("Olá, para começarmos a salvar as senhas, você deverá digitar \n"
"sua senha ")
print("")

senhaAserGravada = input("\n" "Digite sua senha! ")

#Processamento para arquivo .txt
senhaSalvas = open("Arquivos\SenhasSalvas\senhas.txt",'a')
senhaSalvas.write(redeSocial)
senhaSalvas.write(" ")
senhaSalvas.write("==>")
senhaSalvas.write(" ")
senhaSalvas.write(User)
senhaSalvas.write(" ")
senhaSalvas.write("==")
senhaSalvas.write(" ")
senhaSalvas.write(senhaAserGravada)
senhaSalvas.write("\n")

                            VERSÃO DESATUALIZADA DE GUARDAR SENHA, SERÁ REFEITA DO ZERO.

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
    print("Você selecionou Instagram")
elif(opcaoselecionada == 2):
    print("Você selecionou Facebook")
elif(opcaoselecionada == 3):
    print("Você selecionou GitHub")
elif(opcaoselecionada == 4):
    print("Você selecionou Twitter")
elif(opcaoselecionada == 5):
    print("Você selecionou Google")
elif(opcaoselecionada == 6):
    print("Você selecionou YouTube")
elif(opcaoselecionada == 7 ):
    print("Você selecionou LinkedIn")
elif(opcaoselecionada == 8):
    print("Você selecionou TikTok")
elif(opcaoselecionada == 9):
    print("Você selecionou SnapChat")
elif(opcaoselecionada == 10):
    print("Você selecionou iCloud")
elif(opcaoselecionada == 11):
    print("Você selecionou Reddit")
elif(opcaoselecionada == 12):
    print("Você selecionou MiCloud")



