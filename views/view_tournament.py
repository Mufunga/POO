class ViewTournament:
    
    def get_info_tournament(self):
        """Return  tournament info dictionary """
        tournament_info = {}

        print ("Enter the following information".center(80,"*"))

        tournament_info["name"] = input("Enter Tournament name: \n")
        tournament_info["place"] = input( "Enter Place: \n ")
        tournament_info["start_date"] = input ("Enter Start date :\n")
        tournament_info ["end_date"] = input ("Enter the end date ")
        return tournament_info
    
    def players_selected(self):
         """Select the player input by the user"""
         players_selected = {}
         players_selected["id_1"] = input ("Enter the fist player:\n")
         players_selected ["id_2"] = input("Enter the second player:\n")
      
              
         
         
    
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

if __name__ == "__main__":
        view_t = ViewTournament()
        print(view_t.get_info_tournament())

