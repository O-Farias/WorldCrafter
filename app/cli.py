from app.services.world_service import criar_mundo
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
            mundo = criar_mundo()
            print(Fore.GREEN + "\n🌍 Mundo Gerado:" + Style.RESET_ALL)
            print(Fore.YELLOW + f"Nome: {mundo['nome']}" + Style.RESET_ALL)
            print(Fore.YELLOW + f"Cultura: {mundo['cultura']}" + Style.RESET_ALL)
            print(Fore.YELLOW + f"Clima: {mundo['clima']}" + Style.RESET_ALL)
            print(Fore.YELLOW + f"População: {mundo['populacao']}" + Style.RESET_ALL)

        elif opcao == "2":
            # Criar Cidade
            cidade = criar_cidade()
            print(Fore.GREEN + f"\n🏙️ Cidade Criada:" + Style.RESET_ALL)
            print(Fore.YELLOW + f"Nome: {cidade['nome']}" + Style.RESET_ALL)
            print(Fore.YELLOW + f"População: {cidade['populacao']}" + Style.RESET_ALL)
            print(Fore.YELLOW + f"Descrição: {cidade['descricao']}" + Style.RESET_ALL)

        elif opcao == "3":
            # Criar Raça
            raca = criar_raca()
            print(Fore.GREEN + f"\n🧝 Raça Criada:" + Style.RESET_ALL)
            print(Fore.YELLOW + f"Nome: {raca['nome']}" + Style.RESET_ALL)
            print(Fore.YELLOW + f"Habilidade Especial: {raca['habilidade']}" + Style.RESET_ALL)
            print(Fore.YELLOW + f"Característica: {raca['caracteristica']}" + Style.RESET_ALL)

        elif opcao == "4":
            print(Fore.GREEN + "Saindo... 👋" + Style.RESET_ALL)
            break

        else:
            print(Fore.RED + "⚠️ Opção inválida. Tente novamente." + Style.RESET_ALL)

if __name__ == '__main__':
    menu()
