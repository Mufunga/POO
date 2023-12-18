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

    def create_round(self,players: list, current_round):
        name = f"Round {current_round}"
        matches = []
        date = datetime.now
        start_date = date.strftime("%Y-%m-%d %H:%M:%S")

        while len(players) > 0:
            player_1 = players.pop(0)
            player_2 = players.pop(0)
            match = Match(player_1=player_1,player_2=player_2)
            matches.append(match)

        round = Round(name = name, start_date=start_date, matches=matches)

        return round
    
    def manage_rounds(self, tournament: Tournament):
        exit_requested = False
        while not exit_requested:
            choice = self.view.launch_rounds()
            if choice.lower()== "yes":
                players = tournament.players.copy()
            if tournament.current_round == 0:
                random.shuffle(players)
            else:
                players.sort(reverse=True, key=lambda player: player.score)

            tournament.current_round += 1
            round = self.create_round(players, tournament.current_round)
            tournament.rounds.append(round)
                
            



    

    
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
    tour = Tournamentcontroller().create_tournament
    print (tour)
    #round1 =Tournamentcontroller.manage_rounds(tour)
    #print(round1)

