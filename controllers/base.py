from views.start_menu import StartMenu
from views.tournament import TournamentMenu
from models.tournament import Tournament
from models.player import Player
from models.tour import Tour
from models.association import Association

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
        self.tour = None
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
            self.create_round()
        elif menu_tournament == 3:
            self.display_tour()
        elif menu_tournament == 4:
            self.enter_result()
        elif menu_tournament == 6:
            self.start_menu.prompt_for_choice()
        else:
            self.tournament_menu.prompt_for_tournament_menu()

    def count_number_of_player(self) -> bool:
        """Verify the number of players"""
        if len(self.tournament.players) >= NUMBER_OF_PLAYER:
            return False
        else:
            return True

    def display_tour(self) -> None:
        """display tour"""
        self.tournament_menu.display_tour(self.tournament)
        self.choice_tournament()

    def sort_by_ranking(self, list_association: list) -> list:
        """"sort a list by ranking or score"""
        ranking_classement = []
        condition = True
        while condition:
            classement_max = 0.0
            association_max = None
            association_max_ranking = 0.0
            for association in list_association:
                if association.get_result() >= classement_max:
                    if association.get_result() == classement_max:
                        if association.get_player().ranking >= association_max_ranking:
                            association_max = association
                            association_max_ranking = association_max.player.ranking
                    else:
                        association_max = association
                        classement_max = association.get_result()
            ranking_classement.append(association_max)
            list_association.remove(association_max)
            print(ranking_classement)
            if len(ranking_classement) >= NUMBER_OF_PLAYER:
                condition = False
        return ranking_classement

    def test_tour_isNone(self) -> list:
        """"test if a tour is instantiate"""
        tour = self.tour
        list_association = []
        if tour is None:
            for player in self.tournament.players:
                association = Association(player)
                list_association.append(association)
        else:
            for round in tour.tour[-1]:
                for association in round:
                    list_association.append(association[0])
                    print(list_association)
        return list_association

    def create_round(self):
        """generate the round of the match"""
        list_association = self.test_tour_isNone()
        ranking_classement = self.sort_by_ranking(list_association)
        condition = True
        i = 0
        matchs = []
        number_of_tour = 0
        while condition:
            if len(self.tournament.tours) == 0:
                match = ([ranking_classement[i]], [ranking_classement[i+4]])
                i = i + 1
                if i >= self.tournament.numbers_of_turn:
                    condition = False
            else:
                match = ([ranking_classement[i]], [ranking_classement[i+1]])
                i = i + 2
                number_of_tour = len(self.tournament.tours)
                if i >= NUMBER_OF_PLAYER - 1:
                    condition = False
            matchs.append(match)

        self.tour = Tour(NAME_OF_TOUR + " " + str(number_of_tour))
        print(self.tour)
        self.tour.add_match(matchs)
        print([x for x in self.tour.tour])
        self.tournament.add_tours(self.tour)
        self.choice_tournament()

    def enter_result(self):
        """update the score in tour instance"""
        if self.tour is None:
            self.tournament_menu.tour_has_been_create()
        else:
            list_association = self.test_tour_isNone()
            for association in list_association:
                association.post_result(self.tournament_menu.enter_result(association) + association.get_result())
            self.tour.create_end_time()
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
