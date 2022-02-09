ITEM_TOURNAMENT = ["créer un nouveau tournoi", "ajouter un joueur", "generer un nouveau tour",
                   "afficher les tours", "entrer les résultats", "afficher les résultats du tournoi",
                   "reprendre un tournoi", "revenir au menu principal"]

TIME_CONTROL = ["bullet", "blitz", "coup rapide"]
SEXE = ["féminin", "masculin"]
NUMBER_OF_TURN = 4


class TournamentMenu:

    def prompt_for_tournament_menu(self) -> int:
        """prompt for tournament menu"""
        print("Choississez l'action à réaliser:")
        i = 0
        choice = None
        current_menu = True
        while current_menu:
            for menu in ITEM_TOURNAMENT:
                print(f"[{i} . {menu}]")
                i = i + 1
            try:
                choice = int(input("tapez votre choix de 0 à " + str(len(ITEM_TOURNAMENT) - 1) + " : "))
            except ValueError:
                print("Erreur: Vous devez taper un nombre !!")
                i = 0
            else:
                if choice not in [x for x in range(len(ITEM_TOURNAMENT))]:
                    print("Votre choix est incorrect !")
                    i = 0
                else:
                    current_menu = False
        return choice

    def prompt_for_resume_tournament(self, list_object: list) -> int:
        """prompt for tournament menu"""
        print("Choississez l'action à réaliser:")
        i = 0
        current_menu = True
        choice = None
        while current_menu:
            for tournament in list_object:
                print(f"[{i} . {tournament}]")
                i = i + 1
            try:
                choice = int(input("tapez votre choix de 0 à " + str(len(list_object) - 1) + " : "))
            except ValueError:
                print("Erreur: Vous devez taper un nombre !!")
            else:
                if choice not in [x for x in range(len(list_object))]:
                    print("Votre choix est incorrect !")
                    i = 0
                else:
                    current_menu = False
        return choice

    def create_new_tournament(self) -> dict:
        """create a new tournament"""
        tournament = {}
        current_menu = True
        while current_menu:
            tournament['name'] = input("Quel est le nom du tournoi ?")
            if tournament['name'] is not None:
                current_menu = False
        current_menu = True
        while current_menu:
            tournament['location'] = input("Quel est le lieu du tournoi ?")
            if tournament['location'] is not None:
                current_menu = False
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
        current_menu = True
        while current_menu:
            tournament['description'] = input("Entrez une description pour le tournoi.")
            if tournament['description'] is not None:
                current_menu = False
        current_menu = True
        while current_menu:
            number = input("Entrez le nombre de tour (facultatif par défaut 4) :")
            if number == "":
                number = NUMBER_OF_TURN
            try:
                tournament['numbers_of_turn'] = int(number)
            except ValueError:
                print("Vous n'avez pas rentré un nombre !!")
            else:
                current_menu = False
        current_menu = True
        while current_menu:
            number = input("Entrez le nombre de joueurs :")
            try:
                tournament['numbers_of_players'] = int(number)
            except ValueError:
                print("Vous n'avez pas rentré un nombre !!")
            else:
                current_menu = False
        tournament['time_control'] = TIME_CONTROL[index]
        return tournament

    def add_player(self) -> dict:
        """add a player"""
        player = {}
        current_menu = True
        while current_menu:
            name = input("Entrez le nom du joueur :")
            if name is not None:
                current_menu = False
                player['name'] = name
        current_menu = True
        while current_menu:
            surname = input("Entrez le prénom du joueur :")
            if surname is not None:
                player['surname'] = surname
                current_menu = False
        current_menu = True
        while current_menu:
            date_of_birth = input("Entrez la date de naissance du joueur :")
            if date_of_birth is not None:
                current_menu = False
                player['date_of_birth'] = date_of_birth
        current_menu = True
        i = 0
        index = None
        while current_menu:
            print("choississez le sexe du joueur :")
            for choice in SEXE:
                print(f"[{i} . {choice}]")
                i = i + 1
            try:
                index = int(input("taper 0 ou " + str(len(SEXE) - 1) + " : "))
            except ValueError:
                print("Erreur: Vous devez taper un nombre !!")
                i = 0
            else:
                if index not in [x for x in range(len(SEXE))]:
                    print("Votre choix est incorrect !")
                    i = 0
                else:
                    current_menu = False
        current_menu = True
        ranking = None
        while current_menu:
            try:
                ranking = float(input("Entrez le classement du joueur :"))
            except ValueError:
                print("Vous devez taper un nombre !")
            else:
                current_menu = False
        player['ranking'] = ranking
        player['gender'] = SEXE[index]
        return player

    def nombre_max_atteint(self):
        """warning message number of players reach"""
        print("Vous avez atteint le nombre maximum de joueurs !")

    def number_player_not_reach(self):
        """warning message number of players not reach"""
        print("ils manquent des joueurs pour lancer le tournoi !")

    def tour_is_over(self):
        """warning message number of players not reach"""
        print("Le tour est terminé !")

    def number_of_turns_reach(self):
        """warning message number of players not reach"""
        print("Vous avez atteint le nombre maximum de tours !")

    def tournoi_has_been_create(self):
        """warning message tournament has not been created"""
        print("Vous devez creer un tournoi !")

    def tour_has_been_create(self):
        """warning message tournament has not been created"""
        print("Vous devez creer un tour !")

    def previous_tour_not_finish(self):
        """warning message previous tour not finished"""
        print("Vous devez entrez les résultats du tour précédent !")

    def display_tour(self, tournament):
        """display the tours"""
        for tour in tournament.tours:
            print(str(tour))
            for matchs in tour.tour:
                i = 1
                for match in matchs:
                    print("match " + str(i) + " :")
                    print(str(match))
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
