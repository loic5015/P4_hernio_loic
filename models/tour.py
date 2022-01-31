import datetime


class Tour:

    def __init__(self, name: str) -> None:
        """initialize name, tour, beginning hour, end time"""
        self.name = name
        self.tour = []
        self.beginning_hour = datetime.datetime.now()
        self.end_time = None

    def add_match(self, match: list) -> None:
        self.tour.append(match)

    def list_match(self) -> list:
        return self.tour

    def create_end_time(self) -> None:
        self.end_time = datetime.datetime.now()

    def __str__(self):
        """Used in print."""
        return f"{self.name} à {self.beginning_hour.strftime('%m/%d/%Y, %H:%M:%S')}"

    def __repr__(self):
        """Used in print."""
        return str(self)