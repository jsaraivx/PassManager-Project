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
                            ESTE PROGRAMA SERÁ MELHORADO CONFORME O MEU CONHECIMENTO AVANÇAR,
                            POR ENQUANTO ELES APENAS RETORNARÁ OS ARQUIVOS SEM ORDENAR. 

                            THIS PROGRAM WILL BE IMPROVED ACCORDING TO MY KNOWLEDGE ADVANCING,
                            WHILE THEY WILL ONLY RETURN THE FILES WITHOUT ORDERING.
"""



dados=open("Arquivos\SenhasSalvas\senhas.txt",'r')
linha = dados.readlines()

lista = linha
lista.sort()

print(lista)


