import csv
import random

# Get list from csv and import it


# name of csv file goes here...
with open('country_capitals.csv', 'r') as f:

    # make csv file into list
    file = csv.reader(f)
    next(f)
    my_list = list(file)

# choose an item from the main list, this item is itself a list
question_ans = random.choice(my_list)

# first item in small list
question = question_ans[0]
answer = question_ans[1]

print("Question:What is the capital city of the country {}?".format(question))
print("Answer:{}".format(answer))