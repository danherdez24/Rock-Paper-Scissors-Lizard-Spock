from player import Player

class Human(Player):
    def __init__(self, name):
        super().__init__(name)

    def choose_gesture(self):
        while True:
        #how do we get user input
            user_input = input("What gesture? Enter 0 if Rock, 1 if Paper, 2 if Scissors, 3 if Lizard, 4 if Spock ")
         #how do we pull value from a list (self.gesture)
            if user_input in ["0","1","2","3","4"]:
                self.chosen_gesture = self.gestures[int(user_input)]
                break
        #how do we combine the previous two points and store chosen gesture
        
        
       





