
class Round :
    def __init__(self,round_name, start_date, end_date, game=[]):
        self.round_name = round_name
        self.start_date = start_date
        self.end_date = end_date
        self.game = game
    
    def __str__(self) -> str:
        return f'{self.round_name}, {self.start_date}, {self.end_date}'
    
    def __repr__(self) -> str:
        return str(self)
    
    def serialize (self):
        serialize_round = {
            "round_name": self.round_name,
            "start_date": self.start_date,
            "end_date":self.end_date
        }
        return serialize_round
    
        

