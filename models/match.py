class Match:
    def __init__(self,player_1,player_2, score_player_1=0, score_player_2=0):
        self.player_1 = player_1,
        self.player_2 = player_2,

        self.score_player_1 = score_player_1
        self.score_player_2 = score_player_2

    def serialize (self):
        match ={
            "player_1":self.player_1,
            "player_2":self.player_2,
            "score_player_1":self.score_player_1,
            "score_player_2":self.score_player_2
        }
        return match
