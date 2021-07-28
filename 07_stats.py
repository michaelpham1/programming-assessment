# Make an if statement to go to the end of the game.
x = input("")
if x == "a":
    Game()
else:
    print("e")


class Game:
    def __init__(self):
        # End Frame
        self.end_box = Toplevel()
        self.end_frame = Frame(self.end_box)
        self.end_frame.grid(row=0)


        # Heading row 0
        self.end_heading = Label(self.end_frame, text="Thanks for playing!", font="Calibri 20 bold")
        self.end_heading.grid(row=0)