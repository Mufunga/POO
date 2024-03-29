class ViewTournament:
    
    def get_info_tournament(self):
        """Return  tournament info dictionary """
        tournament_info = {}

        print ("Enter the following information".center(80,"*"))

        tournament_info["name"] = input("Enter Tournament name: \n")
        tournament_info["place"] = input( "Enter Place: \n ")
        tournament_info["start_date"] = input ("Enter Start date :\n")
        tournament_info ["end_date"] = input ("Enter the end date ")
        tournament_info ["player_number"] = input ("Enter the number of players ")
        tournament_info ["round_number"] = int(input ("For how many round : \n "))
        tournament_info ["description"] = input ("Enter descriptions ")
        
        return tournament_info
    
    def display_tournament_menu (self):

        while True:
            print("\n","tournament manager".center(80,"-"),"\n")
            print ("choose the following choice : ")
            print ("1. create tournament")
            print ("2. restart tournament")
            print ("3. tournament report")
            print ("4. exit")

            choice = input ("\n Enter your choice : ")

            if choice in ["1","2","3","4"]:
                return choice
            else:
                print("Invalid choice \n")

    def get_tournament_player_id(self, valid_players_id, player_number):
    
            while True:
                 
                player_id_str = input('please indicate players id for the tournament Separate by spaces \n:' )
                players_id = player_id_str.split()

                bad_id = []

                for db_id in players_id:
                     if db_id not in valid_players_id:
                         bad_id.append(db_id)

                if len(bad_id) > 0:
                     print (f"\n the following id(s) are not correct : {bad_id}")

                     continue
                     
                return players_id
            
    def launch_rounds(self):
        """return user's choice according to rounds"""

        valid_choice = ["yes", "no"]
        while True:
            choice = input ("\n Do you want to launch a round (yes/no)?")

            if choice in valid_choice:
                 return choice
            
            print("invalid choice")

    def match_note_request(self):
         valid_choice = ["yes", "no"]
         while True:
              choice = input ("\n Do you want to enter the match note (yes/no)? ")

              if choice in valid_choice:
                   return choice
              
              print("Invlid choice")


    def desplay_match(self, round):
        for match in round.matches:
            print (f"{match.player1.name} VS {match.player2.name}")
        print("****************************************************************************")
            
         

    def get_score(self, match):
         valid_score = ["1","2","3"]
         while True:
            
            print(f"What is the score betwin {match.player1.name} VS {match.player2.name}")
            print("************************************************************************")
            input_score = input(f"Type 1 if the winner is {match.player1.name} or Type 2 if {match.player2.name} is the winner and 3 for draw:")
            print(f' {type(input_score)}')

            if input_score in valid_score:
                return input_score
            else:
                print("score note not correct")
    
    def resume_round(self):
        """Return user's choice according to resume tournament"""

        valid_choice = ["yes", "no"]
        while True:
            choice = input ("\n Do you want to resume Tournaments (yes/no)?")

            if choice in valid_choice:
                 return choice
            
            print("invalid choice")
         



         


if __name__ == "__main__":
        
        view_t = ViewTournament()
        valid_players_id = ["1","3","6","5"]
        print(view_t.get_tournament_player_id(valid_players_id))

