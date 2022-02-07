import datetime
from tinydb import TinyDB
from views.report import Report
from views.tournament import TournamentMenu
from models.tournament import Tournament
from models.player import Player
from models.tour import Tour
from models.association import Association


class ReportController:
    """class controller report"""

    def __init__(self, main):
        self.report_view = Report()
        self.db = TinyDB('db.json')
        self.main = main
        self.tournament_menu = TournamentMenu()

    def choice_report(self):
        """choice menu report"""
        menu_report = self.report_view.prompt_for_choice()
        if menu_report == 0:
            self.sort_player_by_alphabetical_name()
        elif menu_report == 1:
            self.sort_player_by_ranking()
        elif menu_report == 2:
            self.display_player_of_tournament_by_alphabatical()
        elif menu_report == 3:
            self.display_player_of_tournament_by_ranking()
        elif menu_report == 4:
            self.sort_tournament_by_alphabetical_name()
        elif menu_report == 5:
            self.display_tour_of_tournament()
        elif menu_report == 6:
            self.display_match_of_tournament()
        elif menu_report == 7:
            self.main.run()
        else:
            self.choice_report()

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
        """extract and call the method to sort player by ranking"""
        players = self.extract_list("player")
        list_sorted = self.sort_players_ranking(players)
        self.display_list(list_sorted)

    def display_list(self, list_sorted: list):
        """call the view to display the list"""
        self.report_view.display_list(list_sorted)
        self.choice_report()

    def sort_player_by_alphabetical_name(self):
        """extract an call the method to sort player by alphabetical name"""
        players = self.extract_list("player")
        list_sorted = self.sort_by_alphabetical_order(players)
        self.display_list(list_sorted)

    def sort_tournament_by_alphabetical_name(self):
        """extract an call the method to sort tournament by alphabetical name"""
        tournament = self.extract_list("tournament")
        list_sorted = self.sort_by_alphabetical_order(tournament)
        self.display_list(list_sorted)

    def sort_by_alphabetical_order(self, list_object: list) -> list:
        """sort a player list by alphabetical"""
        list_sort_by_alphabetical = []
        while len(list_object) > 0:
            object_name_max = ''
            object_max = None
            for instance in list_object:
                if instance.name >= object_name_max:
                    object_max = instance
                    object_name_max = instance.name
            list_sort_by_alphabetical.append(object_max)
            list_object.remove(object_max)
        return list_sort_by_alphabetical

    def sort_players_ranking(self, players: list) -> list:
        """sort a player list by ranking"""
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

    def extract_data_tournament(self) -> Tournament:
        tournament_list = self.extract_list('tournament')
        choice = self.tournament_menu.prompt_for_resume_tournament(tournament_list)
        tournament = tournament_list[choice]
        tournament.date = datetime.date.fromisoformat(tournament.date)
        player_list = []
        tours_list = []
        for player_dict in tournament.players:
            player = Player(player_dict)
            player_list.append(player)
        for tour_dict in tournament.tours:
            tour = Tour(tour_dict)
            tour.beginning_hour = datetime.datetime.fromisoformat(tour.beginning_hour)
            if tour.end_time is not None:
                tour.end_time = datetime.datetime.fromisoformat(tour.end_time)
            tour_list = []
            for matchs_dict in tour.tour:
                match_list = []
                for matchs_dict in matchs_dict:
                    match = []
                    for match_dict in matchs_dict:
                        association = []
                        for association_dict in match_dict:
                            player_asso = Player(association_dict['player'])
                            association_object = Association(
                                {'player': player_asso, 'result': association_dict['result']})
                            association.append(association_object)
                        match.append(association)
                    match_list.append(match)
                tour_list.append(match_list)
            tour.tour = tour_list
            tours_list.append(tour)
            tour = tour
        tournament.tours = tours_list
        tournament.players = player_list
        return tournament

    def display_tour_of_tournament(self):
        """display a tournament"""
        tournament = self.extract_data_tournament()
        self.report_view.display_tournament(tournament)
        self.choice_report()

    def display_match_of_tournament(self):
        tournament = self.extract_data_tournament()
        self.report_view.display_matchs(tournament)
        self.choice_report()

    def display_player_of_tournament_by_alphabatical(self):
        tournament = self.extract_data_tournament()
        list_players = self.sort_by_alphabetical_order(tournament.players)
        self.report_view.display_list(list_players)
        self.choice_report()

    def display_player_of_tournament_by_ranking(self):
        tournament = self.extract_data_tournament()
        list_players = self.sort_players_ranking(tournament.players)
        self.report_view.display_list(list_players)
        self.choice_report()
