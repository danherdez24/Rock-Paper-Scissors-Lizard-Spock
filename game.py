from human import Human
from ai import AI
class Game:
    # players = int(input("How many players are going to play?"))

    def __init__(self) -> None:
        self.player1 = Human(input("Enter username: "))
        self.player2 = None

    def choose_game_type(self):
        while True:
            user_input = input("How many players 1 or 2? ")
            if user_input == "1":
                self.player2 = AI()
                break
            elif user_input == "2":
                self.player2 = Human(input("Enter username: "))
                break
    def run_game(self):
        self.choose_game_type()
        self.player1.choose_gesture()
        pass

    def best_of_three(self):
        while self.player1.score < 3 and self.player2.score < 3:
            pass
