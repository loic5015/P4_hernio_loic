REPORT_MENU = ["Liste de tous les tournois.", "Liste de tous les tours d'un tournoi.",
               "Liste de tous les matchs d'un tournoi."]


class Report:
"""views of the report page"""

    def prompt_for_choice(self) -> int:
        """prompt for choice menu"""
        i = 0
        current_menu = True
        index = None
        while current_menu:
            print("Choisir l'action à réaliser:")
            for choice in REPORT_MENU:
                print(f"[{i} . {choice}]")
                i = i + 1
            try:
                index = int(input("taper 0 ou " + str(len(REPORT_MENU) - 1) + " : "))
            except ValueError:
                print("Erreur: Vous devez taper un nombre !!")
                i = 0
            else:
                if index not in [x for x in range(len(REPORT_MENU))]:
                    print("Votre choix est incorrect !")
                    i = 0
                    self.prompt_for_choice()
                else:
                    current_menu = False
                    return index