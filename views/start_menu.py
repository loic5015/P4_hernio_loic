START_MENU = ["gérez un nouveau tournoi", "générez les rapports", "sortir du programme"]


class StartMenu:
    """basic menu"""

    def prompt_for_choice(self) -> int:
        """prompt for choice menu"""
        i = 0
        condition = True
        indice = None
        while condition:
            print("Choississez l'action à réaliser:")
            for choice in START_MENU:
                print(f"[{i} . {choice}]")
                i = i + 1
            try:
                indice = int(input("taper 0 ou " + str(len(START_MENU) - 1) + " : "))
            except ValueError:
                print("Erreur: Vous devez taper un nombre !!")
                i = 0
            else:
                if indice not in [x for x in range(len(START_MENU))]:
                    print("Votre choix est incorrect !")
                    i = 0
                    self.prompt_for_choice()
                else:
                    condition = False
                    return indice


    def prompt_for_new_game(self):
        """Request to replay."""
        print("Souhaitez vous refaire un tournoi ?")
        choice = input("Y/n: ")
        if choice == "n":
            return False
        return True