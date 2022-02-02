ITEM_REPORT_MENU = ["Lister tous les acteurs par ordre alphabétique.", "Lister tous les acteurs par classement.",
               "Lister tous les joueurs d'un tournoi par ordre alphabétique.",
               "Lister tous les joueurs d'un tournoi par classement.", "Lister tous les tournois.",
               "Lister de tous les tours d'un tournoi.", "Lister tous les matchs d'un tournoi"]


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
                index = int(input("taper 0 ou " + str(len(ITEM_REPORT_MENU) - 1) + " : "))
            except ValueError:
                print("Erreur: Vous devez taper un nombre !!")
                i = 0
            else:
                if index not in [x for x in range(len(ITEM_REPORT_MENU))]:
                    print("Votre choix est incorrect !")
                    i = 0
                    self.prompt_for_choice()
                else:
                    current_menu = False
                    return index

    def display_list(self, list_sorted: list):
        for player in list_sorted:
            print(str(player))