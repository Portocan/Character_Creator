from pprint import pprint
from PyInquirer import prompt


class Name:

    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.char_name = ""
        self.bad_name = True

    def player_name(self):
        first = ""
        last = ""
        print("First thing is first, I'm going to have you enter your name.")

        while self.bad_name:
            first = input("What's your first name? ")
            self.check_name(first)

        # resetting bad_name check
        self.bad_name = True

        while self.bad_name:
            last = input("What's your last name? ")
            self.check_name(last)

        self.bad_name = True  # resetting bad_name check

        # formatting player name
        self.first_name = first.title()
        self.last_name = last.title()
        return self.last_name, self.first_name

    def av_name(self):
        char_name = ""

        while self.bad_name:
            char_name = input("Now, please enter your character's name. ")
            self.check_name(char_name)

        self.bad_name = True
        # formatting  character name
        self.char_name = char_name.title()
        return self.char_name

    # Used to check names for numbers and flag them if that is the case
    def check_name(self, name):
        for letter in name:
            if letter.isdigit():
                self.bad_name = True
                print("You can't enter numbers.")
            else:
                self.bad_name = False
            return self.bad_name


class Job:

    def __init__(self):
        self.no_job = True
        self.check_job = {}
        self.confirm_job = {}
        self.str = 0
        self.dex = 0
        self.con = 0
        self.int = 0
        self.wis = 0
        self.cha = 0

    # showing job options
    def show_job(self):
        questions = {
            "type": "list",
            "name": "job",
            "message": "Choose your class",
            "choices": ["Archer", "Barbarian", "Cleric", "Druid", "Fighter", "Wizard"]
        }
        self.check_job = prompt(questions)
        self.no_job = False

    # assigning stats based on class
    def add_class_stats(self):
        if self.check_job.get("job") == "Archer":
            self.str = 0
            self.dex = 1
            self.con = 1
            self.int = -1
            self.wis = 0
            self.cha = -1
        elif self.check_job.get("job") == "Barbarian":
            self.str = 2
            self.dex = 0
            self.con = 1
            self.int = -1
            self.wis = -1
            self.cha = 0
        elif self.check_job.get("job") == "Cleric":
            self.str = -2
            self.dex = 0
            self.con = 1
            self.int = 0
            self.wis = 2
            self.cha = 0
        elif self.check_job.get("job") == "Druid":
            self.str = -1
            self.dex = 1
            self.con = 1
            self.int = 0
            self.wis = 2
            self.cha = -1
        elif self.check_job.get("job") == "Fighter":
            self.str = 1
            self.dex = 1
            self.con = 1
            self.int = -1
            self.wis = 0
            self.cha = 0
        elif self.check_job.get("job") == "Wizard":
            self.str = -1
            self.dex = 0
            self.con = -1
            self.int = 2
            self.wis = 0
            self.cha = 1

    def list_job(self):
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
            .format(self.check_job.get("job"), self.str, self.dex, self.con, self.int, self.wis, self.cha)
        )
        questions = {
            "type": "confirm",
            "name": "job_conf",
            "message": "Would you like to select this class?"
        }
        self.confirm_job = prompt(questions)
        if self.confirm_job.get("job_conf") is True:
            self.no_job = False
        else:
            self.no_job = True


class Character(Name, Job):
    Name()
    Job()


class Play:
    print("Welcome to my character creator!")

    # player name creation
    player = Character()
    player.player_name()
    print("Welcome " + player.first_name, player.last_name + " please enjoy my Character Creator.")

    # character name creation
    player.av_name()
    print(player.char_name + " is a fine name!")

    # player job selection
    player.no_job = True
    while player.no_job:
        player.show_job()
        player.add_class_stats()
        player.list_job()

    pprint("End of program")


if __name__ == "__main__":
    Play()
