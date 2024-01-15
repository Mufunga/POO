class Match:
    def __init__(self,player1,player2, score_player_1=0, score_player_2=0):
        self.player1 = player1,
        self.player2 = player2,

        self.score_player_1 = score_player_1
        self.score_player_2 = score_player_2

    def __str__(self) -> str:
        return f"{self.player1.name} VS {self.player2.name}"

    def serialize (self):
        match ={
            "player_1":self.player1.db_id,
            "player_2":self.player2.db_id,
            "score_player_1":self.score_player_1,
            "score_player_2":self.score_player_2
        }
        return match
