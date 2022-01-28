
import datetime
from .player import Player
from .tour import Tour



class Tournament:

    def __init__(self, name: str, location: str, time_control: str, description: str, numbers_of_turn=4) -> None:
        """initialize name, location, date, time_control, description, numbers of turn, players and tours"""
        self.name = name
        self.location = location
        self.date = datetime.date.today()
        self.time_control = time_control
        self.description = description
        self.numbers_of_turn = numbers_of_turn
        self.players = []
        self.tours = []

    def add_players(self, player: Player) -> None:
        self.players.append(player)

    def add_tours(self, tour: Tour) -> None:
        self.tours.append(tour)

    def __str__(self):
        """Used in print."""
        return f"{self.name} de {self.location}"

    def __repr__(self):
        """Used in print."""
        return str(self)