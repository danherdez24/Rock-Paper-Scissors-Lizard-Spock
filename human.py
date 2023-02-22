from player import Player

class Human(Player):
    def __init__(self, name):
        super().__init__(name)

    def choose_gesture(self):
        print(self.gestures[0])
        #how do we get user input
        #how do we pull value from a list (self.gesture)
        #how do we comebine the previous two points and store chosen gesture
       





