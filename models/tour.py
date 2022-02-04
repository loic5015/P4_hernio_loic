import datetime


class Tour:

    def __init__(self, dict_tour: dict) -> None:
        """initialize name, tour, beginning hour, end time"""
        self.name = None
        self.tour = []
        self.beginning_hour = datetime.datetime.now()
        self.end_time = None
        for key in dict_tour:
            setattr(self, key, dict_tour[key])

    def add_match(self, match: list) -> None:
        """add match in tour"""
        self.tour.append(match)

    def create_end_time(self) -> None:
        """enter a value in self.end_time"""
        self.end_time = datetime.datetime.now()

    def __str__(self):
        """Used in print."""
        return f"tour: {self.name:8} debut: {self.beginning_hour.strftime('%m/%d/%Y, %H:%M:%S')} fin: " \
               f"{self.end_time.strftime('%m/%d/%Y, %H:%M:%S') if self.end_time is not None else ''}"

    def __repr__(self):
        """Used in print."""
        return {'name': self.name, 'tour': self.tour, 'beginning_hour': self.beginning_hour.isoformat(),
                'end_time': self.end_time.isoformat() if self.end_time is not None else None}
