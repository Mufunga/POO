class View_round:
    
    def get_round_infos(self):
        """return dictionary of round information put by the user"""

        round_infos = {}

        print("Enter the following informations accordind to the round".center(80, "*"))

        round_infos["round_name"] = input("Enter the name of round: \n")
        round_infos["start_date"] = input("Enter the satrt date and hour for this round: \n")
        round_infos["end_date"] = input ("Enter the end date and hour for this round: \n")
        return round_infos
