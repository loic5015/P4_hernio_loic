
import datetime
from .player import Player
from .tour import Tour


class Tournament:
    """models of tournament"""

    def __init__(self, dict_tournament: dict) -> None:
        """initialize name, location, date, time_control, description, numbers of turn, players and tours"""
        self.name = None
        self.location = None
        self.date = datetime.date.today()
        self.time_control = None
        self.description = None
        self.numbers_of_turn = None
        self.players = []
        self.tours = []
        for key in dict_tournament:
            setattr(self, key, dict_tournament[key])

    def add_players(self, player: Player) -> None:
        """add new players in tournament"""
        self.players.append(player)

    def add_tours(self, tour: Tour) -> None:
        """add new tour in tournament"""
        self.tours.append(tour)

    def __str__(self):
        """Used in print."""
        return f"nom: {self.name:15} lieu: {self.location:15} date: {self.date}"

    def __repr__(self):
        """Used in print."""
        return {'name': self.name, 'location': self.location, 'date': self.date.isoformat(),
                'time_control': self.time_control, 'description': self.description,
                'numbers_of_turn': self.numbers_of_turn, 'players': self.players,
                'tours': self.tours}
