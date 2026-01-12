#TODO import os for save note
#import tkinter or most butiful 
import datetime as dt


class Note:
    def __init__(self, name, text):
        self.name = name
        self.text = text
        self.time_make = dt.datetime.now()

    def show(self):
        print("Name:", self.name)
        print("Text:", self.text)
        print("Create:", self.time_make)

#TODO make function to delate and save note
def make_note():
    name = input("Input name of note: ")
    text = input("Input text of note: ")
    return Note(name, text)


note = None


#TODO add new commands
while True:
    command = input("Command (make / show / break): ")

    if command == "make":
        note = make_note()

    elif command == "show":
        if note is None:
            print("Note is none")
        else:
            note.show()

    elif command == "break":
        break
