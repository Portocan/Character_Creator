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

        self.badname = True     #resetting badname check

        #formatting player name
        self.firstname = first.title()
        self.lastname = last.title()
        return self.lastname, self.firstname

    def avname(self):
        charname = ""

        while self.badname:
            charname = input("Now, please enter your character's name. ")
            self.checkname(charname)

        self.badname = True
        #formatting  character name
        self.charname = charname.title()
        return self.charname

    #Used to check names for numbers and flag them if that is the case
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
        self.charjob = ""


class Character(Name, Job):
    Name()
    Job()


class Play:

    print("Welcome to my character creator!")
    #player name creation
    player = Character()
    player.playername()
    print("Welcome " + player.firstname, player.lastname + " please enjoy my Character Creator.")

    #character name creation
    player.avname()
    print(player.charname + " is a fine name!")


if __name__ == "__main__":
    Play()
