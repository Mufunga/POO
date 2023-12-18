from tinydb import TinyDB
from models.players import Player

class Tournament:
    def __init__(self,name,place,start_date,end_date, description, player_number, rounds=[], players: list =[],current_round=0, round_number=4):
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

    
    def __str__(self) -> str:
        return f'{self.name} {self.place} {self.start_date} {self.end_date} {self.current_round} {self.round_number}'
    
    def __repr__(self) -> str:
        return str(self)
    
    def serialize(self):
        serialize_tournament ={
            "name":self.name,
            "place":self.place,
            "start_date":self.start_date,
            "end_date":self.end_date,
            "current_round":self.current_round,
            "round_number":self.round_number,
            "player_number":self.player_number,
            "description": self.description
        }
        return serialize_tournament
    

    



