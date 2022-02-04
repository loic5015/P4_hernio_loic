import datetime
import pprint
from tinydb import TinyDB, where
from views.tournament import TournamentMenu
from models.tournament import Tournament
from models.player import Player
from models.association import Association
from models.tour import Tour
from .report_controller import ReportController


NUMBER_OF_PLAYER = 8
NAME_OF_TOUR = "Round"


class TournamentController:

    def __init__(self, main):
        self.tournament_menu = TournamentMenu()
        self.db = TinyDB('db.json')
        self.tournament = None
        self.tour = None
        self.main = main
        self.report = ReportController(self.main)

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
            self.resume_tournament()
        elif menu_tournament == 6:
            self.main.run()
        else:
            self.choice_tournament()

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
        list_association = []
        if self.tour is None:
            for player in self.tournament.players:
                association = Association({'player': player})
                list_association.append(association)
        else:
            for round in self.tour.tour[-1]:
                for association in round:
                    print(association)
                    list_association.append(association[0])
        return list_association

    def create_round(self):
        """generate the round of the match"""
        if not self.count_number_of_player():
            list_association = self.test_tour_isNone()
            ranking_classement = self.sort_by_ranking(list_association)
            test_number = True
            i = 0
            matchs = []
            db_matchs = []
            list_match = []
            tour_dict = {}
            number_of_tour = 0
            while test_number:
                if len(self.tournament.tours) == 0:
                    match = ([ranking_classement[i]], [ranking_classement[i+4]])
                    dict_match = ([ranking_classement[i].return_dict()], [ranking_classement[i+4].return_dict()])
                    i = i + 1
                    if i >= self.tournament.numbers_of_turn:
                        test_number = False
                else:
                    match = ([ranking_classement[i]], [ranking_classement[i+1]])
                    dict_match = ([ranking_classement[i].return_dict()], [ranking_classement[i+1].return_dict()])
                    i = i + 2
                    number_of_tour = len(self.tournament.tours)
                    if i >= NUMBER_OF_PLAYER - 1:
                        test_number = False
                matchs.append(match)
                list_match.append(dict_match)
            tour_dict['name'] = NAME_OF_TOUR + " " + str(number_of_tour)
            self.tour = Tour(tour_dict)
            tour_dict = self.tour.__repr__()
            self.tour.add_match(matchs)
            db_matchs.append(list_match)
            tour_dict['tour'] = db_matchs
            self.tournament.add_tours(self.tour)
            db_tournament = self.db.table('tournament')
            verify_tournament = db_tournament.search((where('name') == self.tournament.name) &
                                                     (where('location') == self.tournament.location) &
                                                     (where('date') == self.tournament.date.isoformat()))
            if verify_tournament:
                verify_tournament[0]['tours'].append(tour_dict)
                db_tournament.update({'tours': verify_tournament[0]['tours']},
                                     (where('name') == self.tournament.name) &
                                     (where('location') == self.tournament.location) &
                                     (where('date') == self.tournament.date.isoformat()))
        else:
            self.tournament_menu.number_player_not_reach()
        self.choice_tournament()

    def enter_result(self):
        """update the score in tour instance"""
        tour_list = []
        if self.tour is None:
            self.tournament_menu.tour_has_been_create()
        else:
            list_association = self.test_tour_isNone()

            for association in list_association:
                association.post_result(self.tournament_menu.enter_result(association) + association.get_result())
            self.tour.create_end_time()
            round_list = []
            for round in self.tour.tour[-1]:
                list_association = []
                for association in round:
                    list_association.append([association[0].return_dict()])
                round_list.append(list_association)
            tour_list.append(round_list)
            tour_dict = self.tour.__repr__()
            tour_dict['tour'] = tour_list
            db_tournament = self.db.table('tournament')
            verify_tournament = db_tournament.search((where('name') == self.tournament.name) &
                                                     (where('location') == self.tournament.location) &
                                                     (where('date') == self.tournament.date.isoformat()))
            if verify_tournament:
                verify_tournament[0]['tours'].pop(-1)
                verify_tournament[0]['tours'].append(tour_dict)
                db_tournament.update({'tours': verify_tournament[0]['tours']},
                                     (where('name') == self.tournament.name) &
                                     (where('location') == self.tournament.location) &
                                     (where('date') == self.tournament.date.isoformat()))
            self.choice_tournament()

    def resume_tournament(self):
        """resume a old tournament """
        tournament_list = self.report.extract_list('tournament')
        choice = self.tournament_menu.prompt_for_resume_tournament(tournament_list)
        self.tournament = tournament_list[choice]
        self.tournament.date = datetime.date.fromisoformat(self.tournament.date)
        player_list = []
        tours_list = []
        for player_dict in self.tournament.players:
            player = Player(player_dict)
            player_list.append(player)
        for tour_dict in self.tournament.tours:
            #pprint.pprint(tour_dict)
            tour = Tour(tour_dict)
            tour.beginning_hour = datetime.datetime.fromisoformat(tour.beginning_hour)
            if tour.end_time is not None:
                tour.end_time = datetime.datetime.fromisoformat(tour.end_time)
            tour_list = []
            for matchs_dict in tour.tour:
                #pprint.pprint(matchs_dict)
                match_list = []
                for matchs_dict in matchs_dict:
                    #pprint.pprint(matchs_list)
                    match = []
                    for match_dict in matchs_dict:
                        association = []
                        for association_dict in match_dict:
                            pprint.pprint(association_dict)
                            player_asso = Player(association_dict['player'])
                            association_object = Association({'player': player_asso, 'result': association_dict['result']})
                            association.append(association_object)
                        match.append(association)
                    match_list.append(match)
                tour_list.append(match_list)
            tour.tour = tour_list
            tours_list.append(tour)
            self.tour = tour
        self.tournament.tours = tours_list
        self.tournament.players = player_list
        self.choice_tournament()
