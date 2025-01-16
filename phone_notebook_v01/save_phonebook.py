import json


# path to JSON
PHONEBOOK_FILE = 'db/phonebook.json'


def save_phonebook(phonebook):
    """SAVE. Function, that saves all current records"""
    with open(PHONEBOOK_FILE, 'w') as file:
        json.dump(phonebook, file, indent=4)