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
import utils 

def consultarsenhassalvas():
    redes = {
        1: ("Instagram", utils.get_path("Instagram.txt")),
        2: ("Facebook", utils.get_path("Facebook.txt")),
        3: ("GitHub", utils.get_path("GitHub.txt")),
        4: ("Twitter", utils.get_path("Twitter.txt")),
        5: ("Google", utils.get_path("Google.txt")),
        6: ("YouTube", utils.get_path("YouTube.txt")),
        7: ("LinkedIn", utils.get_path("LinkedIn.txt")),
        8: ("TikTok", utils.get_path("TikTok.txt")),
        9: ("SnapChat", utils.get_path("SnapChat.txt")),
        10: ("iCloud", utils.get_path("iCloud.txt")),
        11: ("Reddit", utils.get_path("Reddit.txt")),
        12: ("MiCloud", utils.get_path("MiCloud.txt"))
    }

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\t\t=== CONSULTA DE SENHAS SALVAS ===\n")
        print("\t\tSelecione o número da rede social que deseja buscar:\n")

        for numero, (nome, _) in redes.items():
            print(f"\t\t {nome} = {numero}")
        print("\t\t 0 = Sair")

        try:
            opcao = int(input("\n\t\tOpção Selecionada: "))

            if opcao == 0:
                print("\n\t\tEncerrando o programa...")
                time.sleep(1.5)
                break

            if opcao not in redes:
                raise ValueError

            nome, caminho = redes[opcao]
            print(f"\n\t\tVocê selecionou: {nome} <=")

            try:
                with open(caminho, 'r', encoding='utf-8') as arquivo:
                    senhas = [linha.strip() for linha in arquivo.readlines() if linha.strip()]
                    senhas.sort()

                    if senhas:
                        print("\n\t\tAs senhas salvas são:")
                        for senha in senhas:
                            print(f"\t\t - {senha}")
                    else:
                        print("\n\t\tNenhuma senha encontrada para esta rede social.")
            except FileNotFoundError:
                print(f"\n\t\tArquivo '{caminho}' não encontrado.")
            
            input("\n\t\tPressione ENTER para continuar...")

        except ValueError:
            os.system('color 4' if os.name == 'nt' else 'clear')
            print("\n\t\tOpção inválida! Digite um número entre 1 e 12, ou 0 para sair.")
            time.sleep(2)

# Executa o programa
consultarsenhassalvas()
