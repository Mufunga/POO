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
        tournament_info ["description"] = input ("Enter descruptions ")
        
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
            
    def launch_rounds():
        """return user's choice according to rounds"""
       
        choice = input ("\n Do you want to launch a round (yes/no)?")
         


if __name__ == "__main__":
        
        view_t = ViewTournament()
        valid_players_id = ["1","3","6","5"]
        print(view_t.get_tournament_player_id(valid_players_id))

