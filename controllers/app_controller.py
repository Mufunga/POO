from models.players import Player
from views.view_app import View_app
from controllers.player_controller import Player_controller
from controllers.tournament_controller import Tournamentcontroller


class App_controller :
    def __init__(self):
       self.main_menu = View_app()
       self.player_controller = Player_controller()
       self.tournament = Tournamentcontroller()

    def start(self):
       exit_requested = False
       while not exit_requested :
         choice = self.main_menu.display_main_menu()
         if choice == "1":
             self.player_controller.player_manager()
             print("Enter your choice:")
         elif choice == "2":
             self.tournament.tournament_manager()
         elif choice == "3":
             exit_requested = True
             
       #while not exit_requested :
             

             
          



if __name__=="__main__":
   str_menu = App_controller()
   str_menu.start()

