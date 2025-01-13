from app.services.world_service import gerar_mundo
from app.services.city_service import criar_cidade
from app.services.race_service import criar_raca
from colorama import Fore, Style

def menu():
    while True:
        print(Fore.CYAN + "\n=== WorldCrafter - Criador de Mundos ===" + Style.RESET_ALL)
        print(Fore.YELLOW + "=" * 50 + Style.RESET_ALL)
        print(Fore.GREEN + "[1]" + Style.RESET_ALL + " Criar Mundo")
        print(Fore.GREEN + "[2]" + Style.RESET_ALL + " Criar Cidade")
        print(Fore.GREEN + "[3]" + Style.RESET_ALL + " Criar Raça")
        print(Fore.GREEN + "[4]" + Style.RESET_ALL + " Sair")
        print(Fore.YELLOW + "=" * 50 + Style.RESET_ALL)
        opcao = input(Fore.CYAN + "Escolha uma opção: " + Style.RESET_ALL)

        if opcao == "1":
            # Criar Mundo
            mundo = gerar_mundo()
            print(Fore.GREEN + "\n🌍 Mundo Gerado:" + Style.RESET_ALL)
            print(Fore.YELLOW + f"Nome: {mundo['nome']}" + Style.RESET_ALL)
            print(Fore.YELLOW + f"Cultura: {mundo['cultura']}" + Style.RESET_ALL)
            print(Fore.YELLOW + f"Clima: {mundo['clima']}" + Style.RESET_ALL)
            print(Fore.YELLOW + f"População: {mundo['populacao']}" + Style.RESET_ALL)

        elif opcao == "2":
            # Criar Cidade
            nome = input(Fore.CYAN + "Digite o nome da cidade: " + Style.RESET_ALL)
            populacao = input(Fore.CYAN + "Digite a população da cidade: " + Style.RESET_ALL)
            cidade = criar_cidade(nome, populacao)
            print(Fore.GREEN + f"\n🏙️ Cidade criada: {cidade['nome']} com {cidade['populacao']} habitantes." + Style.RESET_ALL)

        elif opcao == "3":
            # Criar Raça
            nome = input(Fore.CYAN + "Digite o nome da raça: " + Style.RESET_ALL)
            habilidade = input(Fore.CYAN + "Digite uma habilidade especial da raça: " + Style.RESET_ALL)
            raca = criar_raca(nome, habilidade)
            print(Fore.GREEN + f"\n🧝 Raça criada: {raca['nome']} com habilidade especial: {raca['habilidade']}" + Style.RESET_ALL)

        elif opcao == "4":
            print(Fore.GREEN + "Saindo... 👋" + Style.RESET_ALL)
            break

        else:
            print(Fore.RED + "⚠️ Opção inválida. Tente novamente." + Style.RESET_ALL)

if __name__ == '__main__':
    menu()
