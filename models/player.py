class Player:

    def __init__(self, dict_player: dict):
        """initialize name, surname, date of birth, gender and ranking"""
        self.name = None
        self.surname = None
        self.date_of_birth = None
        self.gender = None
        self.ranking = None
        for key in dict_player:
            setattr(self, key, dict_player[key])

    def __str__(self):
        """Used in print."""
        return f"{self.name:15} {self.surname:15} {self.date_of_birth} {self.gender:10} {self.ranking:6}"

    def __repr__(self):
        """Used in print."""
        return {'name': self.name, 'surname': self.surname, 'date_of_birth': self.date_of_birth, 'gender': self.gender,
                'ranking': self.ranking}
