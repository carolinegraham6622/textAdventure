"""
Text Adventure Game
An adventure in making adventure games.

Refer to the instructions on Canvas for more information.

"""
__author__ = "Caroline Graham"
__version__ = 2

class Player:
    location = ''
    
    def __init__(self, location):
        self.location = location
    def set_location(self, location):
        self.location = location
    def print_location(self):
        print(self.location)

class World:
    #attributes
    player = Player('default')
    game_status = 'playing'
    options = ['']
    hasKey = False
    checkPocket = False
    
    #consumes null
    #produces null
    #initializes all World attributes, including Player player and game_status
    def __init__(self):
        self.player.set_location('starting room')
        self.game_status = 'playing'
        pass
    
    #consumes null
    #produces boolean whether game should end
    #check game_status, ends if anything other than playing
    def is_done(self):
        if self.game_status != 'playing':
            return True
        else:
            return False
        pass
    
    #consumes null
    #produces boolean valid World state
    def is_good(self):
        return True
    
    #consumes null
    #produces a str of text to print (dont print, just str)
    #include: player location, options
    def render(self):
        prompt = '-------\nYou are currently at: ' + self.player.location + "\nWhat would you like to do?"
        options = self.state_options()
        for x in range(len(options)):
            prompt += "\n" + options[x]
        return prompt
    
    #consumes str input 
    #produces bool on valid input based on location/state
    def is_input_good(self, input):
        options = self.state_options()
        input = input.upper()
        if input in options:
            print('valid input')
            return True
        else:
            print('invalid input')
            return False
        pass
    
    #consumes null
    #produces bool show options based on state/location
    def state_options(self):
        loc = self.player.location
        if loc == "starting room":
            if self.checkPocket == False:
                options = ["INSPECT POCKETS","OPEN DOOR","QUIT"]
            else:
                options = ["INSPECT PAPER","OPEN DOOR","QUIT"]
        elif loc == "hallway":
            options = ["GO BACK", "QUIT"]
        return options
    
    #update the state based on input
    def process(self, input):
        input = input.upper()
        loc = self.player.location
        if loc == 'starting room':
            if input == 'OPEN DOOR':
                if self.hasKey == False:
                    print("The door is locked. Maybe there key is somewhere in this room?")
                else:
                    print("The door creaks open, you listen for any noise before stepping into the dark hallway that awaits you.")
                    self.location = hallway
            elif input == "INSPECT POCKETS":
                print("You don't seem to have an visible injuries, but your joints are sore, " 
                + "like they haven't moved in a while.  Moving on to your pockets, you slip"
                + " your hand into your jacket pocket to find a scrap of paper.")
                self.checkPocket = True
            elif input == "INSPECT PAPER":
                print("You pull the crumpled paper out and smooth it out to the best of your ability."
                    + "\nWhat you read makes your whole body go cold."
                    + "HE IS LOOKING FOR YOU\nDON'T LET HIM CATCH YOU\nGET OUT. NOW."
                    + "Your upper lip starts to sweat, and not just because of the words on the paper;"
                    + "you regonize the handwriting... it's YOUR handwriting. You have no memory of ever writing such a note."
                    + "But who better to trust than yourself? You take the warning to heart; you need to get out of here- where ever HERE is- as soon as possible.")
            #fix so option goes away
            else:
                self.game_status = 'quit'
        elif loc == "hallway":
            if input == "GO BACK":
                self.location = "starting room"
            else:
                self.game_status = 'quit'
        pass
    
    
    def tick(self):
        pass
    
    def render_start(self):
        return "The Mystery of Bly Manor\nYou awake to find yourself on the floor in an unfamiliar room.  \nThere is a single lightbulb hanging from the center of the cieling.  It flickers steadily. The room is mostly bare at first glance; there is a single dresser up against the opposide wall and a door to the right of it."
    
    def render_ending(self):
        status = ''
        if self.game_status == 'won':
            status = "You win."
        elif self.game_status == 'lost':
            status = "You lost."
        else:
            status = "You quit."
        return status
        
# Command Paths to give to the unit tester
WIN_PATH = ""
LOSE_PATH = ""

def main():
    '''
    This is the Main game function. When executed, it begins a run of the game.
    Read over it to understand the engine that you are using and the order
    that the methods are executed in.
    '''
    world = World()
    print(world.render_start())
    while not world.is_done():
        if not world.is_good():
            raise ValueError("The world is in an invalid state.", world)
        print(world.render())
        is_input_good = False
        while not is_input_good:
            user_input = input("")
            is_input_good = world.is_input_good(user_input)
        world.process(user_input)
        world.tick()
    print(world.render_ending())

# Executes the main function only if this file is being run directly.
# This prevents the autograder from being confused. Never call main outside
# of this IF statement!
if __name__ == "__main__":
    ## You might comment out the main function and call each function
    ## one at a time below to try them out yourself
    main()
    ## e.g., comment out main() and uncomment the line(s) below
    world = World()
    world.is_done()
    print(world.render())
