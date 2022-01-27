from views.start_menu import StartMenu
from views.tournament import TournamentMenu
from models.tournament import Tournament
from models.player import Player


class Controller:

    def __init__(self, start_menu: StartMenu, tournament_menu: TournamentMenu):
        self.start_menu = start_menu
        self.tournament_menu = tournament_menu
        self.tournament = None

    def create_tournament(self):
        tournament_list = self.tournament_menu.create_new_tournament()
        self.tournament = Tournament(tournament_list[0], tournament_list[1], tournament_list[2], tournament_list[3],
                                tournament_list[4])
        self.choice_tournament()

    def add_player(self):
        if self.tournament.count_number_of_player():
            player_list = self.tournament_menu.add_player()
            player = Player(player_list[0], player_list[1], player_list[2], player_list[3], player_list[4])
            self.tournament.add_players(player)
        else:
            self.tournament_menu.nombre_max_atteint()

    def choice_tournament(self):
        menu_tournament = self.tournament_menu.prompt_for_tournament_menu()
        if menu_tournament == 1:
            self.create_tournament()
        elif menu_tournament == 2:
            self.add_player()

    def choice_report(self):
        pass

    def run(self):
        running = True
        while running:
            main_menu = self.start_menu.prompt_for_choice()
            if main_menu == 1:
                self.choice_tournament()
            elif main_menu == 2:
                self.choice_report()
            running = self.start_menu.prompt_for_new_game()
