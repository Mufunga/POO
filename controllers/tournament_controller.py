from views.view_tournament import ViewTournament

class Tournamentcontroller:
    def __init__(self) -> None:
        self.view = ViewTournament()
    
    def create_tournament(self):
        tournament_infos = self.view.get_info_tournament()
       
    
    def restart_tournament(self):
        pass

    def repport_tournament(self):
        pass

    def tournament_manager(self):
        exit_requested = False
        while not exit_requested:
            choice = self.view.display_tournament_menu()
            if choice == "1":
                self.create_tournament()
            elif choice == "2":
                self.restart_tournament()
            elif choice == "3":
                self.repport_tournament()
            elif choice == "4":
                exit_requested = True

if __name__ == "__main__":
    tour = Tournamentcontroller()
    print(tour.tournament_manager())

