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
        player_input_id = self.view.get_tournament_player_id(
            valid_players_id, self.tournament.player_number
        )

        for p_id in player_input_id:
            self.tournament.players.append(Player.get(p_id))

    def create_tournament(self):
        tournament_infos = self.view.get_info_tournament()
        self.tournament = Tournament(**tournament_infos)
        self.add_players_tournament()
        print(self.tournament.players)
        self.manage_rounds()

    def create_round(self, players: list, current_round):
        round_name = f"Round {current_round}"
        matches = []
        date = datetime.datetime.now()
        start_date = date.strftime("%Y-%m-%d %H:%M:%S")
        end_date = date.strftime("%Y-%m-%d %H:%M:%S")

        while len(players) > 0:
            player1 = players.pop(0)
            player2 = players.pop(0)
            match = Match(player1=player1, player2=player2)
            matches.append(match)

        round = Round(
            round_name=round_name,
            start_date=start_date,
            end_date=end_date,
            matches=matches,
        )

        return round

    def manage_rounds(self):
        exit_requested = False

        while not exit_requested:
            choice = self.view.launch_rounds()
            if choice.lower() == "no":
                break

            players = self.tournament.players.copy()

            if self.tournament.current_round == 0:
                random.shuffle(players)
            else:
                players.sort(reverse=True, key=lambda player: player.score)

            self.tournament.current_round += 1
            round = self.create_round(players, self.tournament.current_round)
            self.tournament.rounds.append(round)

            desplay_matchs = self.view.desplay_match(round)
            result = self.view.match_note_request()
            if result.lower() == "no":
                break

            self.get_score_c(round)
            if self.tournament.current_round >= self.tournament.round_number:
                self.tournament.status = "Done"
            exit_requested = True

        self.tournament.save()
        self.restart_tournament()

    def get_score_c(self, round):

        for match in round.matches:
            result_score = self.view.get_score(match)

            if result_score == 1:
                match.score_player_1 = 1
            elif result_score == 2:
                match.score_player_2 = 1
            else:
                match.score_player_1 = 0.5
                match.score_player_2 = 0.5

    # self.tournament.save()

    def match_score(self):
        pass

    def restart_tournament(self):

        tournaments = Tournament.get_tournament_inprogress()
        return tournaments

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
    tour.desplay_match()
