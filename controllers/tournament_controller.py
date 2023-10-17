from views.view_tournament import ViewTournament
from models.players import Player
from controllers.player_controller import Player_controller



class Tournamentcontroller:
    def __init__(self) -> None:
        self.view = ViewTournament()
        
    
    def players_tournament(self):
        """Return saved players"""
        self.players = Player_controller()
        players_saved = Player.all(type_player=False)
        self.players.show_players_list()
        for saved_player in players_saved:
            db_ids = saved_player.get("db_id")
            
            
    
    
    def create_tournament(self):
        tournament_infos = self.view.get_info_tournament()
        self.players_tournament()

        print ("Selecte two players for this tournament :")


       
    
    def restart_tournament(self):
        pass

    def repport_tournament(self):
        pass

    def tournament_manager(self):
        exit_requested = False
        while not exit_requested:
            choice = self.view.display_tournament_menu()
            if choice == "1":
                self.create_tournament()
            elif choice == "2":
                self.restart_tournament()
            elif choice == "3":
                self.repport_tournament()
            elif choice == "4":
                exit_requested = True

if __name__ == "__main__":
    tour = Tournamentcontroller()
    print(tour.players_tournament())

