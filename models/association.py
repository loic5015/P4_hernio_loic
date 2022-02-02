from .player import Player


class Association:
    """associate player and result"""

    def __init__(self, player: Player):
        self.player = player
        self.result = 0

    def post_result(self, result: float) -> None:
        self.result = result

    def get_result(self) -> float:
        return self.result

    def get_player(self) -> Player:
        return self.player

    def __str__(self):
        """Used in print."""
        return f"{self.player}, {self.result}"

    def __repr__(self):
        """Used in print."""
        return {'player': self.player.__repr__(), 'result': self.result}
