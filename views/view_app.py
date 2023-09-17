class View_app:
    """return the main menu for the application"""

    def display_main_menu (self):
        print("Welcome to the Chess game ".center(80,"="))
        while True:
            print("1. Player manger :")
            print("2. Tournement manger")
            print("3. Exit the game")
            choice = input("\n" "Enter your choice:")
            if choice in ["1","2","3"]:
                return choice
            else:
                print("\n""Invalid choice")

if __name__ == "__main__":
    menu = View_app()
    print(menu.display_main_menu())


            