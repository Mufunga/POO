
class Round :
    def __init__(self,round_name, start_date, end_date,round_status="en cours", matches=[]):
        self.round_name = round_name
        self.start_date = start_date
        self.end_date = end_date
        self.matches = matches
        self.round_status = round_status
    
    def __str__(self) -> str:
        return f'{self.round_name}, {self.start_date}, {self.end_date}'
    
    def __repr__(self) -> str:
        return str(self)
    
    def serialize_round (self):
        serialize_round = {
            "round_name": self.round_name,
            "start_date": self.start_date,
            "end_date":self.end_date
        }
        return serialize_round
    
        

