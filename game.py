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
        self.best_of_three()
        pass

    def best_of_three(self):
        while self.player1.score < 3 and self.player2.score < 3:
            self.player1.choose_gesture()
            # p2 choose
            self.player2.choose_gesture()
            # if tie
            if self.player1.chosen_gesture == "Rock" and self.player2.chosen_gesture == "Rock":
                print("It's a tie")

            elif self.player1.chosen_gesture == "Paper" and self.player2.chosen_gesture == "Paper":
                print("It's a tie")

            elif self.player1.chosen_gesture == "Scissors" and self.player2.chosen_gesture == "Scissors":
                print("It's a tie")

            elif self.player1.chosen_gesture == "Lizard" and self.player2.chosen_gesture == "Lizard":
                print("It's a tie")

            elif self.player1.chosen_gesture == "Spock" and self.player2.chosen_gesture == "Spock":
                print("It's a tie")

            elif self.player1.chosen_gesture == "Rock" and self.player2.chosen_gesture == "Scissors":
                print("Rock crushes Scissors")

            elif self.player1.chosen_gesture == "Scissors" and self.player2.chosen_gesture == "Paper":
                print("Scissors cuts Paper")

            elif self.player1.chosen_gesture == "Paper" and self.player2.chosen_gesture == "Rock":
                print("Paper covers Rock")

            elif self.player1.chosen_gesture == "Rock" and self.player2.chosen_gesture == "Lizard":
                print("Rock crushes Lizard")

            elif self.player1.chosen_gesture == "Lizard" and self.player1.chosen_gesture == "Spock":
                print("Lizard poisons Spock")

            elif self.player1.chosen_gesture == "Spock" and self.player2.chosen_gesture == "Scissors":
                print("Spock smashes Scissors")

            elif self.player1.chosen_gesture == "Scissors" and self.player2.chosen_gesture == "Lizard":
                print("Scissors decapitate Lizard")

            elif self.player1.chosen_gesture == "Lizard" and self.player2.chosen_gesture == "Paper":
                print("Lizard eats Paper")

            elif self.player1.chosen_gesture == "Paper" and self.player2.chosen_gesture == "Spock":
                print("Paper disproves Spock")

            elif self.player1.chosen_gesture == "Spock" and self.player2.chosen_gesture == "Rock":
                print("Spock vaporizes Rock")

            elif self.player1.chosen_gesture == "Scissors" and self.player2.chosen_gesture == "Rock":
                print("Rock crushes Scissors")

            elif self.player1.chosen_gesture == "Paper" and self.player2.chosen_gesture == "Scissors":
                print("Scissors cuts Paper")

            elif self.player1.chosen_gesture == "Rock" and self.player2.chosen_gesture == "Paper":
                print("Paper covers Rock")

            elif self.player1.chosen_gesture == "Lizard" and self.player1.chosen_gesture == "Rock":
                print("Rock crushes Lizard")

            elif self.player1.chosen_gesture == "Spock" and self.player2.chosen_gesture == "Lizard":
                print("Lizard poisons Spock")

            elif self.player1.chosen_gesture == "Scissors" and self.player2.chosen_gesture == "Spock":
                print("Spock smashes Scissors")

            elif self.player1.chosen_gesture == "Lizard" and self.player2.chosen_gesture == "Scissors":
                print("Scissors decapitate Lizard")

            elif self.player1.chosen_gesture == "Paper" and self.player2.chosen_gesture == "Lizard":
                print("Lizard eats Paper")

            elif self.player1.chosen_gesture == "Spock" and self.player2.chosen_gesture == "Paper":
                print("Paper disproves Spock")

            elif self.player1.chosen_gesture == "Rock" and self.player2.chosen_gesture == "Spock":
                print("Spock vaporizes Rock")

            
            # ~20 elifs
            pass
