from colorama import Fore, Back,Style
class View_app:
    """return the main menu for the application"""

    def display_main_menu (self):
        print(Fore.MAGENTA + Style.BRIGHT + "Welcome to the Chess game ".center(80,"="))
        while True:
            print(Fore.MAGENTA + Style.BRIGHT +"1. Player manager :")
            print(Fore.MAGENTA + Style.BRIGHT +"2. Tournement manager")
            print(Fore.MAGENTA + Style.BRIGHT +"3. Exit the game")
            choice = input("\n" "Enter your choice:")
            if choice in ["1","2","3"]:
                return choice
            else:
                print("\n""Invalid choice")

if __name__ == "__main__":
    menu = View_app()
    print(menu.display_main_menu())


            