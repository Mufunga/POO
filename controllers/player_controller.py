from models.players import Player
from views.view_player import View_payer
from datetime import date

class Player_controller:
    def __init__(self)-> None:
        self.view = View_payer()
        #self.player = Player()

    def player_manager(self):
        exit_resquested = False

        while not exit_resquested:
            choice = self.view.display_player_menu()
            if choice == "1":
                palyer_infos = self.view.get_info_player()
                player = Player(**palyer_infos)
                return player.save()
            elif choice == "2":
                players = Player.all(type_player=True)
                for player in players:
                    print(player)
              
            elif choice == "3":
                exit_resquested = True

    #def create_player(self):
        #pass
        

        

if __name__=="__main__":
    plc=Player_controller()
    print(plc.player_manager())
