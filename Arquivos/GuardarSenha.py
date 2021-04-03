"""
                                Este projeto está sendo desenvolvido inteiramente
                                Por João Saraiva, e eu disponibilizei este projeto
                                Para o público, para que o conhecimento se espalhe 
                                sempre! 
"""
""" 
                    ESTRUTURA FUNCIONAL DE GERAR UM ARQUIVO NA PASTA COM O RELATIONAL PATH
arquivo = open("Arquivos\SenhasSalvas\senhas.txt",'a')
arquivo.write("By: Joao saraivx")
arquivo.close()

"""
#Rede Social
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
senhaSalvas.write(User)
senhaSalvas.write(" ")
senhaSalvas.write("=")
senhaSalvas.write(" ")
senhaSalvas.write(senhaAserGravada)
senhaSalvas.write(" ")
senhaSalvas.write("=")
senhaSalvas.write(" ")
senhaSalvas.write(redeSocial)
senhaSalvas.write("\n")

