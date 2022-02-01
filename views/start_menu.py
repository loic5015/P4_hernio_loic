ITEM_MENU = ["gérer un nouveau tournoi", "visualiser le menu des rapports", "sortir du programme"]


class StartMenu:
    """basic menu"""

    def prompt_for_choice(self) -> int:
        """prompt for choice menu"""
        i = 0
        current_menu = True
        index = None
        while current_menu:
            print("Choississez l'action à réaliser:")
            for choice in ITEM_MENU:
                print(f"[{i} . {choice}]")
                i = i + 1
            try:
                index = int(input("taper 0 ou " + str(len(ITEM_MENU) - 1) + " : "))
            except ValueError:
                print("Erreur: Vous devez taper un nombre !!")
                i = 0
            else:
                if index not in [x for x in range(len(ITEM_MENU))]:
                    print("Votre choix est incorrect !")
                    i = 0
                    self.prompt_for_choice()
                else:
                    current_menu = False
                    return index


    def prompt_for_new_game(self):
        """Request to replay."""
        print("Souhaitez vous refaire un tournoi ?")
        choice = input("Y/n: ")
        if choice == "n":
            return False
        return True