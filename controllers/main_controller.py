
from tinydb import TinyDB, where
from views.start_menu import StartMenu
from .report_controller import ReportController
from .tournament_controller import TournamentController


class Main:
    """class main controller"""

    def __init__(self):
        self.start_menu = StartMenu()
        self.db = TinyDB('db.json')
        self.report = ReportController(self)
        self.tournament_controller = TournamentController(self)

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
        self.run()

    def run(self):
        """launch the start menu"""
        running = True
        while running:
            main_menu = self.start_menu.prompt_for_choice()
            if main_menu == 0:
                self.tournament_controller.choice_tournament()
            elif main_menu == 1:
                self.report.choice_report()
            elif main_menu == 2:
                self.modify_ranking_player()
            elif main_menu == 3:
                running = False
            else:
                self.run()


