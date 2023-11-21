from views.view_tournament import ViewTournament
from models.players import Player
from controllers.player_controller import Player_controller



class Tournamentcontroller:
    def __init__(self) -> None:
        self.view = ViewTournament()
        
    
    def add_players_tournament(self):
        """Return saved  players in the data base"""
        players = Player_controller().show_players_list()
        players_saved = Player.all(type_player=False)
        valid_players_id = [p.get("db_id") for p in players_saved]
        player_input_id = ViewTournament.get_tournament_player_id(self)

        if player_input_id == valid_players_id:
            return player_input_id
        else:
            print(" saisie incorrect " + player_input_id)
        



        

        
        
            
            
    
    
    def create_tournament(self):
        tournament_infos = self.view.get_info_tournament()
        self.add_players_tournament()

        print ("Selecte 4 players for this tournament :")


       
    
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
    print(tour.add_players_tournament())

