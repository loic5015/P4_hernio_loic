from .player import Player


class Association:
    """associate player and result"""

    def __init__(self, dict_ass: dict):
        self.player = None
        self.result = 0.0
        for key in dict_ass:
            setattr(self, key, dict_ass[key])

    def post_result(self, result: float) -> None:
        self.result = result

    def get_result(self) -> float:
        return self.result

    def get_player(self) -> Player:
        return self.player

    def return_dict(self):
        return {'player': self.player.__repr__(), 'result': self.result}

    def __str__(self):
        """Used in print."""
        return f"{str(self.player)} score:{self.result:4}"

    def __repr__(self):
        """Used in print."""
        return f"{str(self.player)}, {self.result}"
