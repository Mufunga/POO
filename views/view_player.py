class View_payer:

    def get_info_player(self):
        player_info ={}

        print("Enter your informations".center(80,"*") )

        player_info["first_name"] = input("Enter your First_Name: \n")
        player_info["family_name"] = input("Family Name:\n")
        player_info["birthday"] = input("Birthday:\n ")
        player_info["chess_id"] = input("chess_id:\n")

        return player_info
    
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
                choice = input("\nEnter your choice : ")
                if choice == "1":
                    player_infos = self.get_info_player()
                    return player_infos
                    #print(player["first_name"])
                elif choice == "2":
                    print("Show players List by name order ")
            elif choice == "3":
                return "Merci pour votre visite"
            else:
                print("invalid choice\n")
            

                


if __name__=="__main__" :
    view_player = View_payer()
    print(view_player.desplay_player_menu())