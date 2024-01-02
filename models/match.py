class Match:
    def __init__(self,player1_db_id,player2_db_id, score_player_1=0, score_player_2=0):
        self.player1_db_id = player1_db_id,
        self.player2_db_id = player2_db_id,

        self.score_player_1 = score_player_1
        self.score_player_2 = score_player_2

    def serialize (self):
        match ={
            "player_1":self.player1_db_id,
            "player_2":self.player2_db_id,
            "score_player_1":self.score_player_1,
            "score_player_2":self.score_player_2
        }
        return match
