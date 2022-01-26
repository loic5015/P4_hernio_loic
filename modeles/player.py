class Player:

    def __init__(self, name: str, surname: str, date_of_birth: str, gender: str, ranking: int):
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

    def get_date_of_bith(self) -> str:
        return self.date_of_birth

    def get_gender(self) -> str:
        return self.gender

    def get_ranking(self) -> int:
        return self.ranking