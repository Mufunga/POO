from views.view_tournament import ViewTournament
from models.players import Player
from controllers.player_controller import Player_controller
from models.tournament import Tournament
from models.match import Match
from models.rounds import Round
import datetime
import random



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
        
        for p_id in player_input_id:
            self.tournament.players.append(Player.get(p_id))

    def create_tournament(self):
        tournament_infos = self.view.get_info_tournament()
        self.tournament = Tournament(**tournament_infos)
        self.add_players_tournament()
        print(self.tournament.players)
        self.manage_rounds()

    def create_round(self,players: list, current_round):
        round_name = f"Round {current_round}"
        matches = []
        date = datetime.datetime.now()
        start_date = date.strftime("%Y-%m-%d %H:%M:%S")
        end_date = date.strftime("%Y-%m-%d %H:%M:%S")

        while len(players) > 0:
            player1_db_id = players.pop(0)
            player2_db_id = players.pop(0)
            match = Match(player1_db_id=player1_db_id,player2_db_id=player2_db_id)
            matches.append(match)

        round = Round(round_name = round_name, start_date=start_date, end_date=end_date, matches=matches)

        return round
    
    def manage_rounds(self):
        exit_requested = False

        while not exit_requested:
            choice = self.view.launch_rounds()
            if choice.lower()== "no":
                break
            
            players = self.tournament.players.copy()

            if self.tournament.current_round == 0:
                random.shuffle(players)
            else:
                players.sort(reverse=True, key=lambda player: player.score())

            self.tournament.current_round += 1
            round = self.create_round(players, self.tournament.current_round)
            self.tournament.rounds.append(round)
        
        self.tournament.save()
                
    
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
    tour.manage_rounds()

