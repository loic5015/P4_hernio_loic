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

    def get_name(self) -> str:
        return self.name

    def get_surname(self) -> str:
        return self.surname

    def get_date_of_birth(self) -> str:
        return self.date_of_birth

    def get_gender(self) -> str:
        return self.gender

    def get_ranking(self) -> float:
        return self.ranking

    def set_attribute_player(self, dict_player: dict):
        for key in dict_player:
            setattr(self, key, dict_player[key])

    def __str__(self):
        """Used in print."""
        return f"{self.name} {self.surname} {self.ranking}"

    def __repr__(self):
        """Used in print."""
        return {'name': self.name, 'surname': self.surname, 'day_of_birth': self.date_of_birth, 'gender': self.gender,
                'ranking': self.ranking}
