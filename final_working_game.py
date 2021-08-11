from tkinter import *
from functools import partial
import csv
import random
import re


class Start:
    def __init__(self):
        # Color is bright green
        background = "#90ee90"

        self.rounds = 0

        # Start GUI
        self.start_box = Toplevel()
        self.start_frame = Frame(self.start_box,padx=10, pady=10, bg=background)
        self.start_frame.grid()

        # Country Capital Quiz Heading row 0
        self.capital_label = Label(self.start_frame, text="Country Capitals Quiz",
                                   font="Calibri 30 bold", bg=background)
        self.capital_label.grid(row=0)

        # Sub text and Instructions for the game row 1
        self.subtext_label = Label(self.start_frame, text="How well do you know world's capitals? \n\n"
                                                          "You'll be presented with capitals from a list of 242 "
                                                          "capitals.\n"
                                                          "You'll need to match the capitals with their corresponding "
                                                          "country. \n\n "
                                                          "Please select the amount of rounds you wish to play.",
                                   font="Calibri 10", bg=background)
        self.subtext_label.grid(row=1)


        # Round warning text row 2

        self.round_warning = Label(self.start_frame,text="If left blank there will be an infinite number of rounds",
                                   font="Calibri 9 italic", fg="red",bg=background)
        self.round_warning.grid(row=2, column=0)

        # Frame for rounds row 3
        self.round_frame = Frame(self.start_frame, bg=background)
        self.round_frame.grid(row=3)

        # Round Label row 0.0
        self.round_label=Label(self.round_frame,text="Rounds:", bg=background, font="Calibri 15")
        self.round_label.grid(row=0,column=0)

        # Round Entry row 0.1
        self.round_entry = Entry(self.round_frame,font="Calibri 20", bg="#FFFFFF"
                                 ,width=5)
        self.round_entry.grid(row=0,column=1,padx=5,pady=5)

        # to_game button frame row 4
        self.to_game_frame = Frame(self.start_frame, bg=background)
        self.to_game_frame.grid(row=4)

        # to_game buttons row 4.0
        self.game_button = Button(self.to_game_frame, text="PLAY GAME", font="Calibri 15 bold", bg="purple", fg="white",
                                  command=self.to_game, height=1, width=12, borderwidth=2,relief="raised")
        self.game_button.grid(row=0, column=0, padx=8, pady=8)


        # Help Button row 5
        self.help_button = Button(self.start_frame, text="Help", font="Calibri 12 bold", height=1, width=8,
                                  borderwidth=3, bg="yellow", command=self.help)
        self.help_button.grid(row=5, pady=5)

    def to_game(self):
        self.rounds=self.round_entry.get()
        if self.rounds == "":
            self.rounds = int(999999999)
            self.infinity = 1
            Game(self)
            self.start_box.destroy()
        else:
            try:
                self.rounds = int(self.rounds)
                self.infinity = 0
                if self.rounds >= 1:
                        Game(self)
                        self.start_box.destroy()
                else:
                    self.round_warning.config(bg="red", text="You may enter a positive integer or leave it blank",
                                              fg="#FFFFFF")
                    self.round_entry.delete(0, "end")
            except ValueError:
                self.round_warning.config(bg="red",text="You may enter a positive integer or leave it blank",
                                          fg="#FFFFFF")
                self.round_entry.delete(0, "end")


    def help(self):
        get_help = Help(self)
        get_help.help_text.configure(text="The quiz will present you with a capital \nYou must identify the "
                                          "corresponding country.\n\n"
                                          "This quiz is multiple choice.\n"
                                        "The quit button will end the game and show your "
                                          "statistics. \n"
                                        "The statistics can be exported into a text file")



class Help:
    def __init__(self, partner):
        background = "#d3d3d3"

        # disable help button
        partner.help_button.config(state=DISABLED)

        # Sets up child window (ie: help box)
        self.help_box = Toplevel()

        # If users press 'x' cross at the top, closes help and 'releases' help button.
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # Set up GUI Frame
        self.help_frame = Frame(self.help_box, bg=background)
        self.help_frame.grid()

        # Set up Help heading (row 0)
        self.how_heading = Label(self.help_frame, text="Game Instructions",
                                 font=("Calibri", "24", "bold",),
                                 bg=background)
        self.how_heading.grid(row=0)

        # Help text (label, row 1)
        self.help_text = Label(self.help_frame, text="", font="Calibri",
                                bg=background, justify=LEFT,wrap=350)
        self.help_text.grid(row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss", width=8, bg="#30D5C8", fg="black",
                                  font="Calibri" "10" "bold", command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # Put help button back to normal...
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


def to_quit():
    root.destroy()


class Game:
    def __init__(self,partner):
        # Background color is light purple/pink
        background = "#efbbf0"

        # Import the csv file, name of csv file goes here...
        with open('country_capitals.csv', 'r') as f:
            # make csv file into list
            file = csv.reader(f)
            next(f)
            my_list = list(file)

        # List to store the answers
        self.game_history = []

        # Initial Score
        self.score = 0

        # Amount of total rounds
        self.total_rounds = partner.rounds

        self.infinity = partner.infinity

        # Amounts of games played
        self.played = 0

        # chooses four different countries / capitals from the list
        question_ans = random.choice(my_list)
        if self.infinity == 0:
            my_list.remove(question_ans)
        else:
            pass
        yes = random.choice(my_list)
        no = random.choice(my_list)
        ok = random.choice(my_list)

        # Defining variables for the capitals and countries,
        # question is the capital in question
        # self.answer is the correct answer
        # incorrect[1,2,3] are the incorrect countries.
        self.question = question_ans[1]
        self.answer = question_ans[0]
        incorrect1 = yes[0]
        incorrect2 = no[0]
        incorrect3 = ok[0]

        # I made the button_list a list so the list can be randomized so that the answer button locations is always
        # different.
        button_list = [self.answer, incorrect1, incorrect2, incorrect3]
        random.shuffle(button_list)
        # Defining the randomized list to their corresponding buttons
        self.top_left = button_list[0]
        self.top_right = button_list[1]
        self.bottom_left = button_list[2]
        self.bottom_right = button_list[3]

        # GUI Setup
        self.game_box = Toplevel(bg=background)
        self.game_frame = Frame(self.game_box, bg=background)
        self.game_frame.grid()
        self.game_box.protocol('WM_DELETE_WINDOW', to_quit)

        # Capital Label row 0
        self.capital_label = Label(self.game_frame, text=self.question,
                                   font="Calibri 15 bold", bg=background)
        self.capital_label.grid(row=0)

        # Label showing correct or incorrect row 1
        self.answer_box = Label(self.game_frame, text="", font="Calibri 12 italic", width=45, bg=background)
        self.answer_box.grid(row=1)

        # Setup grid for answer buttons row 2
        self.top_answers_frame = Frame(self.game_box, width=50, height=50, bg=background)
        self.top_answers_frame.grid(row=2, padx=5)

        # width, wrap, font height for buttons
        wt = 15
        ht = 2
        wr = 120
        ft = "Calibri 14"

        # Top level answers buttons row 2.0
        self.top_left_answer_button = Button(self.top_answers_frame, text=self.top_left,
                                             font=ft, padx=5, pady=5, width=wt, height=ht, wrap=wr, bg="#5ed1ff",
                                             command=lambda: self.reveal_answer(self.top_left))
        self.top_left_answer_button.grid(column=0, row=0, padx=5, pady=5)

        self.top_right_answer_button = Button(self.top_answers_frame, text=self.top_right,
                                              font=ft, padx=5, pady=5, width=wt, height=ht, wrap=wr, bg="#5ed1ff",
                                              command=lambda: self.reveal_answer(self.top_right))
        self.top_right_answer_button.grid(column=1, row=0, padx=5, pady=5)

        # Bottom level answers buttons row 2.1
        self.bottom_left_answer_button = Button(self.top_answers_frame, text=self.bottom_left,
                                                font=ft, padx=5, pady=5, width=wt, height=ht, wrap=wr, bg="#5ed1ff",
                                                command=lambda: self.reveal_answer(self.bottom_left))
        self.bottom_left_answer_button.grid(column=0, row=1, padx=5, pady=5)

        self.bottom_right_answer_button = Button(self.top_answers_frame, text=self.bottom_right,
                                                 font=ft, padx=5, pady=5, width=wt, height=ht, wrap=wr, bg="#5ed1ff",
                                                 command=lambda: self.reveal_answer(self.bottom_right))
        self.bottom_right_answer_button.grid(column=1, row=1, padx=5, pady=5)

        # Label for the score and games played row 3
        self.score_label = Label(self.game_box, text="{} correct, {} rounds played".format(self.score, self.played),
                                 bg=background)
        self.score_label.grid(row=3)

        # Button frames for next, quit button row 4
        self.button_frame = Frame(self.game_box, bg=background)
        self.button_frame.grid(row=4)

        # The quit button so users can quit the game early row 0 column 1
        self.quit_button = Button(self.button_frame, text="Quit",bg="#f75f54",
                                  command=lambda:self.to_end(self.game_history)
                                  , width=10,
                                  font="Calibri 10 bold")
        self.quit_button.grid(row=0, column=0, padx=5, pady=8)


        # The Next button to proceed to the next round row 0 column 2
        self.next_button = Button(self.button_frame, text="Next", bg="#97f587",
                                  command=lambda: self.to_next(my_list, self.game_history,self.infinity), width=10,
                                  font="Calibri 10 bold")
        self.next_button.grid(row=0, column=2, padx=5,pady=8)

        # Disable the next button initially,
        self.next_button.config(state=DISABLED)

    def reveal_answer(self, location):

        # Disable all the buttons
        self.top_left_answer_button.config(state=DISABLED)
        self.top_right_answer_button.config(state=DISABLED)
        self.bottom_left_answer_button.config(state=DISABLED)
        self.bottom_right_answer_button.config(state=DISABLED)


        # Enable the next_button
        self.next_button.config(state=NORMAL)

        # Increase total rounds played by 1
        self.played += 1

        # Check if button is correct.
        if location == self.answer:
            self.answer_box.config(text="Correct!", fg="green")
            self.score += 1
            correct_answer = "{}, the answer was {} \u2713".format(self.question,self.answer)
            self.game_history.append(correct_answer)
        else:
            self.answer_box.config(text="Incorrect, correct country is {}".format(self.answer), fg="red")
            incorrect_answer = "{}, the answer was {} \u274c, you answered {}".format(self.question,self.answer,location)
            self.game_history.append(incorrect_answer)

        # Update the score that the user has
        self.score_label.config(text="{} correct / {} rounds played".format(self.score, self.played))

    def to_next(self, capital_list, history,infinity):
        # if the amount of rounds played is 15 the player is taken to the end screen
        if self.played == self.total_rounds:
            game=1
            played=self.total_rounds
            End(self.score, history,game,played)
            self.game_box.destroy()

        # Else the quiz repeats and new questions are asked.
        else:
            self.top_left_answer_button.config(state=NORMAL)
            self.top_right_answer_button.config(state=NORMAL)
            self.bottom_left_answer_button.config(state=NORMAL)
            self.bottom_right_answer_button.config(state=NORMAL)
            self.next_button.config(state=DISABLED)
            self.answer_box.config(text="")


            # chooses four different countries / capitals from the list
            question_ans = random.choice(capital_list)
            if infinity == 0:
                capital_list.remove(question_ans)
            else:
                pass
            yes = random.choice(capital_list)
            no = random.choice(capital_list)
            ok = random.choice(capital_list)

            # Defining variables for the capitals and countries,
            # question is the capital in question
            # self.answer is the correct answer
            # incorrect[1,2,3] are the incorrect countries.
            self.question = question_ans[1]
            self.answer = question_ans[0]
            incorrect1 = yes[0]
            incorrect2 = no[0]
            incorrect3 = ok[0]


            self.capital_label.config(text=self.question)

            # I made the button_list a list so the list can be randomized so that the answer button locations is always
            # different.
            button_list = [self.answer, incorrect1, incorrect2, incorrect3]
            random.shuffle(button_list)
            self.top_left = button_list[0]
            self.top_right = button_list[1]
            self.bottom_left = button_list[2]
            self.bottom_right = button_list[3]

            # Defining the randomized list to their corresponding buttons
            self.top_left_answer_button.config(text=self.top_left, command=lambda: self.reveal_answer(self.top_left))
            self.top_right_answer_button.config(text=self.top_right, command=lambda: self.reveal_answer(self.top_right))
            self.bottom_left_answer_button.config(text=self.bottom_left,
                                                  command=lambda: self.reveal_answer(self.bottom_left))
            self.bottom_right_answer_button.config(text=self.bottom_right,
                                                   command=lambda: self.reveal_answer(self.bottom_right))


    def to_end(self,history):
        game=1
        End(self.score,history,game,self.played)
        self.game_box.destroy()

class End:
    def __init__(self, score, history,difficulty,played):
        # Background color is light purple/pink
        background = "#efbbf0"

        # Accuracy percentage
        if played == 0:
            percentage = 0
        else:
            percentage = (score/played) * 100

        # End Frame
        self.end_box = Toplevel()
        self.end_frame = Frame(self.end_box, bg=background)
        self.end_frame.grid(row=0)
        self.end_box.protocol('WM_DELETE_WINDOW', to_quit)

        # Heading row 0
        self.end_heading = Label(self.end_frame, text="Thanks for playing!", font="Calibri 25 bold", bg=background)
        self.end_heading.grid(row=0, padx=10)

        # Game statistics row 1
        self.end_stats = Label(self.end_frame, text="You were correct for {} out of {} rounds \n\n"
                                                    "Accuracy : {:.2f}%".format(score,played, percentage),
                               bg=background, font="Calibri 10")
        self.end_stats.grid(row=1)


        # Export, play again, Quit buttons
        self.end_buttons = Frame(self.end_frame, bg=background)
        self.end_buttons.grid(row=2)

        # Export button row 0 column 0
        self.end_export_button = Button(self.end_buttons, text="Export", font="Calibri 10 bold",
                                        command=lambda: self.to_export(history,difficulty,score,percentage,played), width=10
                                        , bg="#30D5C8", height=2)
        self.end_export_button.grid(row=0, column=0, padx=6, pady=5)

        # play again Button row 0 column 1
        self.end_retry_button = Button(self.end_buttons, text="Play Again!", font="Calibri 10 bold",
                                       command=self.to_start, width=10, bg="#97f587", height=2)
        self.end_retry_button.grid(row=0, column=1, padx=6, pady=5)

        # Quit button row 0 column 2
        self.end_quit_button = Button(self.end_buttons, text="Quit", font="Calibri 10 bold",
                                      command=root.quit, width=10, bg="#f75f54", height=2)
        self.end_quit_button.grid(row=0, column=2, padx=6, pady=5)

    def to_start(self):
        Start()
        self.end_box.destroy()

    def to_export(self, history,difficulty,score,percentage,played):
        Export(self, history,difficulty,score,percentage,played)


class Export:
    def __init__(self, partner, history,difficulty,score,percentage,played):

        # Background Color is light purple/pink
        background = "#efbbf0"

        # disable export button
        partner.end_export_button.config(state=DISABLED)

        # Sets up child window (ie: export box)
        self.export_box = Toplevel()

        # If users press 'x' cross at the top, closes export and 'releases' export button.
        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.close_export, partner))

        # Set up GUI Frame
        self.export_frame = Frame(self.export_box, width=300, bg=background)
        self.export_frame.grid()

        # Set up Export heading (row 0)
        self.how_heading = Label(self.export_frame, text="Export / Instructions",
                                 font="Calibri 15 bold", bg=background)
        self.how_heading.grid(row=0)

        # Export text (label, row 1)
        self.export_text = Label(self.export_frame, text="Enter a filename in the box below",
                                 justify=LEFT, width=40, wrap=250, bg=background)
        self.export_text.grid(row=1)

        # Warning text (label, row2)
        self.export_text = Label(self.export_frame, text="If the filename you entered already exists,"
                                                         " it will be replaced.", justify=LEFT,
                                 fg='red', font="Calibri 10 italic", bg=background,
                                 wrap=225, padx=10, pady=10)
        self.export_text.grid(row=2, pady=10)

        # Filename Entry Box (row 3)
        self.filename_entry = Entry(self.export_frame, width=20,
                                    font="Calibri 14 bold", justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        # Error Message Labels (initially blank, row 4)
        self.save_error_label = Label(self.export_frame, text="", fg="maroon", bg=background
                                      )
        self.save_error_label.grid(row=4)

        # Save / Cancel Frame (row 5)
        self.save_cancel_frame = Frame(self.export_frame, bg=background)
        self.save_cancel_frame.grid(row=5, pady=10)

        # Save and Cancel buttons (row 0 of save_cancel_frame)
        self.save_button = Button(self.save_cancel_frame, text="Save", width=8,bg="#5ed1ff",
                                  command=partial(lambda: self.save_history(partner, history,difficulty,score,percentage,played)))
        self.save_button.grid(row=0, column=0,padx=5,pady=5)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel",width=8,bg="#5ed1ff",
                                    command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=1,padx=5,pady=5)

    def close_export(self, partner):
        # Put export button back to normal...
        partner.end_export_button.config(state=NORMAL)
        self.export_box.destroy()

    def save_history(self, partner, history,difficulty,score,percentage,played):
        global problem

        valid_char = "[A-Za-z0-9_]"
        has_error = "no"

        filename = self.filename_entry.get()

        for letter in filename:
            if re.match(valid_char, letter):
                continue

            elif letter == " ":
                problem = " (no spaces allowed)"

            else:
                problem = ("(no {}'s allowed)".format(letter))
            has_error = "yes"
            break

        if filename == "":
            problem = "can't be blank"
            has_error = "yes"

        if has_error == "yes":
            self.save_error_label.config(text="Invalid filename - {}".format(problem))

            self.filename_entry.config(bg="#ffafaf")

        else:
            filename = filename + ".txt"

            f = open(filename, "w+", encoding="utf-8")

            f.write("\n\nGame Details\n\n"
                    "You got {} out of {} correct\n\n"
                    "Percentage Correct = {:.2f}% \n\n".format(score,played,percentage))
            f.close()

            self.close_export(partner)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.withdraw()
    root.title("Country Quiz")
    something = Start()
    root.mainloop()
