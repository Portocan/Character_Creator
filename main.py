from pprint import pprint
from PyInquirer import prompt


class Name:

    def __init__(self):
        self.firstname = ""
        self.lastname = ""
        self.charname = ""
        self.badname = True

    def playername(self):
        first = ""
        last = ""
        print("First thing is first, I'm going to have you enter your name.")

        while self.badname:
            first = input("What's your first name? ")
            self.checkname(first)

        # resetting badname check
        self.badname = True

        while self.badname:
            last = input("What's your last name? ")
            self.checkname(last)

        self.badname = True  # resetting badname check

        # formatting player name
        self.firstname = first.title()
        self.lastname = last.title()
        return self.lastname, self.firstname

    def avname(self):
        charname = ""

        while self.badname:
            charname = input("Now, please enter your character's name. ")
            self.checkname(charname)

        self.badname = True
        # formatting  character name
        self.charname = charname.title()
        return self.charname

    # Used to check names for numbers and flag them if that is the case
    def checkname(self, name):
        for letter in name:
            if letter.isdigit():
                self.badname = True
                print("You can't enter numbers.")
            else:
                self.badname = False
            return self.badname


class Job:

    def __init__(self):
        self.nojob = True
        self.checkjob = {}
        self.confirmjob = {}
        self.str = 0
        self.dex = 0
        self.con = 0
        self.int = 0
        self.wis = 0
        self.cha = 0

    # showing job options
    def showjob(self):
        questions = {
            "type": "list",
            "name": "job",
            "message": "Choose your class",
            "choices": ["Archer", "Barbarian", "Cleric", "Druid", "Fighter", "Wizard"]
        }
        self.checkjob = prompt(questions)
        self.nojob = False

    # assigning stats based on class
    def addclassstats(self):
        if self.checkjob.get("job") == "Archer":
            self.str = 0
            self.dex = 1
            self.con = 1
            self.int = -1
            self.wis = 0
            self.cha = -1
        elif self.checkjob.get("job") == "Barbarian":
            self.str = 2
            self.dex = 0
            self.con = 1
            self.int = -1
            self.wis = -1
            self.cha = 0
        elif self.checkjob.get("job") == "Cleric":
            self.str = -2
            self.dex = 0
            self.con = 1
            self.int = 0
            self.wis = 2
            self.cha = 0
        elif self.checkjob.get("job") == "Druid":
            self.str = -1
            self.dex = 1
            self.con = 1
            self.int = 0
            self.wis = 2
            self.cha = -1
        elif self.checkjob.get("job") == "Fighter":
            self.str = 1
            self.dex = 1
            self.con = 1
            self.int = -1
            self.wis = 0
            self.cha = 0
        elif self.checkjob.get("job") == "Wizard":
            self.str = -1
            self.dex = 0
            self.con = -1
            self.int = 2
            self.wis = 0
            self.cha = 1

    def listjob(self):
        print(
            """
            
            {}
            STR: {}
            DEX: {}
            CON: {}
            INT: {}
            WIS: {}
            CHA: {}
            
            """
            .format(self.checkjob.get("job"), self.str, self.dex, self.con, self.int, self.wis, self.cha)
        )
        questions = {
            "type": "confirm",
            "name": "jobconf",
            "message": "Would you like to select this class?"
        }
        self.confirmjob = prompt(questions)
        if self.confirmjob.get("jobconf") is True:
            self.nojob = False
        else:
            self.nojob = True


class Character(Name, Job):
    Name()
    Job()


class Play:
    print("Welcome to my character creator!")

    # player name creation
    player = Character()
    player.playername()
    print("Welcome " + player.firstname, player.lastname + " please enjoy my Character Creator.")

    # character name creation
    player.avname()
    print(player.charname + " is a fine name!")

    # player job selection
    player.nojob = True
    while player.nojob:
        player.showjob()
        player.addclassstats()
        player.listjob()

    pprint("End of program")


if __name__ == "__main__":
    Play()
