from models.players import Player
from views.view_player import View_payer
from datetime import date


class Player_controller:
    def __init__(self)-> None:
        self.view = View_payer()
        #self.player = Player()

    def create_player(self):
        palyer_infos = self.view.get_info_player()
        player = Player(**palyer_infos)
        return player.save()
    
    def show_players_list(self):
        players = Player.all()
        self.view.display_players(players)

    def player_manager(self):
        exit_resquested = False

        while not exit_resquested:
            choice = self.view.display_player_menu()
            if choice == "1":
                self.create_player()
                
            elif choice == "2":
                self.show_players_list()

            elif choice == "3":
                exit_resquested = True

        

        

if __name__=="__main__":
    plc=Player_controller()
    print(plc.show_players_list())
