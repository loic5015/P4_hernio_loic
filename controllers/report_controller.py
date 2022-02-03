from tinydb import TinyDB, where
from views.report import Report
from models.tournament import Tournament
from models.player import Player
#from .main_controller import Main


class ReportController:

    def __init__(self):
        self.report_view = Report()
        self.db = TinyDB('db.json')

    def choice_report(self):
        """choice menu report"""
        menu_report = self.report_view.prompt_for_choice()
        if menu_report == 0:
            self.sort_player_by_alphabetical_name()
        elif menu_report == 1:
            self.sort_player_by_ranking()
        elif menu_report == 2:
            pass
        elif menu_report == 3:
            pass
        elif menu_report == 4:
            self.sort_tournament_by_alphabetical_name()
        elif menu_report == 5:
            self.sort_tournament_by_alphabetical_name()
        elif menu_report == 7:
            #self.main.run()
            pass
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
        """extract an call the method to sort player by ranking"""
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
        list_sorted = self.sort_players_alphabetical(players)
        self.display_list(list_sorted)

    def sort_tournament_by_alphabetical_name(self):
        """extract an call the method to sort tournament by alphabetical name"""
        tournament = self.extract_list("tournament")
        list_sorted = self.sort_players_alphabetical(tournament)
        self.display_list(list_sorted)

    def sort_players_alphabetical(self, players: list) -> list:
        """sort a player list by alphabetical"""
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
