class Name:

    def __init__(self):
        print("Welcome to my character creator!")
        self.firstname = ""
        self.lastname = ""
        self.charname = ""
        self.badname = True

    def playername(self):
        print("First thing is first, I'm going to have you enter your name.")
        first = input("What's your first name? ")

        last = input("What's your last name? ")

        self.firstname = first.title()
        self.lastname = last.title()
        return self.lastname, self.firstname

    def avname(self):
        charname = input("Now, please enter your character's name. ")

        for letter in charname:
            if letter.isdigit():
                self.badname = True
            else:
                self.badname = False
            return self.badname

        self.charname = charname.title()
        return self.charname


class Character(Name):
    player = Name()


class Play:

    #player name creation
    player = Character()
    player.playername()
    print("Welcome " + player.firstname, player.lastname + " please enjoy my Character Creator.")

    #character name creation
    player.avname()

    if player.badname:
        print("Don't enter numbers, you aren't a robot")
        player.avname()
    print(player.charname)


if __name__ == "__main__":
    Play()
