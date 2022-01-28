from .player import Player


class Association:
    """associate player and result"""

    def __init__(self, player: Player):
        self.player = player
        self.result = 0

    def post_result(self, result) -> None:
        self.result = result

