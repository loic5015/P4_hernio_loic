import tinydb.table
from tinydb import TinyDB, where
from views.start_menu import StartMenu
from views.tournament import TournamentMenu
from views.report import Report
from models.tournament import Tournament
from models.player import Player
from models.tour import Tour
from models.association import Association

NUMBER_OF_PLAYER = 8
NAME_OF_TOUR = "Round"


class Controller:

    def __init__(self, start_menu: StartMenu, tournament_menu: TournamentMenu, db: TinyDB, report: Report):
        self.start_menu = start_menu
        self.tournament_menu = tournament_menu
        self.db = db
        self.tournament = None
        self.tour = None
        self.db_matchs = []
        self.report = report

    def create_tournament(self):
        """instantiate a new tournament"""
        tournament_dict = self.tournament_menu.create_new_tournament()
        self.tournament = Tournament(tournament_dict)
        db_tournament = self.db.table('tournament')
        verify_tournament = db_tournament.search((where('name') == self.tournament.name) &
                                         (where('location') == self.tournament.location) &
                                         (where('date') == self.tournament.date))
        if not verify_tournament:
            db_tournament.insert(self.tournament.__repr__())
        self.tour = None
        self.db_matchs = []
        self.choice_tournament()

    def add_player(self):
        """instantiate a new player"""
        if self.tournament is not None:
            if self.count_number_of_player():
                player_dict = self.tournament_menu.add_player()
                player = Player(player_dict)
                db_player = self.db.table('player')
                verify_player = db_player.search((where('name') == player.name) & (where('surname') == player.surname))
                if verify_player:
                    db_player.update({'ranking': player.ranking}, (where('name') == player.name) &
                                     (where('surname') == player.surname))
                else:
                    db_player.insert(player_dict)
                self.tournament.add_players(player)
                db_tournament = self.db.table('tournament')
                verify_tournament = db_tournament.search((where('name') == self.tournament.name) &
                                                         (where('location') == self.tournament.location) &
                                                         (where('date') == self.tournament.date.isoformat()))
                if verify_tournament:
                    db_tournament.update({'players': [player.__repr__() for player in self.tournament.players]},
                                         (where('name') == self.tournament.name) &
                                         (where('location') == self.tournament.location) &
                                         (where('date') == self.tournament.date.isoformat()))
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
        elif menu_tournament == 5:
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
        if not self.count_number_of_player():
            list_association = self.test_tour_isNone()
            ranking_classement = self.sort_by_ranking(list_association)
            condition = True
            i = 0
            matchs = []
            list_match = []
            tour_dict = {}
            number_of_tour = 0
            while condition:
                if len(self.tournament.tours) == 0:
                    match = ([ranking_classement[i]], [ranking_classement[i+4]])
                    dict_match = ([ranking_classement[i].__repr__()], [ranking_classement[i+4].__repr__()])
                    i = i + 1
                    if i >= self.tournament.numbers_of_turn:
                        condition = False
                else:
                    match = ([ranking_classement[i]], [ranking_classement[i+1]])
                    dict_match = ([ranking_classement[i].__repr__()], [ranking_classement[i+1].__repr__()])
                    i = i + 2
                    number_of_tour = len(self.tournament.tours)
                    if i >= NUMBER_OF_PLAYER - 1:
                        condition = False
                matchs.append(match)
                list_match.append(dict_match)
            tour_dict['name'] =  NAME_OF_TOUR + " " + str(number_of_tour)
            self.tour = Tour(tour_dict)
            print(self.tour)
            self.tour.add_match(matchs)
            self.db_matchs.append(list_match)
            db_tournament = self.db.table('tournament')
            verify_tournament = db_tournament.search((where('name') == self.tournament.name) &
                                                     (where('location') == self.tournament.location) &
                                                     (where('date') == self.tournament.date.isoformat()))
            if verify_tournament:
                db_tournament.update({'tours': self.db_matchs},
                                     (where('name') == self.tournament.name) &
                                     (where('location') == self.tournament.location) &
                                     (where('date') == self.tournament.date.isoformat()))
            self.tournament.add_tours(self.tour)
        else:
            self.tournament_menu.number_player_not_reach()
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

    def modify_ranking_player(self):
        """modify the ranking of a player"""
        player = self.start_menu.find_player()
        db_player = self.db.table('player')
        verify_player = db_player.search((where('name') == player[0]) & (where('surname') == player[1]) &
                                         (where('day_of_birth') == player[2]))
        if verify_player:
            db_player.update({'ranking': player[3]}, (where('name') == player[0]) &
                             (where('surname') == player[1]) & (where('day_of_birth') == player[2]))
        else:
            self.start_menu.unknow_player()
        self.start_menu.prompt_for_choice()

    def choice_report(self):
        """choice menu report"""
        menu_report = self.report.prompt_for_choice()
        if menu_report == 0:
            self.sort_player_by_alphabetical_name()
        elif menu_report == 1:
            self.sort_player_by_ranking()
        elif menu_report == 2:
            self.create_round()
        elif menu_report == 3:
            self.display_tour()
        elif menu_report == 4:
            self.sort_tournament_by_alphabetical_name()
        elif menu_report == 5:
            self.sort_tournament_by_alphabetical_name()
        else:
            self.report.prompt_for_choice()

    def extract_list(self, table: str) -> list:
        """extract data from table et instantiate object tournament or player"""
        db_table = self.db.table(table)
        list = db_table.all()
        list_object = []
        for dic in list:
            if table == "tournament":
                tournament = Tournament(dic)
                list_object.append(tournament)
            elif table == "player":
                player = Player(dic)
                list_object.append(player)
        return list_object

    def sort_player_by_ranking(self):
        """sort player by ranking"""
        players = self.extract_list("player")
        list_sorted = self.sort_players_ranking(players)
        self.report.display_list(list_sorted)
        self.report.prompt_for_choice()

    def sort_player_by_alphabetical_name(self):
        """sort player by alphabetical name"""
        players = self.extract_list("player")
        list_sorted = self.sort_players_alphabetical(players)
        self.report.display_list(list_sorted)
        self.report.prompt_for_choice()

    def sort_tournament_by_alphabetical_name(self):
        """sort tournament by alphabetical name"""
        tournament = self.extract_list("tournament")
        list_sorted = self.sort_players_alphabetical(tournament)
        self.report.display_list(list_sorted)
        self.report.prompt_for_choice()

    def sort_players_alphabetical(self, players: list) -> list:
        players_sort_by_alphabetical = []
        while len(players) > 0:
            player_name_max = ''
            player_max = None
            for player in players:
                if player.name >= player_name_max:
                    player_max = player
                    player_name_max = player.name
            players_sort_by_alphabetical.append(player_max)
            players.remove(player_max)
        return players_sort_by_alphabetical

    def sort_players_ranking(self, players: list) -> list:
        players_sort_by_ranking = []
        while len(players) > 0:
            player_max = None
            player_ranking_max = 0
            for player in players:
                if player.ranking >= player_ranking_max:
                    player_max = player
                    player_ranking_max = player.ranking
            players_sort_by_ranking.append(player_max)
            players.remove(player_max)
        return players_sort_by_ranking


    def run(self):
        """launch the start menu"""
        running = True
        while running:
            db_tournament = self.db.table('tournament')
            db_association = self.db.table('association')
            main_menu = self.start_menu.prompt_for_choice()
            if main_menu == 0:
                self.choice_tournament()
            elif main_menu == 1:
                self.choice_report()
            elif main_menu == 2:
                self.modify_ranking_player()
            elif main_menu == 3:
                running = False
            else:
                self.start_menu.prompt_for_choice()
            running = self.start_menu.prompt_for_new_game()
        db_player = self.db.table('player')
        db_tournament = self.db.table('tournament')
        print(db_tournament.all())
        print(db_player.all())
        print(str(self.tournament))

