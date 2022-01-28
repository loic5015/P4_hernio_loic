from views.start_menu import StartMenu
from views.tournament import TournamentMenu
from models.tournament import Tournament
from models.player import Player
from models.tour import Tour

NUMBER_OF_PLAYER = 8
NAME_OF_TOUR = "Round"


class Controller:

    def __init__(self, start_menu: StartMenu, tournament_menu: TournamentMenu):
        self.start_menu = start_menu
        self.tournament_menu = tournament_menu
        self.tournament = None
        self.tour = None

    def create_tournament(self):
        """instantiate a new tournament"""
        tournament_list = self.tournament_menu.create_new_tournament()
        self.tournament = Tournament(tournament_list[0], tournament_list[1], tournament_list[2], tournament_list[3],
                                tournament_list[4])
        self.choice_tournament()

    def add_player(self):
        """instantiate a new player"""
        if self.tournament is not None:
            if self.count_number_of_player():
                player_list = self.tournament_menu.add_player()
                player = Player(player_list[0], player_list[1], player_list[2], player_list[3], player_list[4])
                self.tournament.add_players(player)
            else:
                self.tournament_menu.nombre_max_atteint()
        else:
            self.tournament_menu.tournoi_has_been_create()
        self.choice_tournament()

    def choice_tournament(self):
        """choice the tournament menu"""
        menu_tournament = self.tournament_menu.prompt_for_tournament_menu()
        if menu_tournament == 0:
            self.create_tournament()
        elif menu_tournament == 1:
            self.add_player()
        elif menu_tournament == 2:
            self.create_round_one()
        elif menu_tournament == 4:
            self.display_tour()
        elif menu_tournament == 6:
            self.start_menu.prompt_for_choice()
        else:
            self.tournament_menu.prompt_for_tournament_menu()

    def count_number_of_player(self) -> bool:
        if len(self.tournament.players) >= NUMBER_OF_PLAYER:
            return False
        else:
            return True

    def display_tour(self) -> None:
        self.tournament_menu.display_tour(self.tournament)
        self.choice_tournament()


    def sort_by_ranking(self) -> list:
        """"sort by ranking"""
        ranking_classement = []
        list_player = self.tournament.players
        condition = True
        while condition:
            classement_max = 0
            player_max = None
            for player in list_player:
                if player.ranking >= classement_max:
                    player_max = player
                    classement_max = player_max.ranking
            ranking_classement.append(player_max)
            list_player.remove(player_max)
            if len(ranking_classement) >= NUMBER_OF_PLAYER:
                condition = False
        return ranking_classement


    def create_round_one(self):
        """generate the first round of match"""
        ranking_classement = self.sort_by_ranking()
        condition = True
        i = 0
        matchs = []
        while condition:
            match = ([ranking_classement[i], 0], [ranking_classement[i+4], 0])
            matchs.append(match)
            i = i + 1
            if i >= 4:
                condition = False
        self.tour = Tour(NAME_OF_TOUR + " 1")
        print(self.tour)
        self.tour.add_match(matchs)
        print([x for x in self.tour.tour])
        self.tournament.add_tours(self.tour)
        self.choice_tournament()

    def choice_report(self):
        pass

    def run(self):
        """launch the start menu"""
        running = True
        while running:
            main_menu = self.start_menu.prompt_for_choice()
            if main_menu == 0:
                self.choice_tournament()
            elif main_menu == 1:
                self.choice_report()
            elif main_menu == 2:
                running = False
            running = self.start_menu.prompt_for_new_game()
            print(self.tournament)
            print(self.tournament.players)
            print(self.tournament.tours)
