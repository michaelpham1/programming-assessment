from tkinter import *


class Start:
    def __init__(self):
        background = "#add8e6"

        # Start GUI
        self.start_frame = Frame(padx=10, pady=10, bg=background)
        self.start_frame.grid()

        # Country Capital Quiz Heading row 0
        self.capital_label = Label(self.start_frame, text="Country Capital Quiz",
                                   font="Calibri 20 bold", bg=background)
        self.capital_label.grid(row=0)

        # Sub text and Instructions for the game row 1
        self.subtext_label = Label(self.start_frame, text="How well do you know world's capitals? \n\n"
                                                          "You'll be presented with capitals from a list of 242 "
                                                          "capitals.\n"
                                                          "You'll need to match the capitals with their corresponding "
                                                          "country. \n\n "
                                                          "Hit the play button to start the quiz",
                                   font="Calibri 10", bg=background)
        self.subtext_label.grid(row=1)

        # to_game button frame row 2
        self.to_game_frame = Frame(self.start_frame, bg=background)
        self.to_game_frame.grid(row=2)

        # Button Font
        button_font = ("Calibri 15 bold")

        # to_game button row 2.0
        self.play_button = Button(self.to_game_frame, text="play", font=button_font, bg="#00FF00",
                                  command=lambda: self.to_game(1), height=1, width=10, borderwidth=2)
        self.play_button.grid(row=0, column=0, padx=10, pady=5)

        # Help Button row 3
        self.help_button = Button(self.start_frame, text="Help", font="Calibri 12 bold", height=2, width=10,
                                  borderwidth=3, command=self.to_help)
        self.help_button.grid(row=3, pady=5)

    def to_game(self, difficulty):
        Game(self,difficulty)

    def to_help(self):
        Help(self)

class Help:
    def __init__(self,partner):
        print("Game instructions")

        partner.help_button.config(state=DISABLED)

class Game:
    def __init__(self,partner, difficulty):
        print(difficulty)
        # Disable the play game button (not yet implemented)
        # partner.play_button.config(state=DISABLED)

        # GUI Setup
        self.game_box = Toplevel()
        self.game_frame = Frame(self.game_box)
        self.game_frame.grid()

        # Capital Label row 0
        self.capital_label = Label(self.game_frame, text="Capital",
                                   font="Calibri 15 bold")
        self.capital_label.grid(row=0)

        # Setup grid for answer buttons row 2
        self.top_answers_frame = Frame(self.game_box)
        self.top_answers_frame.grid(row=2)

        # Top level answers buttons row 2.0
        self.top_left_answer_button = Button(self.top_answers_frame, text="Top left",
                                             font="Calibri 12 bold", padx=5, pady=5,
                                             command=lambda: self.reveal_answer(1))
        self.top_left_answer_button.grid(column=0, row=0)

        self.top_right_answer_button = Button(self.top_answers_frame, text="Top right",
                                              font="Calibri 12 bold", padx=5, pady=5,
                                              command=lambda: self.reveal_answer(2))
        self.top_right_answer_button.grid(column=1, row=0)

        # Bottom level answers buttons row 2.1
        self.bottom_left_answer_button = Button(self.top_answers_frame, text="Bottom left",
                                                font="Calibri 12 bold", padx=5, pady=5,
                                                command=lambda: self.reveal_answer(3))
        self.bottom_left_answer_button.grid(column=0, row=1)

        self.bottom_right_answer_button = Button(self.top_answers_frame, text="Bottom right",
                                                 font="Calibri 12 bold", padx=5, pady=5,
                                                 command=lambda: self.reveal_answer(4))
        self.bottom_right_answer_button.grid(column=1, row=1)

    def reveal_answer(self, location):
        # Print corresponding number based on location
        # Top Left =1 Top Right =2 Bottom Left = 3 Bottom Right = 4
        print(location)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Country Quiz")
    something = Start()
    root.mainloop()