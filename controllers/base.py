from models.players import Player
from views.view_player import View_payer

class Player_controller:
    def __init__(self)-> None:
        self.view = View_payer()
        self.player = Player()

    def palyer_manager(self):
        exit_resquested = False

        while not exit_resquested:
            choice = self.view.desplay_player_menu()
            if choice == "1":
                print("Tournement manager")
            elif choice == "2":
                pass
            elif choice == "3":
                exit_resquested = True
        

if __name__=="__main__":
    plc=Player_controller()
    print(plc.palyer_manager())
