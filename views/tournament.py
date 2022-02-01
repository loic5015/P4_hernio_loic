ITEM_TOURNAMENT = ["créer un nouveau tournoi", "ajouter un joueur", "generer un nouveau tour",
                   "afficher les tours", "entrer les résultats", "revenir au menu principal"]

TIME_CONTROL = ["bullet", "blitz", "coup rapide"]


class TournamentMenu:

    def prompt_for_tournament_menu(self) -> int:
        """prompt for tournament menu"""
        print("Choississez l'action à réaliser:")
        i = 0
        current_menu = True
        while current_menu:
            for menu in ITEM_TOURNAMENT:
                print(f"[{i} . {menu}]")
                i = i + 1
            try:
                choice = int(input("tapez votre choix de 0 à " + str(len(ITEM_TOURNAMENT) - 1) + " : "))
            except ValueError:
                print("Erreur: Vous devez taper un nombre !!")
            else:
                if choice not in [x for x in range(len(ITEM_TOURNAMENT))]:
                    print("Votre choix est incorrect !")
                    i = 0
                    self.prompt_for_tournament_menu()
                current_menu = False
                return choice

    def create_new_tournament(self) -> list:
        """create a new tournament"""
        tournament = []
        time_control = None
        number_of_turns = None
        name = input("Quel est le nom du tournoi ?")
        localisation = input("Quel est le lieu du tournoi ?")
        i = 0
        current_menu = True
        index = None
        while current_menu:
            print("choississez le controle du temps :")
            for choice in TIME_CONTROL:
                print(f"[{i} . {choice}]")
                i = i + 1
            try:
                index = int(input("taper 0 ou " + str(len(TIME_CONTROL) - 1) + " : "))
            except ValueError:
                print("Erreur: Vous devez taper un nombre !!")
                i = 0
            else:
                if index not in [x for x in range(len(TIME_CONTROL))]:
                    print("Votre choix est incorrect !")
                    i = 0
                else:
                    current_menu = False
        description = input("Entrez une description pour le tournoi.")
        current_menu = True
        while current_menu:
            number_of_turns = input("Entrez le nombre de tour (facultatif par défaut 4) :")
            if number_of_turns is not None:
                try:
                    number_of_turns = int(number_of_turns)
                except ValueError:
                    print("Vous n'avez pas rentré un nombre !!")
                else:
                    number_of_turns = 4
                    current_menu = False

        tournament.append(name)
        tournament.append(localisation)
        tournament.append(TIME_CONTROL[index])
        tournament.append(description)
        tournament.append(number_of_turns)
        return tournament

    def add_player(self) -> list:
        """add a player"""
        player = []
        name = input("Entrez le nom du joueur :")
        player.append(name)
        surname = input("Entrez le prénom du joueur :")
        player.append(surname)
        date_of_birth = input("Entrez la date de naissance du joueur :")
        player.append(date_of_birth)
        gender = input("Entrez le sexe du joueur :")
        player.append(gender)
        current_menu = True
        ranking = None
        while current_menu:
            try:
                ranking = float(input("Entrez le classement du joueur :"))
            except ValueError:
                print("Vous devez taper un nombre !")
            else:
                current_menu = False
        player.append(ranking)
        return player

    def nombre_max_atteint(self):
        """warning message number of players reach"""
        print("Vous avez atteint le nombre maximum de joueurs !")

    def number_player_not_reach(self):
        """warning message number of players not reach"""
        print("ils manquent des joueurs pour lancer le tournoi !")

    def tournoi_has_been_create(self):
        """warning message tournament has not been created"""
        print("Vous devez creer un tournoi !")

    def tour_has_been_create(self):
        """warning message tournament has not been created"""
        print("Vous devez creer un tour !")

    def display_tour(self, tournament):
        """display the tours"""
        for tour in tournament.tours:
            print(tour.name + " " + tour.beginning_hour.strftime('%m/%d/%Y, %H:%M:%S') + " " +
                  tour.end_time.strftime('%m/%d/%Y, %H:%M:%S') if tour.end_time is not None else "")
            for matchs in tour.tour:
                i = 1
                for match in matchs:
                    print("match " + str(i) + " :")
                    print(match)
                    i = i + 1

    def enter_result(self, association):
        """enter result"""
        current_menu = True
        score = None
        while current_menu:
            try:
                print("Entrer le résultat pour le joueur :")
                score = float(input(str(association) + " : "))
            except ValueError:
                print("Vous devez entrer un nombre !")
            else:
                current_menu = False
        return score
