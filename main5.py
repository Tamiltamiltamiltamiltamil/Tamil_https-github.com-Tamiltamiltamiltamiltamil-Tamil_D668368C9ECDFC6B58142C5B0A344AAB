# Define the Player class
class Player:
    # Define the constructor
    def __init__(self, name):
        # Assign the name attribute
        self.name = name
    
    # Define the play() method
    def play(self):
        # Print a message
        print("The player is playing cricket.")

# Define the Batsman class as a subclass of Player
class Batsman(Player):
    # Override the play() method
    def play(self):
        # Print a message
        print("The batsman is batting.")

# Define the Bowler class as a subclass of Player
class Bowler(Player):
    # Override the play() method
    def play(self):
        # Print a message
        print("The bowler is bowling.")

# Create an object of the Batsman class
batsman = Batsman("Virat Kohli")

# Create an object of the Bowler class
bowler = Bowler("Jasprit Bumrah")

# Call the play() method for each object
batsman.play()
bowler.play()