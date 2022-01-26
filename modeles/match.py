import datetime


class Tour:

    def __init__(self, name: str):
        """initialize name, tour, beginning hour, end time"""
        self.name = name
        self.tour = []
        self.beginning_hour = datetime.datetime.now()
        self.end_time = None

    def add_match(self, match: tuple):
        self.tour.append(match)

    def create_end_time(self):
        self.end_time = datetime.datetime.now()