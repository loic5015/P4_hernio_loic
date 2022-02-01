from tinydb import TinyDB
from controllers.base import Controller
from views.start_menu import StartMenu
from views.tournament import TournamentMenu

def main():
    start_menu = StartMenu()
    tournament_menu = TournamentMenu()
    db = TinyDB('db.json')
    game = Controller(start_menu, tournament_menu, db)
    game.run()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
