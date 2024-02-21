from tinydb import TinyDB, Query
from models.players import Player

db = TinyDB("data/tournament_db.json")
tournament = Query()


class Tournament:
    def __init__(
        self,
        name,
        place,
        start_date,
        end_date,
        description,
        player_number,
        rounds=[],
        players: list = [],
        status="In progress",
        current_round=0,
        round_number=4,
    ):
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.rounds = rounds
        self.players = players
        self.current_round = current_round
        self.round_number = round_number
        self.description = description
        self.player_number = player_number
        self.status = status

    def __str__(self) -> str:
        return f"{self.name} {self.place} {self.start_date} {self.end_date} {self.current_round} {self.round_number}"

    def __repr__(self) -> str:
        return str(self)

    def serialize(self):
        players = []
        for player in self.players:
            players.append(player.db_id)

        rounds = []
        for round in self.rounds:
            rounds.append(round.serialize_round())

        serialize_tournament = {
            "name": self.name,
            "place": self.place,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "current_round": self.current_round,
            "round_number": self.round_number,
            "player_number": self.player_number,
            "description": self.description,
            "players": players,
            "rounds": rounds,
            "status": self.status,
        }
        return serialize_tournament

    def save(self):
        tournament_data = db.insert(self.serialize())
        print(len(tournament_data))
        return tournament_data

    @classmethod
    def all(cls, Type_t=False):
        """Return saved tournament in dict format"""
        all_data = db.all()
        for infos in all_data:
            infos["db_id"] = infos.doc_id
        if Type_t == False:
            return all_data
        else:
            infos_tournaments = []
            for infos_dic in all_data:
                infos_tournaments.append(Tournament(**infos_dic))
                return infos_tournaments

    @classmethod
    def get_tournament_inprogress(self):
        db.search(tournament.status == "In progress")
