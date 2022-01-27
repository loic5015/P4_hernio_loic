class View:
    """basic menu"""

    def prompt_for_choice(self) -> int:
        """prompt for choice menu"""
        print("Choississez l'action à réaliser:")
        print("1 . gérer un nouveau tournoi")
        print("2 . générer les rapports")
        try:
            choice = int(input("taper 1 ou 2:"))
        except ValueError:
            print("Erreur: Vous devez taper un nombre !!")
        else:
            if choice not in [1,2]:
                print("Vous devez taper 1 ou 2")
                self.prompt_for_choice()
            return choice

    def prompt_for_tournament_menu(self) -> int:
        """prompt for tournament menu"""
        print("Choississez l'action à réaliser:")
        print("1 . création d'un nouveau tournoi")
        print("2 . ajouter un joueur")
        try:
            choice = int(input("taper 1 ou 2:"))
        except ValueError:
            print("Erreur: Vous devez taper un nombre !!")
        else:
            if choice not in [1,2]:
                print("Vous devez taper 1 ou 2")
                self.prompt_for_choice()
            return choice

    def create_new_tournament(self) -> list:
        """creer un nouveau tournoi"""
        tournament = []
        time_control = None
        number_of_turns = None
        name = input("Quel est le nom du tournoi ?")
        localisation = input("Quel est le lieu du tournoi ?")
        incorrect = True
        while incorrect:
            choice = int(input("choississez le controle du temps 1. bullet, 2. blitz, 3. coup rapide"))
            if choice == 1:
                time_control = "bullet"
                incorrect = False
            elif choice == 2:
                time_control = "blitz"
                incorrect = False
            elif choice == 3:
                time_control = "coup rapide"
                incorrect = False
            else :
                "Vous n'avez pas entré le bon choix !!"
        description = input("Entrez une description pour le tournoi.")
        incorrect = True
        while incorrect:
            number_of_turns = int(input("Entrez le nombre de tour (facultatif par défaut 4"))
            if number_of_turns is not None:
                try:
                    number_of_turns = int(number_of_turns)
                except ValueError:
                    print("Vous n'avez pas rentré un nombre !!")
                else:
                    incorrect = False

        tournament.append(name)
        tournament.append(localisation)
        tournament.append(time_control)
        tournament.append(description)
        tournament.append(number_of_turns)
        return tournament

    def prompt_for_new_game(self):
        """Request to replay."""
        print("Souhaitez vous refaire un tournoi ?")
        choice = input("Y/n: ")
        if choice == "n":
            return False
        return True