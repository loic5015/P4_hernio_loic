from models.tournament import Tournament

ITEM_REPORT_MENU = ["Lister tous les acteurs par ordre alphabétique.", "Lister tous les acteurs par classement.",
                    "Lister tous les joueurs d'un tournoi par ordre alphabétique.",
                    "Lister tous les joueurs d'un tournoi par classement.", "Lister tous les tournois.",
                    "Lister de tous les tours d'un tournoi.", "Lister tous les matchs d'un tournoi",
                    "Revenir au menu principal"]


class Report:
    """views of the report page"""

    def prompt_for_choice(self) -> int:
        """prompt for choice menu"""
        i = 0
        current_menu = True
        index = None
        while current_menu:
            print("Choisir l'action à réaliser:")
            for choice in ITEM_REPORT_MENU:
                print(f"[{i} . {choice}]")
                i = i + 1
            try:
                choice = input("taper 0 ou " + str(len(ITEM_REPORT_MENU) - 1) + " : ")
                index = int(choice)
            except ValueError:
                print("Erreur: Vous devez taper un nombre !!")
                i = 0
            else:
                if index not in [x for x in range(len(ITEM_REPORT_MENU))]:
                    print("Votre choix est incorrect !")
                    i = 0
                else:
                    current_menu = False
        return index

    def display_tournament(self, tournament: Tournament):
        """display tournament in view"""
        print(str(tournament))
        self.display_list(tournament.tours)

    def display_matchs(self, tournament: Tournament):
        """display matchs in view"""
        print(str(tournament))
        for tour in tournament.tours:
            print(str(tour))
            for match in tour.tour:
                self.display_list(match)

    def display_list(self, list_sorted: list):
        """display a list"""
        for list in list_sorted:
            print(str(list))
