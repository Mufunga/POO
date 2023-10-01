from tabulate import tabulate
from colorama import Fore,Back,Style

class View_payer:

    def get_info_player(self):
        player_info ={}

        print("Enter your informations".center(80,"*") )

        player_info["first_name"] = input("Enter your first_Name: \n")
        player_info["name"] = input("name:\n")
        player_info["birthday"] = input("birthday:\n ")
        player_info["chess_id"] = input("chess_id:\n")

        return player_info
    
    def display_player_menu(self):
        while True:
            print("\n", "Players manager".center(80,"-"), "\n")
            print("choose the following choice : ")
            print("1.create player")
            print("2.show players list")
            print("3.Return to the previous menu")

            choice = input("\nEnter your choice : ")
            if choice in ["1","2","3"]:
               return choice
            else:
                print("invalid choice\n")
    def display_players(self,players):
       print(Fore.BLUE + Style.BRIGHT+ tabulate(players,headers="keys",tablefmt="grid"))


                


if __name__=="__main__" :
    view_player = View_payer()
    print(view_player.get_info_player())