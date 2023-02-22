from player import Player

class Human(Player):
    
    def choose_gesture(self):
        print(self.gestures[0])
        #how do we get user input
        #how do we pull value from a list (self.gesture)
        #how do we comebine the previous two points and store chosen gesture
        username = input("Enter username: ")
        print("Username is " + username)

        
Player1 = Human("Bob")
Player1.choose_gesture()

