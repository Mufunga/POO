class View_payer:
    def desplay_player_menu(self):
        while True:
            print("\n", "Welcome to the Chess game".center(80,"-"), "\n")
            print("choose the following choice : ")
            print("1.Tournemant manager")
            print("2.Player manager")
            print("3.Exit")

            choice = input("\nEnter your choice : ")
            if choice == "1":
                print("Tournement Manager : \n")
            elif choice == "2":
                print("1.Create player")
                print("2.Show players List by name order ")
                choice = input("\nEnter your choice for player : ")
            elif choice in ["1","2"]:
                    return choice
                
            print("invalid choice \n")


if __name__=="__main__" :
    view_player = View_payer()
    print(view_player.desplay_player_menu())