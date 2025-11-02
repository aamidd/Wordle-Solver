import random
import re

# store the five-letter words
with open("five_letter_words", "r") as file:
    words = [line.strip() for line in file]

backup = words


def hint():
    return random.choice(words)

# add conditions to filter the words
def add(conditions):
    global words
    if len(conditions.split()) == 1:
        print("you should specify conditions after the add command")
        return
    conditions = conditions.split()[1:]
    for condition in conditions:
        pattern = re.compile(condition)
        words = [word for word in words if pattern.search(word)]

# remove the words with these conditions
def remove(conditions):
    global words
    if len(conditions.split()) == 1:
        print("you should specify conditions after the remove command")
        return
    conditions = conditions.split()[1:]
    for condition in conditions:
        pattern = re.compile(condition)
        words = [word for word in words if not pattern.search(word)]


while True:
    usr_input = input("> ")
    if usr_input == "quit":
        break
    elif usr_input == "print":
        for word in words:
            print(word)
    elif usr_input == "hint":
        print(hint())
    elif "add" in usr_input:
        add(usr_input)
    elif "remove" in usr_input:
        remove(usr_input)
    elif usr_input == "reset":
        words = backup
    else:
        print(f"{usr_input.split()[0]}: not a command")
