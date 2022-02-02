class Player:

    def __init__(self, name: str, surname: str, date_of_birth: str, gender: str, ranking: float):
        """initialize name, surname, date of birth, gender and ranking"""
        self.name = name
        self.surname = surname
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.ranking = ranking

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
