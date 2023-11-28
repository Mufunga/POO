from views.view_tournament import ViewTournament
from models.players import Player
from controllers.player_controller import Player_controller
from models.tournament import Tournament



class Tournamentcontroller:
    def __init__(self) -> None:
        self.view = ViewTournament()
        self.tournament = None
        
    def add_players_tournament(self):

        """Return saved  players in the data base"""
        players_l = Player_controller().show_players_list()
        players_saved = Player.all(type_player=False)
        valid_players_id = [str(p.get("db_id")) for p in players_saved]
        player_input_id = self.view.get_tournament_player_id(valid_players_id, self.tournament.player_number)
        players = []
        for p_id in player_input_id:
            players.append(Player.get(p_id))
            return players

    def create_tournament(self):
        tournament_infos = self.view.get_info_tournament()
        self.tournament = Tournament(**tournament_infos)
        return self.tournament
    
        self.add_players_tournament()
    

    
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
    player_number = 4
    valid_players_id = ["1","2","4","7"]

    tour.add_players_tournament()

