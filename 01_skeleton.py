from tkinter import *


class Start:
    def __init__(self):
        # Start GUI
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # Country Capital Quiz Heading row 0
        self.capital_label = Label (self.start_frame, text="Country Capitals Quiz",
                                    font= "Calibri 20 bold")
        self.capital_label.grid(row=0)

        # to_game button row 1
        self.play_button = Button(text="Play", command=lambda: self.to_game(0))
        self.play_button.grid(row=1)

    def to_game(self, difficulty):
        Game(self,difficulty)

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
                                   font="Calibri 16 bold")
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
                                             font="Calibri 12 bold", padx=5,pady=5,
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
        # Top Left = 1 Top Right =2 Bottom Left = 3 Bottom Right = 4
        print(location)





# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Country Quiz")
    something = Start()
    root.mainloop()
