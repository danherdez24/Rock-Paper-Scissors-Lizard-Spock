import random
from player import Player
class AI(Player):
    def __init__(self):
            super().__init__("AI")
    def choose_gesture(self):
        self.chosen_gesture = random.choice(self.gestures)
