import datetime as dt
import os

class Note:
    def __init__(self, name, text, note_location):
        self.name = name
        self.text = text
        # Get file creation time from the system
        self.time_make = dt.datetime.fromtimestamp(os.path.getctime(note_location))
        self.note_location = note_location

    def show(self):
        print("\n" + "="*30)
        print(f"Name:     {self.name}")
        print(f"Content:  {self.text}")
        print(f"Created:  {self.time_make.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Location: {self.note_location}")
        print("="*30 + "\n")

# Folder name for notes
FOLDER = r"notes/my_notes"

# Create folder if it doesn't exist
if not os.path.exists(FOLDER):
    os.makedirs(FOLDER)

def make_note():
    name = input("Enter note name: ")
    text = input("Enter note text: ")
    
    file_path = os.path.join(FOLDER, f"{name}.txt")
    
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(text)
    
    print(f"Note '{name}' saved to {FOLDER}")
    return Note(name, text, file_path)

def open_note():
    name = input("Enter note name to open: ")
    file_path = os.path.join(FOLDER, f"{name}.txt")
    
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
        return Note(name, text, file_path)
    else:
        print("Error: File not found.")
        return None

def list_notes():
    files = [f.replace(".txt", "") for f in os.listdir(FOLDER) if f.endswith(".txt")]
    if files:
        print("\nYour notes list:")
        for f in files:
            print(f" - {f}")
    else:
        print("\nNotes folder is empty.")

note = None

while True:
    command = input("\nCommand (make / show / list / open / break): ").lower().strip()

    if command == "make":
        note = make_note()

    elif command == "show":
        if note is None:
            print("Please create or open a note first!")
        else:
            note.show()

    elif command == "list":
        list_notes()

    elif command == "open":
        note = open_note()
        if note:
            print(f"Note '{note.name}' successfully loaded.")

    elif command == "break":
        print("Program terminated.")
        break
    else:
        print("Unknown command.")
